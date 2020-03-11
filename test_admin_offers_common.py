# -*- coding: utf-8 -*-
import time
import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # ожидания различных событий
from selenium.webdriver.support.ui import Select  # работа со списками
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import \
    ActionChains  # для сколинга к нужному элементу импортируем класс ActionChains
from random import randint
from selenium.webdriver.chrome.options import Options

import string


import  allure

# админка, список объявлений

class Admin_offers(unittest.TestCase):

    def my_metho_with_predlojenie(self, kolvo_bukv_v_slove, count_slov, count_predlojeniy):

        list_predloj = []

        for k in range(count_predlojeniy):  # цикл по колву предло;ений
            list_slov = []
            # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

            for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

                list_bukv = []
                for j in range(kolvo_bukv_v_slove):  # цикл по буквам в i-ом слове

                    list_bukv.append(' '.join([self.list_characters[randint(0, len(self.list_characters) - 1)]]))

                list_slov.append(''.join(list_bukv))

            list_predloj.append(' '.join(list_slov) + '.')

        return str(' '.join(list_predloj))


    def my_metho_randem_stroka(self, kolvo_bukv_v_slove, count_slov):  # генерит предложение

        list_slov = []
        # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

        for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

            list_bukv = []
            for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                list_bukv.append(' '.join([self.list_characters[randint(0, len(self.list_characters) - 1)]]))

            list_slov.append(''.join(list_bukv))

        return str(' '.join(list_slov))


    def generation_tel_phone(self):  # генерит номер телфона

        list_digits = []
        for i in range(0, 11):
            if i != 0:
                # print(string.digits[randint(0,9)]) # 0123456789
                list_digits.append(string.digits[randint(1, 9)])

        # print(list_digits)

        return str(str(8) + ''.join(list_digits))


    def my_metho_randem_stroka_for_email(self, kolvo_bukv_v_slove, count_slov):

        list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'W', 'X', 'Y', 'Z',
                           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'w', 'x', 'y', 'z',
                           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_',
                           '.']  # добавить символы !,  ? , *, %, #, $, ~

        list_slov = []
        # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

        for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

            list_slov = []
            # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

            for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

                list_bukv = []
                for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                    list_bukv.append(' '.join([list_characters[randint(0, len(list_characters) - 1)]]))

                list_slov.append(''.join(list_bukv))

        for_email = {0: "@yandex.ru", 1: "@mail.ru", 2: "@gmail.com",
                     3: "@yahoo.com", 4: "@felisadipiscing.edu", 5: "@aarcu.net", 6: "@sempereratin.edu",
                     7: "@estMauriseu.net", 8: "@pharetra.co.uk", 9: "@ut.ca", 10: "@felisDonectempor.org"}

        return str(' '.join(list_slov)) + for_email[randint(0, len(for_email) - 1)]


    def setUp(self):

        opts = Options()  # чтобы тест выполнялся без интерфейса
        opts.headless = True  # чтобы тест выполнялся без интерфейса

        self.driver = webdriver.Chrome('/Users/rufina/.jenkins/workspace/realtors_master/chromedriver', options=opts)

        # self.driver.set_window_position(0, 0)  # устанавливает позицию левого верзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна

        # self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()

        self.list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                'R', 'S',
                                'T', 'U', 'W', 'X', 'Y', 'Z',
                                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q',
                                'r', 's',
                                't', 'u', 'w', 'x', 'y', 'z', 'A'
                                                              ' ']  # поле

    @allure.step("authotization admin")
    def authorization(self, driver):

        driver.get("https://admin.realtor.technaxis.com/external/login")



        time.sleep(2)  # чтобы сразу окно не закрывалось
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='login']"))).send_keys(
            "admin@mail.ru")  #

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']"))).send_keys("password")

        time.sleep(2)

        # кнопка Вход
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//button[@type='button']")))[1].click()


    def test_offers(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода авторизации
        time.sleep(2)

        # кликаем на калденарь От
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='От']"))).click()

        time.sleep(2)

        # жме мна стрелочку предыдущего месяца
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Previous month']"))).click()
        time.sleep(2)

        list_of_dates_from = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//td[@class='mat-calendar-body-cell ng-star-inserted']")))

        list_of_dates_from[randint(0, len(list_of_dates_from) - 1)].click()  # кликает рандомную дату
        time.sleep(2)

        # кликаем на калденарь До
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='До']"))).click()

        time.sleep(2)

        list_of_dates_to = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//td[@class='mat-calendar-body-cell ng-star-inserted']")))

        time.sleep(2)

        list_of_dates_to[randint(0, len(list_of_dates_to) - 1)].click()
        time.sleep(2)


        # кликаем на Тип недвижимости
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//mat-select[@role='listbox']")))[0].click()

        time.sleep(2)

        list_of_nedvishimocts = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@role='option']")))

        time.sleep(2)
        list_of_nedvishimocts[randint(0, len(list_of_nedvishimocts)-1)].click() # кликаем ранломнй пункт из списка

        time.sleep(3)

        # кликаем на Тип объявления
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//mat-select[@role='listbox']")))[1].click()

        time.sleep(2)

        list_of_type_offers = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@role='option']")))

        list_of_type_offers[randint(0, 2)].click()

        time.sleep(2)

        # кликаем на Статус объявления
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//mat-select[@role='listbox']")))[3].click()

        time.sleep(2)

        list_of_type_paid = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@role='option']")))

        time.sleep(2)
        list_of_type_paid[randint(0, 2)].click()

        time.sleep(2)




        # перезагружаем станицу:
        self.driver.refresh()  # перезугружаем страницу

        time.sleep(5)



        for i in range(0, 5):

            search_field = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Поиск по ID, адресу']")))

            time.sleep(2)

            list_of_address_offers = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//mat-cell[@class='mat-cell cdk-column-address mat-column-address ng-star-inserted']")))

            search_field.send_keys(list_of_address_offers[randint(0, len(list_of_address_offers)-1)].text)

            time.sleep(2)

            search_field.clear()
            self.driver.refresh()  # перезугружаем страницу

            time.sleep(3)

        # поиск по id
        for i in range(0, 5):
            search_field = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Поиск по ID, адресу']")))

            time.sleep(2)

            list_of_id_offers = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located(
                    (By.XPATH, "//mat-cell[@class='mat-cell cdk-column-id mat-column-id ng-star-inserted']")))

            search_field.send_keys(list_of_id_offers[randint(0, len(list_of_id_offers) - 1)].text)

            time.sleep(2)

            search_field.clear()
            self.driver.refresh()  # перезугружаем страницу

            time.sleep(3)







    def tear_down(self):
        time.sleep(5)

        # self.driver.close()
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()

