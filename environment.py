import os
import json
import string
import random


from pathlib import Path

from behave import fixture

from behave.fixture import use_fixture
from appium import webdriver

from myAllure import Report

from PIL import Image
from resizeimage import resizeimage

config_path = Path.cwd() / "config.json"


def before_all(context):
    '''
    Set basic attributes to run tests.
    Initialize appium driver.
    '''
    with open(str(config_path)) as json_file:
        config_data = json.load(json_file)
    keys = ['port', 'platform', 'real_device', 'report_dir_name']
    context.config_data = {}
    for key in keys:
        context.config_data[key] = config_data[key]
    context.report_dir_name = config_data['report_dir_name']
    context.android_sim_cap = config_data['android_config']
    context.android_real_cap = config_data['android_config']
    context.ios_sim_cap = config_data['iOS_config']
    context.ios_real_cap = config_data['iOS_device_config']

    if not os.path.exists(str(Path.cwd() / "allure/pictures")):
        os.makedirs(str(Path.cwd() / "allure/pictures"))

    context.allure = Report(context.config_data['report_dir_name'], report_name='SwagLabs ' + context.config_data['platform'],
                            app_type="iOS & Android", re_create=False)
    use_fixture(init_driver, context)


def before_feature(context, feature):
    context.allure.before_feature(feature)


def before_scenario(context, scenario):
    context.allure.before_scenario(scenario)


def before_step(context, step):
    context.allure.before_step(step)


def after_step(context, step):
    context.allure.after_step(step, attachments=take_screenshot(context))


def after_scenario(context, scenario):
    context.allure.after_scenario(scenario)


def after_all(context):
    context.allure.after_all()


def take_screenshot(context):
    '''
    Takes screenshot and attach it to Allure Report
    '''
    path = "pictures/" + get_random_string() + '.jpg'
    context.driver.save_screenshot(context.report_dir_name + "/" + path)
    resize_image(context.report_dir_name + "/" + path)
    return [{"title": "Image", "filename": path, "type": "image/png"}]


def get_random_string(length=10):
    random_list = []
    for i in range(length):
        random_list.append(random.choice(
            string.ascii_uppercase + string.digits))
    return ''.join(random_list)


def resize_image(path):
    fd_img = open(os.path.join(path), 'rb')
    img = Image.open(fd_img)
    img = resizeimage.resize_height(img, 600)
    img.save(path, img.format)
    fd_img.close()


@fixture
def init_driver(context):
    if context.config_data['platform'] == "android":
        if context.config_data['real_device']:
            capabilities = context.android_real_cap
        else:
            capabilities = context.android_sim_cap
    else:
        if context.config_data['real_device']:
            capabilities = context.ios_real_cap
        else:
            capabilities = context.ios_sim_cap
    context.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:' +
        context.config_data['port'] + '/wd/hub',
        desired_capabilities=capabilities)
    yield context.driver
