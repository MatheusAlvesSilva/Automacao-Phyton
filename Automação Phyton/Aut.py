import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
centrocustos = ['*****']
cnpj = ['*****']

pyautogui.PAUSE = 1

navegador = webdriver.Chrome()

navegador.get('*****')

navegador.maximize_window()

navegador.find_element_by_xpath('//*[@id="logon"]').send_keys('****')

navegador.find_element_by_xpath('//*[@id="senha"]').send_keys('*****')

navegador.find_element_by_xpath('//*[@id="invisible"]').click()

pyautogui.sleep(20)

navegador.find_element_by_xpath('//*[@id="myModalValoresVisao"]/div/div/div[2]/button').click()

navegador.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/div/div[12]/span[1]/a').click()

navegador.find_element_by_xpath('//*[@id="buscarMenuTxt"]').send_keys('Cadastro de Clientes e Fornecedores')

navegador.find_element_by_xpath('//*[@id="searchMenus"]/div[1]/a').click()

navegador.find_element_by_xpath('//*[@id="CNPJ"]').send_keys(cnpj)

pyautogui.sleep(2)

pyautogui.write(cnpjs)

for cnpjs in cnpj:
    pyautogui.sleep(2)
    pyperclip.copy((cnpj[0]))
    pyautogui.sleep(7)
    pyautogui.write(cnpjs)
    pyautogui.sleep(2)
    pyautogui.click(x=287, y=289)
    pyautogui.sleep(2)
    pyautogui.click(x=137, y=226)
    pyautogui.sleep(2)
    pyautogui.click(x=32, y=525)
for cc in centrocustos:
    pyautogui.sleep(2)
    pyautogui.write(cc)
    pyautogui.sleep(2)
    pyautogui.click(x=1313, y=704)
    pyautogui.sleep(2)
    pyautogui.click(x=1195, y=121)
    pyautogui.sleep(2)
    pyautogui.click(x=1184, y=232)
    pyautogui.sleep(2)
