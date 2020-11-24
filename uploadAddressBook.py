from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from statistics import mean
import time
import datetime
import logging
import userData

logging.basicConfig(filename='/Users/igorgerasimov/OneDrive/Python/CEAP/upload.log' ,
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%H:%M:%S'
                    )

uploadBook = '/Users/igorgerasimov/OneDrive/Python/files/vse10112020.csv'
nameGroup = 'test21'

logging.info('Start')
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 30)
# def startBrowser():
#     driver.get("https://mail.ru/")
driver.get("https://mail.ru/")
# Поле ввода логина 
countIteration = 0
avgSecond = [35]
for user in userData.users:

    lostTime = mean(avgSecond) * (len(userData.users) - countIteration) / 60 
    print(f'Итерация {countIteration} of {len(userData.users)} осталось {round(lostTime,1) } мин')
    
    login = user
    password = userData.users[user]
    start_time = datetime.datetime.now()


    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/form/div[3]/div[4]/button')))
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/form/div[3]/div[1]/div[2]/input').send_keys(login)
    except NameError:
        logging.error('Нет такого элемента')
        driver.quit()

    # Кнопка продолжить
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/form/div[3]/div[4]/button').click()
    time.sleep(2)
    # Поле ввода пароля 
    driver.find_element_by_id('mailbox:password-input').send_keys(password)
    time.sleep(1)
    # Кнопка продолжить 
    driver.find_element_by_id('mailbox:submit-button').click()
    time.sleep(5)

    # Адресная книга кнопка 
    try:
        
        wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/div[1]/div[1]/div/div[2]/span/div[1]/div/div/div/div[3]/div[2]/span/a/span')))
        driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/div/div[2]/span/div[1]/div/div/div/div[3]/div[2]/span/a/span').click()
    except:
        logging.error(f'Не удалось войти в почту для логина: {login} с паролем {password}')
        driver.quit()

    # Выделить все
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/button')))
    driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/button').click()

    # Удалить
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div[3]/div[3]/div/button')))
    driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div[3]/div[3]/div/button').click()

    # Подтвердить удаление 
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/div/form/div/div[2]/div[3]/button[1]')))
    driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/div/form/div/div[2]/div[3]/button[1]').click()

    # Выплывающий список 
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/button')))
    driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/button').click()

    # Импорт контактов 
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/a[2]/div')))
    driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/a[2]/div').click()

    # Загрузка книги 
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/div/form/div/div[2]/div[2]/div[5]/button')))
    driver.find_element_by_css_selector('input[type=file]').send_keys(uploadBook)

    # Название группы контактов
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/div/form/div/div[2]/div[2]/div[8]/div/input')))
    driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/div/form/div/div[2]/div[2]/div[8]/div/input').send_keys(nameGroup)

    # Продолжить 
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/div/form/div/div[2]/div[3]/button[1]')))
    driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/div/form/div/div[2]/div[3]/button[1]').click()

    # Крестик
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[3]')))
    driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[3]').click()

    # Выход 
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[1]/table/tbody/tr/td[2]/div[1]/table/tbody/tr/td[2]/a')))
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/table/tbody/tr/td[2]/div[1]/table/tbody/tr/td[2]/a').click()

    # Очистка поля ввода логина
    try:
        wait.until(EC.element_to_be_clickable((By.ID,'mailbox:login-input')))
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/form/div[3]/div[1]/div[2]/input').clear()
    except :
        logging.error('Нет такого элемента')
        driver.quit()

    workTime = datetime.datetime.now() - start_time
    avgSecond.append(workTime.seconds)
    countIteration += 1

    print(f'Для {login} добавили книгу за {workTime.seconds} c.')


time.sleep(5)
driver.quit()

