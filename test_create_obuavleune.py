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
from selenium.webdriver.chrome.options import  Options
import string
import allure

# Создание объявления

class create_obuavlenie(unittest.TestCase):


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
        opts = Options()  # чтобы тест выполнялся без интерфейса
        opts.headless = True  # чтобы тест выполнялся без интерфейса
        
        self.driver = webdriver.Chrome('/Users/rufina/.jenkins/workspace/realtors_master/chromedriver', options=opts)

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
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']"))).send_keys("password")

        time.sleep(2)

        # кнопка Вход
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='gl-btn mod-middle mod-fill mod-primary gl-full-width']"))).click()












    def test_create_obuavlenie(self):  # главный метод, надо чтобы он начинался  с test_

            driver = self.driver
            self.authorization(driver) # вызов метода авторизации
            time.sleep(2)




            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,  "//button[@class='gl-btn mod-primary mod-border']"))).click() # жмем  Разместить объявление
            time.sleep(4)

            sdam_or_prodam_index = randint(0,1)
            print("sdam_or_prodam_index is equal", sdam_or_prodam_index)

            # выбмрает Сдам в аренду или Продам
            WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@class='gl-btn mod-fill chips-btn mod-grey mod-hover']")))[sdam_or_prodam_index].click()
            time.sleep(2)

            k = randint(2, 11) # выбираем тип недвижимотси от 3 до 12 включительно



            print("k EQUAL is", k)

            WebDriverWait(driver, 10).until(
                        ec.presence_of_all_elements_located((By.XPATH, "//button[@class='gl-btn mod-fill chips-btn mod-grey mod-hover']")))[k-1].click()#тип Недвижимости

            # кнопка Далее
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='gl-btn mod-fill mod-primary submit-btn']"))).click()
            time.sleep(2)

            if (k == 6 or k == 9 or k == 10): # склад, производство, торговое помещение

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


            if (k == 7):  # Гараж

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


            if(k == 8 or k == 11): # жилой учатсок, коммер земля

                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@formcontrolname='totalAreaInSquareMeters']"))).send_keys(
                    randint(10, 50))  # Общая площадь

                time.sleep(1)

                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@formcontrolname='priceInRubles']"))).send_keys(
                    randint(290, 5050))  # Оющая стоимость



            if(k == 2 or k == 5):# Квартра, Офис

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



            if(k == 3): # дОм
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


            if(k == 4): #  Комната
                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@formcontrolname='totalAreaInSquareMeters']"))).send_keys(
                    randint(10, 50))  # Площадь

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

                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//input[@formcontrolname='priceInRubles']"))).send_keys(
                    randint(290, 5050))  # Оющая стоимость



            # кнопка Далее
            WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//button[@class='gl-btn mod-fill mod-primary submit-btn']"))).click()

            time.sleep(1)

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

            time.sleep(1)
            WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, "//button[@class='gl-btn mod-fill mod-primary submit-btn']"))).click() # кнпока Далее

            time.sleep(1)



             # фото набора
            file_dicitionary = {0: "/Users/rufina/Desktop/realtors_images/98_7u6 y5tr.jpeg",
                                1: "/Users/rufina/Desktop/realtors_images/Без названия.jpeg",
                                2: "/Users/rufina/Desktop/realtors_images/дом9.jpeg",
                                3: "/Users/rufina/Desktop/realtors_images/дом25.jpg",
                                4: "/Users/rufina/Desktop/realtors_images/не мое это и все .jpeg",
                                5: "/Users/rufina/Desktop/realtors_images/oiuyitrtr.jpeg",
                                6: "/Users/rufina/Desktop/realtors_images/oipuu.jpeg",
                                7: "/Users/rufina/Desktop/realtors_images/склад5.jpeg",
                                8: "/Users/rufina/Desktop/realtors_images/склад3.jpeg",
                                9: "/Users/rufina/Desktop/realtors_images/склад6.jpeg"

                        }



            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))[0].send_keys(
                file_dicitionary[randint(0, len(file_dicitionary) - 1)])

            time.sleep(2)

            for i in range(0, 6):  # грузим фото
                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))[i].send_keys(
                    file_dicitionary[randint(0, len(file_dicitionary) - 1)])
                time.sleep(1)

            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='gl-btn mod-fill mod-primary submit-btn']"))).click()  # кнпока Далее

            # Описание
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH,  "//textarea[@formcontrolname='description']"))).send_keys(self.my_metho_randem_stroka(randint(4,7),16))


            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='gl-btn mod-fill mod-primary submit-btn']"))).click()  # кнпока Далее


            time.sleep(1)

            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))[1].send_keys(
                file_dicitionary[randint(0, len(file_dicitionary) - 1)])

            time.sleep(2)

            for i in range(0, 4):  # грузим фото опционально
                WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))[i].send_keys(
                    file_dicitionary[randint(0, len(file_dicitionary) - 1)])
                time.sleep(1)

            time.sleep(1)



            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='gl-btn mod-fill mod-primary submit-btn']"))).click()  # кнпока Отправить на модерацию

            time.sleep(1)







    def tear_down(self):
        time.sleep(5)

        #self.driver.close()
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()
