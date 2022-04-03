import pyautogui
from selenium.webdriver.common.by import By
from PySimpleGUI import PySimpleGUI as sg
import time
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from PySimpleGUI import PySimpleGUI as sg
import time
import pyautogui


Set_Alarm1 = input("Entre com o 1º horário  H:M:S:")


Actual_Time = time.strftime("%I:%M:%S")

while (Actual_Time != Set_Alarm1):
    Actual_Time = time.strftime("%I:%M:%S")

if (Actual_Time == Set_Alarm1):
    print("1º pesquisa")
    navegador = webdriver.Chrome(executable_path=r'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
    navegador.get("https://www.google.com")
    navegador.maximize_window()
    time.sleep(3)
    navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Dolar")
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(60)
    navegador.close()