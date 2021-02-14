from behave import given, when, then
from Pages.LoginScreen.LoginScreenActions import LoginScreenActions
from Pages.LoginScreen.LoginScreenAsserts import LoginScreenAsserts
from Pages.ProductsScreen.ProductsScreenAsserts import ProductsScreenAsserts
from Pages.ProductsScreen.ProductsScreenScrolls import ProductsScreenScrolls


@given('I am on Login screen')
def step_impl(context):
    LoginScreenAsserts(context.driver).login_screen_is_displayed()


@given('I am on Products screen')
def step_impl(context):
    ProductsScreenAsserts(context.driver).products_screen_is_displayed()


@when('I insert username "{user}" and password "{password}"')
def step_impl(context, user, password):
    LoginScreenActions(context.driver).login(user, password)


@when('I put baby tshirt on screen')
def step_impl(context):
    ProductsScreenScrolls(context.driver).put_on_viemport_baby_tshirt()


@then('Products screen is displayed')
def step_impl(context):
    ProductsScreenAsserts(context.driver).products_screen_is_displayed()


@then('The price should be "{price}"')
def step_impl(context, price):
    ProductsScreenAsserts(context.driver).check_price_is_correct(price)
