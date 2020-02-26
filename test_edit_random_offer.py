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
from selenium.webdriver.common.action_chains import ActionChains # lля сколинга к нужному элементу импортируем класс ActionChains
from random import randint
import string
import  allure

# Редктирование рандомного  объявления

class edit_random_offer(unittest.TestCase):


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


    def my_metho_randem_stroka(self, kolvo_bukv_v_slove, count_slov): # генерит предложение

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
                           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_',  '.'] # добавить символы !,  ? , *, %, #, $, ~

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
                     3:"@yahoo.com", 4:"@felisadipiscing.edu", 5:"@aarcu.net", 6:"@sempereratin.edu", 7:"@estMauriseu.net", 8:"@pharetra.co.uk", 9:"@ut.ca", 10: "@felisDonectempor.org"}

        return str(' '.join(list_slov)) + for_email[randint(0, len(for_email)-1)]






    def setUp(self):
        self.driver = webdriver.Chrome('/Users/rufina/.jenkins/workspace/realtors_master/chromedriver')  # '/usr/local/bin/chromedriver'

        #self.driver.set_window_position(0, 0)  # устанавливает позицию левого верзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна


        #self.driver.maximize_window()
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

        driver.get("https://realtor.technaxis.com/")

        # кнпока Да в сплывашке
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='gl-btn mod-fill mod-primary gl-full-width confirm-btn']"))).click()

        # кнопка Войти
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//button[@class='gl-btn mod-primary mod-border']")))[0].click()

        time.sleep(2)  # чтобы сразу окно не закрывалось
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='login']"))).send_keys(
            "rufinka_91@mail.ru") #

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']"))).send_keys("password1")

        time.sleep(2)

        # кнопка Вход
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='gl-btn mod-middle mod-fill mod-primary gl-full-width']"))).click()












    def test_edit_obuavlenie(self):  # главный метод, надо чтобы он начинался  с test_

            driver = self.driver
            self.authorization(driver) # вызов метода авторизации
            time.sleep(2)

            # жмем на смайлик
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,  "//button[@class='gl-link gl-btn nav-item profile']"))).click()
            time.sleep(1)

            # пнкт Мои объявлеия  в иконке самайлика
            WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH,  "//a[@class='gl-options-list-item mod-small']")))[0].click() # //a[text()=' Мои объявления ']
            time.sleep(6)

            # Спсисок объявлений
            list_of_offers = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//a[@class='offer-item gl-offer-card-item-link']")))

            list_of_offers[randint(0, len(list_of_offers)-1)].click() # выбмаем рандомную картчоку  и кликаем на нее
            time.sleep(7)

            # жмем на кнопку Многоточие
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn-menu gl-icon-btn mod-primary mod-dots']"))).click()

            time.sleep(3)

            # Жме мна редаткирвоать в меню кнпоки многоточия
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@class='gl-options-list-item mod-small']"))).click()

            time.sleep(2)

            # спсиок типов недвижиомсти
            list_of_yupes_nedvoshomost = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='option-wrapper']")))

            k = randint(2, 11) ## до 11 включительно
            print("k equal", k)

            list_of_yupes_nedvoshomost[k].click()





            # кнопка Далее
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='gl-btn mod-fill mod-primary submit-btn']"))).click()
            time.sleep(2)

            if (k == 2 or k == 5 or k == 6): # склад, производство, торговое помещение

                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@formcontrolname='totalAreaInSquareMeters']"))).send_keys(randint(10,50)) # Общая площадь

                time.sleep(1)

                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@formcontrolname='ceilingHeightInMeters']"))).send_keys(
                    randint(10, 50))  # Высота потолков

                time.sleep(1)

                etage = randint(2, 7) # генерит этаж
                print("etage is equal", etage)

                WebDriverWait(driver, 10).until( # Этаж
                    ec.presence_of_all_elements_located(
                        (By.XPATH,  "//input[@type='number']")))[2].send_keys(etage)

                time.sleep(1)
                WebDriverWait(driver, 10).until(  # Этаж Из
                    ec.presence_of_all_elements_located(
                        (By.XPATH, "//input[@type='number']")))[3].send_keys(randint(etage+1, 10))

                time.sleep(1)
                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@formcontrolname='priceInRubles']"))).send_keys(randint(290, 5050))  # Оющая стоимость

                time.sleep(1)


            if (k == 3):  # Гараж

                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@formcontrolname='totalAreaInSquareMeters']"))).send_keys(
                    randint(10, 50))  # Общая площадь

                time.sleep(1)

                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@formcontrolname='ceilingHeightInMeters']"))).send_keys(
                    randint(10, 50))  # Высота потолков

                time.sleep(1)
                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@formcontrolname='priceInRubles']"))).send_keys(
                    randint(290, 5050))  # Оющая стоимость


            if(k == 4 or k == 7): # жилой учатсок, коммер земля

                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@formcontrolname='totalAreaInSquareMeters']"))).send_keys(
                    randint(10, 50))  # Общая площадь

                time.sleep(1)

                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@formcontrolname='priceInRubles']"))).send_keys(
                    randint(290, 5050))  # Оющая стоимость



            if(k == 10 or k == 8):# Квартра, Офис

                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located(
                        (By.XPATH, "//button[@class='gl-btn mod-fill option mod-trans mod-hover']")))[randint(0,3)].click()# колво комнат

                time.sleep(1)
                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@formcontrolname='totalAreaInSquareMeters']"))).send_keys(
                    randint(10, 50))  # Общая площадь

                time.sleep(1)

                etage = randint(2, 7)  # генерит этаж
                print("etage is equal", etage)

                WebDriverWait(driver, 10).until(  # Этаж
                    ec.presence_of_all_elements_located(
                        (By.XPATH, "//input[@type='number']")))[1].send_keys(etage)

                time.sleep(1)
                WebDriverWait(driver, 10).until(  # Этаж Из
                    ec.presence_of_all_elements_located(
                        (By.XPATH, "//input[@type='number']")))[2].send_keys(randint(etage + 1, 10))


                time.sleep(1)
                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@formcontrolname='priceInRubles']"))).send_keys(
                    randint(290, 5050))  # Оющая стоимость



            if(k == 11): # дОм
                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located(
                        (By.XPATH, "//button[@class='gl-btn mod-fill option mod-trans mod-hover']")))[
                    randint(0, 3)].click()  # колво комнат

                time.sleep(1)

                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@formcontrolname='totalAreaInSquareMeters']"))).send_keys(
                    randint(10, 50))  # Площадь

                time.sleep(1)

                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@formcontrolname='totalFloors']"))).send_keys(
                    randint(1, 5))  # колов этажей

                time.sleep(1)
                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@formcontrolname='priceInRubles']"))).send_keys(
                    randint(290, 5050))  # Оющая стоимость


            if(k == 9): #  Комната
                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@formcontrolname='totalAreaInSquareMeters']"))).send_keys(
                    randint(10, 50))  # Площадь

                time.sleep(2)

                etage = randint(2, 7)  # генерит этаж
                print("etage is equal", etage)

                WebDriverWait(driver, 10).until(  # Этаж
                    ec.presence_of_all_elements_located(
                        (By.XPATH, "//input[@type='number']")))[1].send_keys(etage)

                time.sleep(2)
                WebDriverWait(driver, 10).until(  # Этаж Из
                    ec.presence_of_all_elements_located(
                        (By.XPATH, "//input[@type='number']")))[2].send_keys(randint(etage + 1, 10))

                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@formcontrolname='priceInRubles']"))).send_keys(
                    randint(290, 5050))  # Оющая стоимость



            # кнопка Далее
            WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//button[@class='gl-btn mod-fill mod-primary submit-btn']"))).click()

            time.sleep(2)

            # Карта:
            address =  WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@placeholder='Введите местоположение']")))
            address.click()

            for i in range(0,3):

                address.send_keys(Keys.DOWN)

                time.sleep(1)

            address.send_keys(Keys.ENTER)
            #address.send_keys(Keys.BACK_SPACE)

            time.sleep(2)
            WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//button[@class='gl-btn mod-fill mod-primary submit-btn']"))).click() # кнпока Далее

            time.sleep(2)



            # фото набора
            file_dicitionary = {0: "/Users/rufina/Desktop/realtors_images/команата4.jpg",
                                1: "/Users/rufina/Desktop/realtors_images/дом7.jpeg",
                                2: "/Users/rufina/Desktop/realtors_images/дом25.jpg",
                                3: "/Users/rufina/Desktop/realtors_images/дом27.jpg",
                                4: "/Users/rufina/Desktop/realtors_images/команата4.jpg",
                                5: "/Users/rufina/Desktop/realtors_images/команата5.jpg",
                                6: "/Users/rufina/Desktop/realtors_images/команата6.jpg",
                                7: "/Users/rufina/Desktop/realtors_images/команата9.jpg",
                                8: "/Users/rufina/Desktop/realtors_images/команата10.jpg",
                                9: "/Users/rufina/Desktop/realtors_images/команата11.jpg",
                                10: "/Users/rufina/Desktop/realtors_images/команата7.jpg",
                                11: "/Users/rufina/Desktop/realtors_images/команата17.jpg",
                                12: "/Users/rufina/Desktop/realtors_images/офис1.jpeg",
                                13: "/Users/rufina/Desktop/realtors_images/офис6.jpeg",
                                14: "/Users/rufina/Desktop/realtors_images/офис8.jpg",
                                15: "/Users/rufina/Desktop/realtors_images/произвлдво2.jpeg",
                                16: "/Users/rufina/Desktop/realtors_images/произвлдво3.jpeg",
                                17: "/Users/rufina/Desktop/realtors_images/произвлдво4.jpeg",
                                18: "/Users/rufina/Desktop/realtors_images/произвлдво5.jpeg",
                                19: "/Users/rufina/Desktop/realtors_images/склад1.jpeg",
                                20: "/Users/rufina/Desktop/realtors_images/склад2.jpeg",
                                21: "/Users/rufina/Desktop/realtors_images/склад3.jpeg",
                                22: "/Users/rufina/Desktop/realtors_images/склад5.jpeg",
                                23: "/Users/rufina/Desktop/realtors_images/oiuyitrtr.jpeg",
                                24: "/Users/rufina/Desktop/realtors_images/zxcfvghbjn.jpeg",
                                25: "/Users/rufina/Desktop/realtors_images/"



                                 }


            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))[0].send_keys(
                file_dicitionary[randint(0, len(file_dicitionary) - 1)])

            time.sleep(2)

            for i in range(0, 3):  # грузим фото опционально
                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))[i].send_keys(
                    file_dicitionary[randint(0, len(file_dicitionary) - 1)])
                time.sleep(1)

            time.sleep(2)
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='gl-btn mod-fill mod-primary submit-btn']"))).click()  # кнпока Далее

            # Описание
            time.sleep(10)
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH,  "//textarea[@formcontrolname='description']"))).send_keys(self.my_metho_randem_stroka(randint(4,7),16))

            time.sleep(2)
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='gl-btn mod-fill mod-primary submit-btn']"))).click()  # кнпока Далее


            time.sleep(2)

            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))[1].send_keys(
                file_dicitionary[randint(0, len(file_dicitionary) - 1)])

            time.sleep(2)

            for i in range(0, 4):  # грузим фото опционально
                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))[i].send_keys(
                    file_dicitionary[randint(0, len(file_dicitionary) - 1)])
                time.sleep(1)

            time.sleep(2)



            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='gl-btn mod-fill mod-primary submit-btn']"))).click()  # кнпока Отправить на модерацию

            time.sleep(2)







    def tear_down(self):
        time.sleep(5)

        #self.driver.close()
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()
