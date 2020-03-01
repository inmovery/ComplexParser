## ComplexParser 

<p align="center">
  <a href="https://github.com/inmovery/ComplexParser/tree/master#ComplexParser">Русский</a> |
  <a href="https://github.com/inmovery/ComplexParser/tree/master/lang/russian#ComplesParser">English</a>
</p>

This project is intended for data collection (parsing) from the site `https://freedom-stat.com`. 
The functionality of most sites includes registration and authorization, because of which it is impossible to obtain data from the site pages in a normal way (for example, using the `curl` library). Authorization requires user activity.
This project provides for such a situation. This project demonstrates the process of collecting combat statistics for mortal Combat at bookmakers.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Requirements](#requirements)
  - [Requirements to sowtware](#requirements-for-software)
  - [Requirements to dependencies](#requirements-to-dependencies)
- [Installation](#installation)
  - [Connect to the site](#connect-to-the-site)
    - [Getting access](#getting-access)
  - [Installation of dependencies](#installation-of-dependencies)
  - [Getting API_KEY for sending mail](#getting-api_key-for-sending-mail)
  - [Heroku Setup](#heroku-setup) 
  - [Setting values](#setting-values)
- [Using](#using)
- [Deployment](#deployment)
  - [Local deployment](#local-deployment)
  - [Server deployment](#server-deployment) 
- [FAQ](#faq)

## Requirements

### Requirements to sowtware
- Python 3.6, 3.7 and their modifications

### Requirements to dependencies
The following dependencies must be installed:
1. selenium
2. pandas
3. bs4
4. sendgrid

## Installation

### Connect to the site
In order to access the site you need 3 parameters:
1. Mail
2. Password
3. Access to statistics on the site

#### Getting access:
- Register (e.g. temp-mail.org)
- Confirm your mail
- Log in to the tasks section and click on the following commands:
  - Check the progress
  - To Receive the award

![Step 1](https://github.com/inmovery/ComplexParser/tree/master/images/1.jpg)
![Step 2](https://github.com/inmovery/ComplexParser/tree/master/images/2.jpg)
![Step 3](https://github.com/inmovery/ComplexParser/tree/master/images/3.jpg)
![Step 4](https://github.com/inmovery/ComplexParser/tree/master/images/4.jpg)
![Step 5](https://github.com/inmovery/ComplexParser/tree/master/images/5.jpg)
![Step 6](https://github.com/inmovery/ComplexParser/tree/master/images/6.jpg)

### Installation of dependencies
- Installing the module SendGrid
  `pip install sendgrid`
- Installing the module Selenium
  `pip install selenium`
- Installing the module BeautifulSoup
  `pip install bs4`
- Installing the Data Module
  `pip install pandas`

### Getting API_KEY for sending mail

1. Register at [sendgrid.com](https://sendgrid.com)
2. Log in to [sendgrid.com](https://sendgrid.com)
3. Go to Dashboard
4. Select the tab on the left side of the Email API screen and select Integration Guide in the pop-up window
5. Then select "Web API".
6. Select Python
7. Create API key
8. Confirm connection.

![Step 1](https://github.com/inmovery/ComplexParser/tree/master/images/8.jpg)
![Step 2](https://github.com/inmovery/ComplexParser/tree/master/images/9.jpg)
![Step 3](https://github.com/inmovery/ComplexParser/tree/master/images/10.jpg)

### Heroku Setup

To connect to heroku, follow the following algorithm:
1. Register at [Heroku.com](https://heroku.com)
2. Log in to [Heroku.com](https://heroku.com)
3. Create a new application by clicking on the "New" button in the upper right corner of the screen
4. Go to Settings
5. Go to Buildpacks and add the following dependencies:
```
    heroku/python
    https://github.com/heroku/heroku-buildpack-chromedriver
    https://github.com/heroku/heroku-buildpack-google-chrome
```
6. Go to the Config Vars section and click the reveal Config Vars button
7. In the `key` field, enter `CHROMEDRIVER_path`, and in the `value` field enter `/app/.chromedriver/bin/chromedriver`, and then click the add button
8. Enter `GOOGLE_CHROME_bin` in the `key` field, and enter `/app/.apt/usr/bin/google-chrome` in the `value` field, and then click the Add button.

![Instructions](https://github.com/inmovery/ComplexParser/tree/master/images/7.jpg)

### Setting values
Set the constants `URL_PARSE`, `EMAIL`, `PASSWORD`, `SENDGRID_API_key`, `FROM_EMAIL`, `TO_EMAIL` according to the data that you have been in the installation phase.

## Using
Download the application:
1. Via the command line, using the GitHub's capabilities: `git clone https://github.com/inmovery/ComplexParser.git`
2. Via download [archive](https://github.com/inmovery/ComplexParser/archive/master.zip)
This program can be run from the command line `python main.py` and the IDE PyCharm.

## Deployment

### Local deployment
In order to use the program on your computer:
1. Download [chromedriver (Google Chrome)](https://chromedriver.chromium.org/downloads) or [Teckodriver (Firefox)](https://github.com/mozilla/geckodriver/releases)
  After downloading, move to the folder containing the `main.py` file
2. Use the following code in the driver selenium initialization (at the beginning of the code):
  `driver = webdriver.Chrome()`

### Server deployment
To turn on the server, use the features of Heroku. To connect and use Google Chrom Driver, use the blind code in the driver selenium initialization (at the beginning of the code):
```
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
```

After configuring Heroku, the deployment of the application is the following sequence of commands, which implies the use of Heroku CLI:
1. heroku login
2. git init
3. heroku get:remote -a complex-parser
4. git add .
5. git commit -m “initial commit”
6. pip3 freeze > requirements.txt
7. echo  > Procfile
8. Open the Profile file and add "worker : python main.py`
9. git push heroku master
10. heroku run python main.py
11. heroku scale worker=1
12. heroku logs --tail

## FAQ

See and ask questions in [Issues](https://github.com/inmovery/ComplexParser/issues)
