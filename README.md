# ComplexParser

<p align="center">
  <a href="https://github.com/inmovery/ComplexParser/tree/master#ComplexParser">Русский</a> |
  <a href="https://github.com/inmovery/ComplexParser/tree/master/lang/english#ComplexParser">English</a>
</p>

Данный проект предназначен для сбора данных (парсинга) с сайта `https://freedom-stat.com`. 
Функциональность большинства сайтов включает в себя регистрацию и авторизацию, из-за чего получить данные со страниц сайта обычный способом (например, при помощи библиотеки `curl`) невозможно. Авторизация требует активности пользователя.
В данном проекте предусмотрена подобная ситуация. В данном проекте продемонстрирован процесс сбора статистики боёв игры Mortal Combat на букмекерских компаниях.

## Содержание

- [Содержание](#содержание)
- [Требования](#требования)
  - [Требования к программному обеспечению](#требования-к-программному-обеспечению)
  - [Требования к зависимостям](#требования-к-зависимостям)
- [Установка](#установка)
  - [Подключение к сайту](#подключение-к-сайту)
    - [Получение доступа](#получение-доступа)
  - [Установка зависимостей](#установка-зависимостей)
  - [Получение API_KEY для отправки почты](#получение-api_key-для-отправки-почты)
  - [Настройка Heroku](#настройка-heroku) 
  - [Установка значений](#установка-значений)
- [Использование](#использование)
- [Развёртывание](#развёртывание)
  - [Локальное развёртывание](#локальное-развёртывание)
  - [Серверное развёртывание](#серверное-развёртывание) 
- [Вопросы](#вопросы)

## Требования

### Требования к программному обеспечению
- Python 3.6, 3.7 и их модификации

### Требования к зависимостям
Должны быть установлены следующие зависимости:
1. selenium
2. pandas
3. bs4
4. sendgrid

## Установка

### Подключение к сайту
Для того, чтобы получить доступ к сайту необходимы 3 параметра:
1. Почта
2. Пароль
3. Доступ на сайте к получению статистики

#### Получение доступа:
- Зарегистрироваться (например, через сайт temp-mail.org)
- Подтвердить свою почту
- Зайти в раздел «Задания» и нажать следующие команды:
  - Проверить выполнение
  - Получить награду
  
#### Регистрация
![Шаг 1](https://github.com/inmovery/ComplexParser/blob/master/images/1.png?raw=true)

#### Получение письма
![Шаг 2](https://github.com/inmovery/ComplexParser/blob/master/images/2.png?raw=true)

#### Подтверждение почты и получение данных для авторизации
![Шаг 3](https://github.com/inmovery/ComplexParser/blob/master/images/3.png?raw=true)

#### Получение доступа к сайту. Шаг 1
![Шаг 4](https://github.com/inmovery/ComplexParser/blob/master/images/4.png?raw=true)

#### Поулчение доступа к сайту. Шаг 2
![Шаг 5](https://github.com/inmovery/ComplexParser/blob/master/images/5.png?raw=true)

#### Пример таблицы, из которой собираются данные
![Шаг 6](https://github.com/inmovery/ComplexParser/blob/master/images/6.png?raw=true)

### Установка зависимостей
- Установка модуля SendGrid
  `pip install sendgrid`
- Установка модуля Selenium
  `pip install selenium`
- Установка модуля BeautifulSoup
  `pip install bs4`
- Установка модуля для работы с данными
  `pip install pandas`

### Получение API_KEY для отправки почты

1. Зарегистрироваться на сайте [sendgrid.com](https://sendgrid.com)
2. Авторизоваться на сайте [sendgrid.com](https://sendgrid.com)
3. Перейти в раздел «Dashboard»
4. Выбрать вкладку в левой части экрана «Email API» и в выдвинувшемся меня выбрать «Integration Guide»
5. Далее выбрать «Web API». 
6. Выбрать Python
7. Создать API KEY
8. Подтвердить подключение.

#### Получение доступа к отправке писем
![Шаг 1](https://github.com/inmovery/ComplexParser/blob/master/images/8.png?raw=true)

#### Получение API_KEY
![Шаг 2](https://github.com/inmovery/ComplexParser/blob/master/images/9.png?raw=true)

#### Результат генерации API_KEY на основе его названия
![Шаг 3](https://github.com/inmovery/ComplexParser/blob/master/images/10.png?raw=true)

### Настройка Heroku

Для подклюения к heroku необходимо следовать следующему алгоритму:
1. Зарегистрироваться на сайте [Heroku.com](https://heroku.com)
2. Авторизоваться на сайте [Heroku.com](https://heroku.com)
3. Создать новое приложение, нажав на кнопку «New» в правом верхнем углу экрана
4. Перейти в раздел «Settings»
5. Перейти к разделу «Buildpacks» и добавить следующие зависимости:
```
    heroku/python
    https://github.com/heroku/heroku-buildpack-chromedriver
    https://github.com/heroku/heroku-buildpack-google-chrome
```
6. Перейти к разделу «Config Vars» и нажать на кнопку «Reveal Config Vars»
7. В поле `KEY` ввести `CHROMEDRIVER_PATH`, а в поле `VALUE` ввести `/app/.chromedriver/bin/chromedriver`, после чего нажать на кнопку «Add»
8.  В поле `KEY` ввести `GOOGLE_CHROME_BIN`, а в поле `VALUE` ввести `/app/.apt/usr/bin/google-chrome`, после чего нажмите на кнопку «Add».

![Инструкция](https://github.com/inmovery/ComplexParser/blob/master/images/7.png?raw=true)


### Установка значений
Установите константы `URL_PARSE`, `EMAIL`, `PASSWORD`, `SENDGRID_API_KEY`, `FROM_EMAIL`, `TO_EMAIL` в файле `settings.py` в соответствии с теми данными, которые вы полуили на этапе установки.

## Использование
Скачайте приложение:
1. Через командную строку, используя возможности GitHub: `git clone https://github.com/inmovery/ComplexParser.git`
2. Через скачивание [архива](https://github.com/inmovery/ComplexParser/archive/master.zip)
Данную программу можно запустить как через командную строку `python main.py`, так и в IDE PyCharm.

## Развёртывание

### Локальное развёртывание
Для того, чтобы использовать программу на своём компьюетере нужно:
1. Скачать [chromedriver (Google Chrome)](https://chromedriver.chromium.org/downloads) или [geckodriver (Firefox)](https://github.com/mozilla/geckodriver/releases)
  После скачивание переместить в папку с файлом `main.py`
2. Использовать следующий код в инициализации driver selenium (в начале кода):
    `driver = webdriver.Chrome()`

### Серверное развёртывание
Для того, чтобы развернуться на сервере используюся возможности Heroku. Чтобы подключить и использовать Google Chrom Driver используйте слеудющий код в инициализации driver selenium (в начале кода):
```
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
```

После настройки Heroku развёртывание приложения представляет из себя следующую последовательность команд, которая подразумевает использование Heroku CLI:
1. heroku login
2. git init
3. heroku get:remote -a complex-parser
4. git add .
5. git commit -m “initial commit”
6. pip3 freeze > requirements.txt
7. echo  > Procfile
8. Открыть файл Procfile и добавить в него «worker : python  main.py`
9. git push heroku master
10. heroku run python main.py
11. heroku scale worker=1
12. heroku logs --tail

## Вопросы

Смотрите и задавай вопросы в разделе [Issues](https://github.com/inmovery/ComplexParser/issues)
