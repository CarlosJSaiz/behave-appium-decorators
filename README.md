# Python Appium Behave project using decorators for elements location

This project include:

- Test on Android and Appium versions of the same app.
- Decorators to get elements in Android and iOS.
- Page Object design pattern.
- Basic actions and scrolling method to use in any project.
- External config file and final report with screenshots.

## Dependencies

**1. Testing app**
The app is developed by [Saucelabs](https://saucelabs.com/) in [this repository](https://github.com/saucelabs/sample-app-mobile#contributing-to-the-app)

**2. Report**
The report library is developed by [Allure](http://allure.qatools.ru/) in [this repository](https://github.com/allure-framework/allure2)

## Installation

**1. Install all the requirements for the project.**

```bash
pip install -r requirements.txt
```

**2. Install [Saucelabs test app](https://github.com/saucelabs/sample-app-mobile/releases) in your cellphone or simulator**

**3. Modify config.json with your data**

```json
  "platform": "android or iOS",
  "real_device": true or false,
  "port": "port of your appium service (usually 4723)",
```

For iOS simulator

```json
"iOS_config": {
    "platformVersion": "YOUR VERSION",
    "deviceName": "PHONE THAT YOU WANT TO USE",
  }
```

for iOS real device

```json
"iOS_device_config": {
    "platformVersion": "YOUR VERSION",
    "deviceName": "YOUR DEVICE NAME",
    "udid": "YOUR UDID",
    "xcodeOrgId": "YOUR XCODE",
  }
```

## Usage

**1. Connect your device or open your simulator**

Then execute:

```bash
behave
```

**2. To create report**

Install Allure commandline: _You need NodeJS for this_

```bash
npm install -g allure-commandline
```

Temporal report:

```bash
allure serve allure
```

Generate Report:

```bash
allure generate allure -o allure-report
```
