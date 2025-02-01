import os

import time

import threading
import openpyxl
import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
link_schet=0
schet = 1
schet1 = 1
book = openpyxl.open("telegramm.xlsx")
list1 = book.active

def searh_po_slovo(driver, slovo, timeout):
    elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{slovo}')]")
    if elements:
        last_element = elements[-1]
        try:
            # Ждем, пока элемент станет кликабельным
            WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(last_element))
            driver.execute_script("arguments[0].click();", last_element)
        except Exception as e:
            print(f"Ошибка при клике на элемент: {e}")


def search_element_Xpath(driver, element, timeout):
    try:
        button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, element)))
        driver.execute_script("arguments[0].scrollIntoView();", button)
        driver.execute_script("arguments[0].click();", button)
    except TimeoutException:
        print("Ошибка: Время ожидания загрузки элемента истекло.")


def search_element_Ypath_and_vsravka_text(driver, element, timeout, text):
    try:
        button = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, element)))
        button.click()
        button.send_keys(text)
        button.send_keys(Keys.RETURN)
    except Exception as e:
        print(f"An error occurred: {e}")


def poisk_elementov_click111(driver, element, t):
    TIME_TO_LOOP = t
    start = time.time()
    schetchik = 0
    spisok_element = element
    print(spisok_element)
    while time.time() < start + TIME_TO_LOOP:
        try:
            for i in spisok_element:
                print(i)
                elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{i}')]")
                # last_element = element[-1]
                if elements:
                    for g in elements:
                        print(f"Элемент найден в {i}")
                        # WebDriverWait(driver, 0.1).until(EC.element_to_be_clickable(last_element))
                        # driver.execute_script("arguments[0].scrollIntoView();", elements)
                        driver.execute_script("arguments[0].click();", g)
                        # r.click()
                        # driver.execute_script("arguments[0].scrollIntoView();", elements)
                        # driver.execute_script("arguments[0].click();", elements)
                        time.sleep(2)
                        schetchik += 1
                        # spisok_element.remove(i)

                        # continue
                if len(spisok_element) == 0:
                    break
        except Exception as e:
            print(f"Жду: {e}")


def poisk_elementov_click(driver, element, t):
    TIME_TO_LOOP = t
    start = time.time()
    schetchik = 0
    spisok_element = element
    print(spisok_element)
    while time.time() < start + TIME_TO_LOOP:
        try:
            for i in spisok_element:
                #print(i)
                elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{i}')]")
                # last_element = element[-1]
                if elements:
                    for g in elements:
                        print(f"Элемент найден в {i}")
                        # WebDriverWait(driver, 0.1).until(EC.element_to_be_clickable(last_element))
                        driver.execute_script("arguments[0].scrollIntoView();", g)
                        driver.execute_script("arguments[0].click();", g)
                        # r.click()
                        # driver.execute_script("arguments[0].scrollIntoView();", elements)
                        # driver.execute_script("arguments[0].click();", elements)
                        time.sleep(2)
                        schetchik += 1
                        spisok_element.remove(i)

                        # continue
                if len(element) == 0:
                    break
        except Exception as e:
            print(f"Жду: {e}")


def searh_po_slovo(driver, slovo, timeout):
    elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{slovo}')]")
    if elements:
        last_element = elements[-1]
        try:
            # Ждем, пока элемент станет кликабельным
            WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(last_element))
            driver.execute_script("arguments[0].click();", last_element)
        except Exception as e:
            print(f"Ошибка при клике на элемент: {e}")
def send_msg(photo):
    token = "5976486278:AAHql7K0uYyIUu6wfbSwPvI6J4LUJf_2AjE"
    chat_id = "1979830722"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + photo
    results = requests.get(url_req)

def magnit_kupon(photo):
    chat_id = "1979830722"
    token = "5976486278:AAHql7K0uYyIUu6wfbSwPvI6J4LUJf_2AjE"
    #image = pyautogui.screenshot(r'kuponchik.jpg', region=(664, 46, 589, 941))
    files = {'photo': open(photo, 'rb')}
    url_req = requests.post('https://api.telegram.org/bot5976486278:AAHql7K0uYyIUu6wfbSwPvI6J4LUJf_2AjE/sendPhoto?chat_id=1979830722',files=files)

