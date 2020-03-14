# ComplexParser

<p align="center">
  <a href="https://github.com/inmovery/ComplexParser/tree/master#ComplexParser">Русский</a> |
  <a href="https://github.com/inmovery/ComplexParser/tree/master/lang/english#ComplexParser">English</a>
</p>

Приложение предназначено для сбора данных (парсинга) с сайта [https://freedom-stat.com](https://freedom-stat.com). 
Функциональность большинства сайтов включает в себя регистрацию и авторизацию, из-за чего получить данные со страниц сайта обычный способом (например, при помощи библиотеки `curl`) невозможно. Авторизация требует активности пользователя.
В приложении предусмотрена подобная ситуация — продемонстрирован процесс сбора статистики боёв игры Mortal Combat на букмекерских компаниях.

## Содержание

- [Содержание](#содержание)
- [Требования](#требования)
  - [Требования к языкам программирования](#требования-к-языкам-программирования)
  - [Требования к зависимостям](#требования-к-зависимостям)
- [Установка](#установка)
  - [Регистрация на сайте](#регистрация-на-сайте)
    - [Получение доступа](#получение-доступа)
    - [Результат](#результат)
  - [Получение API_KEY для отправки почты](#получение-api_key-для-отправки-почты)
  - [Настройка Heroku](#настройка-heroku) 
  - [Установка значений](#установка-значений)
- [Использование](#использование)
- [Развёртывание](#развёртывание)
  - [Локальное развёртывание](#локальное-развёртывание)
  - [Серверное развёртывание](#серверное-развёртывание)
- [Вопросы](#вопросы)

## Требования

### Требования к языкам программирования
- Python 3.6, 3.7 и их модификации.

### Требования к зависимостям
Должны быть установлены следующие зависимости (модули):
- [Selenium](https://pypi.org/project/selenium/).
- [Pandas](https://pypi.org/project/pandas/).
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/).
- [SendGrid](https://pypi.org/project/sendgrid/).

Чтобы установить требуемые зависимости, выполните следующий код в командной строке:
```
pip install selenium
pip install pandas
pip install bs4
pip install sendgrid
```

## Установка

### Регистрация на сайте
Чтобы получить доступ к [сайту](https://freedom-stat.com), необходимы следующие параметры:
1. Почта.
2. Пароль.
3. Доступ на [сайте](https://freedom-stat.com) к получению статистики Mortal Combat.

#### Получение доступа
Чтобы получить доступ к сайту, выполните следующие действия:
- Зарегистрируйтесь на почтовом сервисе (например, на сайте [temp-mail.org](https://temp-mail.org)).
![Шаг 1](https://github.com/inmovery/ComplexParser/blob/master/images/1.png?raw=true)
- Подтвердите свою почту и получите данные для авторизации.
![Шаг 2](https://github.com/inmovery/ComplexParser/blob/master/images/2.png?raw=true)
![Шаг 3](https://github.com/inmovery/ComplexParser/blob/master/images/3.png?raw=true)
- На сайте [freedom-stat.com](https://freedom-stat.com) перейдите в раздел «Задания» и последовательно нажмите на следующие кнопки:
  - "Проверить" (для того, чтобы верифицировать подтверждение почты)
  ![Шаг 4](https://github.com/inmovery/ComplexParser/blob/master/images/4.png?raw=true)
  - "Получить награду" (для того, чтобы активировать бесплатный режим пользования сайтом на 1 час)
  ![Шаг 5](https://github.com/inmovery/ComplexParser/blob/master/images/5.png?raw=true)

#### Результат 
Результатом является доступ к таблице [статистики Mortal Combat](https://freedom-stat.com/stats/mk).
##### Пример таблицы, из которой собираются данные
![Шаг 6](https://github.com/inmovery/ComplexParser/blob/master/images/6.png?raw=true)

### Получение API_KEY для отправки почты
Чтобы получить API_KEY, выполните следующие действия:
1. Зарегистрируйтесь на сайте [sendgrid.com](https://sendgrid.com).
2. Авторизуйтесь на сайте [sendgrid.com](https://sendgrid.com).
3. Перейдите в раздел «Dashboard».
4. Перейдите на вкладку «Email API» в левой части экрана, выберите в меню «Integration Guide» и кликните по "Web API".
![Шаг 1](https://github.com/inmovery/ComplexParser/blob/master/images/8.png?raw=true)
5. Создайте API KEY, выбрав язык программирования Python.
![Шаг 2](https://github.com/inmovery/ComplexParser/blob/master/images/9.png?raw=true)
![Шаг 3](https://github.com/inmovery/ComplexParser/blob/master/images/10.png?raw=true)
6. Подтвердите подключение.

### Настройка Heroku

Чтобы подключиться к Heroku выполните следующие действия:
1. Зарегистрируйтесь на сайте [Heroku.com](https://heroku.com).
2. Авторизуйтесь на сайте [Heroku.com](https://heroku.com).
3. Создайте новое приложение, нажав на кнопку «New» в правом верхнем углу экрана.
4. Перейдите в раздел «Settings».
5. Перейдите к разделу «Buildpacks» и добавить следующие зависимости:
```
    heroku/python
    https://github.com/heroku/heroku-buildpack-chromedriver
    https://github.com/heroku/heroku-buildpack-google-chrome
```
6. Перейдите к разделу «Config Vars» и нажать на кнопку «Reveal Config Vars».
7. В поле `KEY` введите `CHROMEDRIVER_PATH`, а в поле `VALUE` введите `/app/.chromedriver/bin/chromedriver`, после чего нажмите на кнопку «Add».
8. В поле `KEY` введите `GOOGLE_CHROME_BIN`, а в поле `VALUE` введите `/app/.apt/usr/bin/google-chrome`, после чего нажмите на кнопку «Add».

![Инструкция](https://github.com/inmovery/ComplexParser/blob/master/images/7.png?raw=true)


### Установка значений
Установите константы `URL_PARSE`, `EMAIL`, `PASSWORD`, `SENDGRID_API_KEY`, `FROM_EMAIL`, `TO_EMAIL` в файле `settings.py` в соответствии с теми данными, которые вы получили на этапе установки.

## Использование
Скачайте приложение:
- Через командную строку, используя возможности GitHub: `git clone https://github.com/inmovery/ComplexParser.git`.
- Через скачивание [архива](https://github.com/inmovery/ComplexParser/archive/master.zip).

Приложение можно запустить как через командную строку `python main.py`, так и в IDE PyCharm.

## Развёртывание

### Локальное развёртывание
Чтобы использовать приложение на своём компьютере:
1. Скачайте [chromedriver (Google Chrome)](https://chromedriver.chromium.org/downloads) или [geckodriver (Firefox)](https://github.com/mozilla/geckodriver/releases). После скачивания переместите скаченные данные в папку с файлом `main.py`.
2. Используйте следующий код в инициализации driver selenium (в начале кода):
    `driver = webdriver.Chrome()`.

### Серверное развёртывание
Чтобы развернуть приложение на сервере, используются возможности Heroku. Чтобы подключить и использовать Google Chrome Driver, используйте следующий код в инициализации driver selenium (в начале кода):
```
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
```

После настройки Heroku развёртывание приложения представляет из себя следующую последовательность команд, которая подразумевает использование Heroku CLI:
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

## Часто задаваемые вопросы

Если у вас есть возникли вопросы по работе приложения, создайте GitHub [Issues](https://github.com/inmovery/ComplexParser/issues).
