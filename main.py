import time
import datetime
import schedule
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from sendgrid import SendGridAPIClient
from sendgrid import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId)
from bs4 import BeautifulSoup
import pandas as pd
import requests
import base64
import os.path
import pytz
from settings import *

def main():

    dataframe = pd.DataFrame(columns=["Ссылка", "Дата", "Время", "Игрок 1", "Игрок 2", "Счёт", "Тотал раундов",
                                      "Исход Раунд 1", "Исход Раунд 2", "Исход Раунд 3", "Исход Раунд 4",
                                      "Исход Раунд 5", "Исход Раунд 6", "Исход Раунд 7", "Исход Раунд 8",
                                      "Исход Раунд 9",
                                      "T-F", "T-B", "T-R", "1x2 П1", "1x2 П2", "П1", "П2", "F", "B", "R",
                                      "Время Раунд 1", "Время Раунд 2", "Время Раунд 3", "Время Раунд 4",
                                      "Время Раунд 5", "Время Раунд 6", "Время Раунд 7", "Время Раунд 8",
                                      "Время Раунд 9",
                                      "М", "М_ov", "М_un", "С", "С_ov", "С_un", "Б", "Б_ov", "Б_un",
                                      "5.5", "6.5", "7.5", "8.5",
                                      "Б 5.5", "М 5.5", "Б 6.5", "М 6.5", "Б 7.5", "М 7.5", "Б 8.5", "М 8.5",
                                      "Фаталити Да", "Фаталити Нет",
                                      "Б 1-ИТ 1.5", "М 1-ИТ 1.5", "Б 1-ИТ 2.5", "М 1-ИТ 2.5", "Б 1-ИТ 3.5",
                                      "М 1-ИТ 3.5", "Б 2-ИТ 1.5", "М 2-ИТ 1.5", "Б 2-ИТ 2.5", "М 2-ИТ 2.5",
                                      "Б 2-ИТ 3.5", "М 2-ИТ 3.5",
                                      "Б F 0.5", "М F 0.5", "Б F 2.5", "М F 2.5", "Б F 4.5", "М F 4.5",
                                      "Б B 0.5", "М B 0.5", "Б B 2.5", "М B 2.5", "Б B 4.5", "М B 4.5",
                                      "Чистая победа Да", "Чистая победа 0.5 Б"])

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    driver.get(URL_PARSE)

    # Ожидаем загрузку страницы
    wait = WebDriverWait(driver, 10)

    # Нажимаем на "Войти"
    driver.find_element_by_class_name("login").click()

    # Вводим логин
    login = driver.find_element_by_css_selector("#auth-modal #email-input input[type='email']")
    login.send_keys(EMAIL)

    # Вводим пароль
    password = driver.find_element_by_css_selector("#auth-modal #password-input input[type='password']")
    password.send_keys(PASSWORD)
    driver.find_element_by_css_selector("#auth-modal button").click()

    # Ждём пока загрузится кнопка статистики
    wait.until(presence_of_element_located((By.LINK_TEXT, "Статистика")))

    # Переходим на страницу со статистикой
    driver.find_element_by_link_text("Статистика").click()

    # Переходим на страницу со статистикой про Мортал Комбат
    driver.find_element_by_xpath("//a[@href='https://freedom-stat.com/stats/mk']").click()

    i = 0 # Счётчик страниц
    while(True):
        try:
            time.sleep(7) # Ждём окончательной загрузки таблицы
            this_page = driver.find_element_by_css_selector("div.table-pagination a.active").text
            soup = BeautifulSoup(driver.page_source, "lxml")
            table = soup.find('table', attrs={'class': 'game-stats'})
            table_body = table.find('tbody')

            j = 0 # Счётчик пройденных строк
            for row in table_body.find_all("tr"):
                j += 1
                try:
                    links = row.find("td", attrs={"class":"hovered-live"}).find("div", attrs={"class":"actionStat"}).find("div", attrs={"class":"actionStatLinks"})
                except:
                    links = row.find("td", attrs={"class":"show"}).find("div", attrs={"class":"actionStat"}).find("div", attrs={"class":"actionStatLinks"})

                # Парсим и записываем значения
                link = links.find_all("a")[2]["href"]
                date_round = row.find("td", attrs={"class": "date_round"}).text
                time_round = row.find("td", attrs={"class": "time_round"}).text
                players = row.find_all("td", attrs={"class": "player"})
                player_1 = players[0].text
                player_2 = players[1].text
                score = row.find("td", attrs={"class": "score"}).text
                score_total = row.find("td", attrs={"class": "scoretotal"}).text
                rounds = row.find_all("td", attrs={"class": "fin fincolor"})
                round_1 = rounds[0].text
                round_2 = rounds[1].text
                round_3 = rounds[2].text
                round_4 = rounds[3].text
                round_5 = rounds[4].text
                round_6 = rounds[5].text
                round_7 = rounds[6].text
                round_8 = rounds[7].text
                round_9 = rounds[8].text

                totals = row.find_all("td", attrs={"class": "total"})
                T_F = totals[0].text
                T_B = totals[1].text
                T_R = totals[2].text

                final_coef_player_1x2 = row.find_all("td", attrs={"class": "finalcoefs_1x2 color1x2"})
                final_coef_player_1_1x2 = final_coef_player_1x2[0].text
                final_coef_player_2_1x2 = final_coef_player_1x2[1].text

                final_coefs = row.find_all("td", attrs={"class": "finalcoefs_p12 colorp12"})
                final_coef_player_1 = final_coefs[0].text
                final_coef_player_2 = final_coefs[1].text

                final_coefs_F_B_R = row.find_all("td", attrs={"class": "finalcoefs_fbr colorfbr"})
                final_coef_F = final_coefs_F_B_R[0].text
                final_coef_B = final_coefs_F_B_R[1].text
                final_coef_R = final_coefs_F_B_R[2].text

                times = row.find_all("td", attrs={"class": "time tmc"})
                time_round_1 = times[0].text
                time_round_2 = times[1].text
                time_round_3 = times[2].text
                time_round_4 = times[3].text
                time_round_5 = times[4].text
                time_round_6 = times[5].text
                time_round_7 = times[6].text
                time_round_8 = times[7].text
                time_round_9 = times[8].text

                # Борьба с некорректностью и неполнотой таблицы
                try:
                    M_items = row.find_all("td", attrs={"class": "time_m"})
                    M_init = M_items[0].text
                    M_ov = M_items[1].text
                    M_un = M_items[2].text

                    S_items = row.find_all("td", attrs={"class": "time_s"})

                    S = S_items[0].text
                    S_ov = S_items[1].text
                    S_un = S_items[2].text

                    B_items = row.find_all("td", attrs={"class": "time_b"})
                    B = B_items[0].text
                    B_ov = B_items[1].text
                    B_un = B_items[2].text

                    score_5_5 = row.find_all("td", attrs={"class": "score_55 sc55"})
                    score_5_5_B = score_5_5[0].text
                    score_5_5_M = score_5_5[1].text

                    score_6_5 = row.find_all("td", attrs={"class": "score_65 sc65"})
                    score_6_5_B = score_6_5[0].text
                    score_6_5_M = score_6_5[1].text

                    score_7_5 = row.find_all("td", attrs={"class": "score_75 sc75"})
                    score_7_5_B = score_7_5[0].text
                    score_7_5_M = score_7_5[1].text

                    score_8_5 = row.find_all("td", attrs={"class": "score_85 sc85"})
                    score_8_5_B = score_8_5[0].text
                    score_8_5_M = score_8_5[1].text

                    fatality = row.find_all("td", attrs={"class": "fat_yes_no colorfat"})
                    fatality_yes = fatality[0].text
                    fatality_no = fatality[1].text

                    IT_1_1_5 = row.find_all("td", attrs={"class": "it1_15 it1_15color"})
                    IT_1_1_5_B = IT_1_1_5[0].text
                    IT_1_1_5_M = IT_1_1_5[1].text

                    IT_1_2_5 = row.find_all("td", attrs={"class": "it1_25 it1_25color"})
                    IT_1_2_5_B = IT_1_2_5[0].text
                    IT_1_2_5_M = IT_1_2_5[1].text

                    IT_1_3_5 = row.find_all("td", attrs={"class": "it1_35 it1_35color"})
                    IT_1_3_5_B = IT_1_3_5[0].text
                    IT_1_3_5_M = IT_1_3_5[1].text

                    IT_2_1_5 = row.find_all("td", attrs={"class": "it2_15 it2_15color"})
                    IT_2_1_5_B = IT_2_1_5[0].text
                    IT_2_1_5_M = IT_2_1_5[1].text

                    IT_2_2_5 = row.find_all("td", attrs={"class": "it2_25 it2_25color"})
                    IT_2_2_5_B = IT_2_2_5[0].text
                    IT_2_2_5_M = IT_2_2_5[1].text

                    IT_2_3_5 = row.find_all("td", attrs={"class": "it2_35 it2_35color"})
                    IT_2_3_5_B = IT_2_3_5[0].text
                    IT_2_3_5_M = IT_2_3_5[1].text

                    F_0_5 = row.find_all("td", attrs={"class": "extra_fat_05 extra_fat_05color"})
                    F_0_5_B = F_0_5[0].text
                    F_0_5_M = F_0_5[1].text

                    F_2_5 = row.find_all("td", attrs={"class": "extra_fat_25 extra_fat_25color"})
                    F_2_5_B = F_2_5[0].text
                    F_2_5_M = F_2_5[1].text

                    F_4_5 = row.find_all("td", attrs={"class": "extra_fat_45 extra_fat_45color"})
                    F_4_5_B = F_4_5[0].text
                    F_4_5_M = F_4_5[1].text

                    B_0_5 = row.find_all("td", attrs={"class": "extra_br_05 extra_br_05color"})
                    B_0_5_B = B_0_5[0].text
                    B_0_5_M = B_0_5[1].text

                    B_2_5 = row.find_all("td", attrs={"class": "extra_br_25 extra_br_25color"})
                    B_2_5_B = B_2_5[0].text
                    B_2_5_M = B_2_5[1].text

                    B_4_5 = row.find_all("td", attrs={"class": "extra_br_45 extra_br_45color"})
                    B_4_5_B = B_4_5[0].text
                    B_4_5_M = B_4_5[1].text

                    clear_victory = row.find_all("td", attrs={"class": "extra_fw extra_fwcolor"})
                    clear_victory_yes = clear_victory[0].text
                    clear_victory_0_5_B = clear_victory[1].text
                except:
                    if (round_1 != "" or round_2 != "" or round_3 != "" or round_4 != "" or
                            round_5 != "" or round_6 != "" or round_7 != "" or round_8 != "" or round_9 != ""):
                        M_init = "-"
                        M_ov = "-"
                        M_un = "-"
                        S = "-"
                        S_ov = "-"
                        S_un = "-"
                        B = "-"
                        B_ov = "-"
                        B_un = "-"
                        score_5_5_B = "-"
                        score_5_5_M = "-"
                        score_6_5_B = "-"
                        score_6_5_M = "-"
                        score_7_5_B = "-"
                        score_7_5_M = "-"
                        score_8_5_B = "-"
                        score_8_5_M = "-"
                        fatality_yes = "-"
                        fatality_no = "-"
                        IT_1_1_5_B = "-"
                        IT_1_1_5_M = "-"
                        IT_1_2_5_B = "-"
                        IT_1_2_5_M = "-"
                        IT_1_3_5_B = "-"
                        IT_1_3_5_M = "-"
                        IT_2_1_5_B = "-"
                        IT_2_1_5_M = "-"
                        IT_2_2_5_B = "-"
                        IT_2_2_5_M = "-"
                        IT_2_3_5_B = "-"
                        IT_2_3_5_M = "-"
                        F_0_5_B = "-"
                        F_0_5_M = "-"
                        F_2_5_B = "-"
                        F_2_5_M = "-"
                        F_4_5_B = "-"
                        F_4_5_M = "-"
                        clear_victory_yes = "-"
                        clear_victory_0_5_B = "-"
                    else:
                        # Пустая строка
                        continue
                dataframe = dataframe.append(
                    {"Ссылка": link, "Дата": date_round, "Время": time_round, "Игрок 1": player_1, "Игрок 2": player_2,
                     "Счёт": score, "Тотал раундов": score_total,
                     "Исход Раунд 1": round_1, "Исход Раунд 2": round_2, "Исход Раунд 3": round_3,
                     "Исход Раунд 4": round_4, "Исход Раунд 5": round_5, "Исход Раунд 6": round_6,
                     "Исход Раунд 7": round_7, "Исход Раунд 8": round_8, "Исход Раунд 9": round_9,
                     "T-F": T_F, "T-B": T_B, "T-R": T_R, "1x2 П1": final_coef_player_1_1x2,
                     "1x2 П2": final_coef_player_2_1x2, "П1": final_coef_player_1, "П2": final_coef_player_2,
                     "F": final_coef_F, "B": final_coef_B, "R": final_coef_R,
                     "Время Раунд 1": time_round_1, "Время Раунд 2": time_round_2, "Время Раунд 3": time_round_3,
                     "Время Раунд 4": time_round_4, "Время Раунд 5": time_round_5, "Время Раунд 6": time_round_6,
                     "Время Раунд 7": time_round_7, "Время Раунд 8": time_round_8, "Время Раунд 9": time_round_9,
                     "М": M_init, "М_ov": M_ov, "М_un": M_un, "С": S, "С_ov": S_ov, "С_un": S_un, "Б": B, "Б_ov": B_ov,
                     "Б_un": B_un,
                     "Б 5.5": score_5_5_B, "М 5.5": score_5_5_M, "Б 6.5": score_6_5_B, "М 6.5": score_6_5_M,
                     "Б 7.5": score_7_5_B, "М 7.5": score_7_5_M, "Б 8.5": score_8_5_B, "М 8.5": score_8_5_M,
                     "Фаталити Да": fatality_yes, "Фаталити Нет": fatality_no,
                     "Б 1-ИТ 1.5": IT_1_1_5_B, "М 1-ИТ 1.5": IT_1_1_5_M, "Б 1-ИТ 2.5": IT_1_2_5_B,
                     "М 1-ИТ 2.5": IT_1_2_5_M, "Б 1-ИТ 3.5": IT_1_3_5_B, "М 1-ИТ 3.5": IT_1_3_5_M,
                     "Б 2-ИТ 1.5": IT_2_1_5_B, "М 2-ИТ 1.5": IT_2_1_5_M, "Б 2-ИТ 2.5": IT_2_2_5_B,
                     "М 2-ИТ 2.5": IT_2_2_5_M, "Б 2-ИТ 3.5": IT_2_3_5_B, "М 2-ИТ 3.5": IT_2_3_5_M,
                     "Б F 0.5": F_0_5_B, "М F 0.5": F_0_5_M, "Б F 2.5": F_2_5_B, "М F 2.5": F_2_5_M, "Б F 4.5": F_4_5_B,
                     "М F 4.5": F_4_5_M,
                     "Б B 0.5": B_0_5_B, "М B 0.5": B_0_5_M, "Б B 2.5": B_2_5_B, "М B 2.5": B_2_5_M, "Б B 4.5": B_4_5_B,
                     "М B 4.5": B_4_5_M,
                     "Чистая победа Да": clear_victory_yes, "Чистая победа 0.5 Б": clear_victory_0_5_B},
                    ignore_index=True)

            i += 1

            # Оповещение о том, что страница пройдена

            # Создаём CSV файл для отправки в качестве Attachment
            directory = os.path.dirname(os.path.realpath(__file__))
            filename = "data.csv"
            file_path = os.path.join(directory, 'csv_files/', filename)
            dataframe.to_csv(file_path, index=False)

            # Читаем сохранённый файл
            with open(file_path, 'rb') as f:
                data = f.read()
                f.close()

            pre_subj = str(i) + " pages are completed!"

            encoded = base64.b64encode(data).decode()
            message = Mail(
                from_email=FROM_EMAIL,
                to_emails=TO_EMAIL,
                subject=pre_subj,
                html_content='')

            attachment = Attachment()
            attachment.file_content = FileContent(encoded)
            attachment.file_type = FileType('text/csv')
            attachment.file_name = FileName('data_' + str(i) + '.csv')
            attachment.disposition = Disposition('attachment')
            attachment.content_id = ContentId('Example Content ID')
            message.attachment = attachment

            try:
                sg = SendGridAPIClient(SENDGRID_API_KEY)
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e)

            # Переходим на следующую страницу
            driver.find_elements_by_id("p-next")[0].click()
        except Exception as e:
            print(e)
            break

    driver.quit()


while(True):
    schedule.every(1).minutes.do(main)