def regictracia(driver):
    global schet



    # Загружаем данные из Excel

    account = list(range(1, 100))
    accounts = [i for i in account if list1['D'][i].value]
    link_group = [str(list1['D'][schet].value) for schet in accounts]  # ,# reverse=True)
    #random.shuffle(link_group)
    account_11=list1['A'][schet].value

    link=link_group[link_schet]
    print(link)
    try:

        driver.get(link)
        spisok_game_element = ['СТАРТ']
        poisk_elementov_click(driver, spisok_game_element, 30)
        driver.save_screenshot(f"screenshot{account_11}.png")
        magnit_kupon(f"screenshot{account_11}.png")
        send_msg(f'{account_11},{link}')

        #находим подписаться и жмем
        spisok_game_element = ['ПОДПИСАТЬСЯ','SUBSCRIBE']
        print(spisok_game_element)
        poisk_elementov_click(driver, spisok_game_element, 5)
# Нажимаем кнопку "закрепленное сообщение"

        element = driver.find_element(By.CSS_SELECTOR, '.chat-pinlist > div:nth-child(1)')
        # src_value = element.get_attribute('class')
        text = element.text
        print(text)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(5)
#учавствовать в конкурсе
        join_button = driver.find_element(By.CLASS_NAME, "reply-markup-button-text")
        text = join_button.text
        print(text)
        spisok_game_element = [text]
        poisk_elementov_click(driver, spisok_game_element, 20)
# Нажимаем кнопку "запустить"
        spisok_game_element = ['Launch', 'Запустить']#
        print(spisok_game_element)
        poisk_elementov_click(driver, spisok_game_element, 20)
# # Нажимаем кнопку "запустить"
#         element = driver.find_element(By.CSS_SELECTOR, '.cb-lb > input:nth-child(1)')
#         # src_value = element.get_attribute('class')
#         text = element.text
#         print(text)
#         driver.execute_script("arguments[0].click();", element)

        time.sleep(40)
        driver.save_screenshot(f"screenshot{account_11}.png")
        magnit_kupon(f"screenshot{account_11}.png")
        send_msg(f'{account_11},{link}')




    except Exception as e:
        print(f"An error occurred: {e}")
        # schet -= 1


def upload_process(profile_path):
    try:
        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options
        from fake_useragent import UserAgent

        ua = UserAgent()
        random_user_agent = ua.random
        options = Options()

        # Опции для ускорения загрузки
        options.set_preference("permissions.default.image", 2)  # Отключение загрузки изображений
        #options.set_preference("javascript.enabled", False)  # Отключение JavaScript (если это возможно)
        options.set_preference("network.http.use-cache", True)  # Использовать кэш
        options.set_preference("general.useragent.override", random_user_agent)  # Устанавливаем случайный User-Agent
        options.set_preference("dom.webdriver.enabled", False)
        #options.add_argument("--headless")  # Запуск в безголовом режиме
        options.profile = profile_path

        driver = webdriver.Firefox(options=options)


        # driver.maximize_window()
        # time.sleep(20000)

        print('игра и взять ссылку')
        regictracia(driver)
        # time.sleep(5)



    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


while True:

    threads = []
    num_threads = 0 # Количество потоков, которые вы хотите запустить одновременно



    while schet <= 43:  # Предположим, у вас всего 100 аккаунтов
        a = list1['C'][schet].value  # тут адреса
        b = list1['B'][schet].value

        if a == None or b != None:
            print(schet, list1['C'][schet].value)
            account_1 = "pr" #list1['B'][schet].value

            # Создаем и запускаем поток
            t = threading.Thread(target=upload_process, args=(account_1,))
            threads.append(t)
            t.start()
            print(account_1, 'startanul')
            # Удаляем завершившиеся потоки и проверяем количество текущих потоков
            while len(threads) > num_threads:
                for t in threads:
                    if not t.is_alive():  # Если поток завершен
                        threads.remove(t)  # Удаляем его из списка текущих потоков
                        print(f'удалили поток {t}')
                    time.sleep(1)  # Подождите немного

            schet += 1
        else:
            schet += 1
    # Ждем завершения всех оставшихся потоков
    for t in threads:
        t.join()

    if schet == 44:  # Например, если reached 100 accounts
        # break
        schet = 1
        schet1 += 1
        link_schet+=1
        path_to_script = r"D:\тг по новому\тг_участие в акциях\пятерочка_с_приглашением друзей\test.py"
        os.system(f'python "{path_to_script}"')
    if len(link_group) >= link_schet:
        break
        path_to_script = r"D:\тг по новому\тг_участие в акциях\пятерочка_с_приглашением друзей\пятерочка.py"
        os.system(f'python "{path_to_script}"')

        shutdown_command = "shutdown /s /t 00"
        os.system(shutdown_command)
        path_to_script = r"D:\СЕЛЕНИУМ ФАЕР ФОКС\дирол викторина\дирол_викторина.py"
        os.system(f'python "{path_to_script}"')
        path_to_script = r"D:\СЕЛЕНИУМ ФАЕР ФОКС\вискас викторина.py"
        os.system(f'python "{path_to_script}"')

