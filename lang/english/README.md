# ComplexParser 

<p align="center">
  <a href="https://github.com/inmovery/ComplexParser/tree/master#ComplexParser">Русский</a> |
  <a href="https://github.com/inmovery/ComplexParser/tree/master/lang/english#ComplexParser">English</a>
</p>

Application is intended for data collection (parsing) from the site [https://freedom-stat.com](https://freedom-stat.com). 
The functionality of most sites includes registration and authorization, because of which it is impossible to obtain data from the site pages in a normal way (for example, using the `curl` library). Authorization requires user activity.
This project provides for such a situation — demonstrates the process of collecting combat statistics for Mortal Combat at bookmakers.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Requirements](#requirements)
  - [Requirements to programming languages](#requirements-to-programming-languages)
  - [Requirements to dependencies](#requirements-to-dependencies)
- [Installation](#installation)
  - [Registration on the site](#registration-on-the-site)
    - [Getting access](#getting-access)
    - [Result](#result)
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

### Requirements to programming languages
- Python 3.6, 3.7 and their modifications

### Requirements to dependencies
The following dependencies (modules) must be installed:
- [Selenium](https://pypi.org/project/selenium/).
- [Pandas](https://pypi.org/project/pandas/).
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/).
- [SendGrid](https://pypi.org/project/sendgrid/).

To install the required dependencies, run the following command line code:
```
pip install selenium
pip install pandas
pip install bs4
pip install sendgrid
```

## Installation

### Connect to the site
The following options are required to access the [site](https://freedom-stat.com):
1. Mail.
2. Password.
3. Access to statistics on the [site](https://freedom-stat.com).

#### Getting access:
To access the site, follow these steps:
1. Log in to the mail service (e.g. via [temp-mail.org](https://temp-mail.org))
![Step 1](https://github.com/inmovery/ComplexParser/blob/master/images/1.png?raw=true)
2. Confirm your mail.
![Step 2](https://github.com/inmovery/ComplexParser/blob/master/images/2.png?raw=true)
![Step 3](https://github.com/inmovery/ComplexParser/blob/master/images/3.png?raw=true)
3. On [freedom-stat.com](https://freedom-stat.com) go to the tasks section and click the following buttons in sequence:
  3.1. "Проверить" (to verify email confirmation)
  ![Step 4](https://github.com/inmovery/ComplexParser/blob/master/images/4.png?raw=true)
  3.2. "Получить награду" (in order to activate the free use of the site for 1 hour)
  ![Step 5](https://github.com/inmovery/ComplexParser/blob/master/images/5.png?raw=true)

#### Result 
Результатом является доступ к таблице [статистики Mortal Combat](https://freedom-stat.com/stats/mk).
##### An example of a table from which data is collected
![Step 6](https://github.com/inmovery/ComplexParser/blob/master/images/6.png?raw=true)

### Getting API_KEY for sending mail
To get API_key, do the following:
1. Register at [sendgrid.com](https://sendgrid.com).
2. Log in to [sendgrid.com](https://sendgrid.com).
3. Go to Dashboard.
4. Click the Email API tab on the left side of the screen, select Integration Guide from the menu, and click Web API.
![Step 1](https://github.com/inmovery/ComplexParser/blob/master/images/8.png?raw=true)
5. Create API_KEY by selecting the Python programming language.
![Step 2](https://github.com/inmovery/ComplexParser/blob/master/images/9.png?raw=true)
![Step 3](https://github.com/inmovery/ComplexParser/blob/master/images/10.png?raw=true)
6. Confirm connection.

### Heroku Setup

To connect to Heroku:
1. Register at [Heroku.com](https://heroku.com).
2. Log in to [Heroku.com](https://heroku.com).
3. Create a new application by clicking on the "New" button in the upper right corner of the screen.
4. Go to Settings.
5. Go to Buildpacks and add the following dependencies:
```
    heroku/python
    https://github.com/heroku/heroku-buildpack-chromedriver
    https://github.com/heroku/heroku-buildpack-google-chrome
```
6. Go to the Config Vars section and click the "Reveal Config Vars" button.
7. In the `key` field, enter `CHROMEDRIVER_path`, and in the `value` field enter `/app/.chromedriver/bin/chromedriver`, and then click the "Add" button.
8. Enter `GOOGLE_CHROME_bin` in the `key` field, and enter `/app/.apt/usr/bin/google-chrome` in the `value` field, and then click the Add button.

![Instructions](https://github.com/inmovery/ComplexParser/tree/master/images/7.jpg)

### Setting values
Set the constants `URL_PARSE`, `EMAIL`, `PASSWORD`, `SENDGRID_API_key`, `FROM_EMAIL`, `TO_EMAIL` according to the data that you have been in the installation phase.

## Using
Download the application:
- Via the command line, using the GitHub's capabilities: `git clone https://github.com/inmovery/ComplexParser.git`.
- Via download [archive](https://github.com/inmovery/ComplexParser/archive/master.zip).

Application can be run from the command line `python main.py` and the IDE PyCharm.

## Deployment

### Local deployment
To use the application on your computer:
1. Download [chromedriver (Google Chrome)](https://chromedriver.chromium.org/downloads) or [Teckodriver (Firefox)](https://github.com/mozilla/geckodriver/releases). After downloading, move to the folder containing the `main.py` file.
2. Use the following code in the driver selenium initialization (at the beginning of the code):
  `driver = webdriver.Chrome()`.

### Server deployment
To deploy on the server, use the features of Heroku. To connect and use Google Chrome Driver, use following code in the driver selenium initialization (at the beginning of the code):
```
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
```

After configuring Heroku, the deployment of the application is the following sequence of commands, which implies the use of Heroku CLI:
```
heroku login
git init
heroku get:remote -a complex-parser
git add .
git commit -m “initial commit”
pip3 freeze > requirements.txt
echo worker : python  main.py > Procfile
git push heroku master
heroku run python main.py
heroku scale worker=1
heroku logs --tail
```

## FAQ

If you have any questions about how the application works, create a GitHub [Issues](https://github.com/inmovery/ComplexParser/issues).
