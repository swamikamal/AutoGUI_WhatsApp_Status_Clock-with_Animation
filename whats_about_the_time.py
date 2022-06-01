#@author Kamal Swami
#@date 17-07-20
#libraries&modules requied to download
#selenium
#pyautogui
#tkinter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from tkinter import *
bot=webdriver.Firefox()

#add selenium plug in to your web browser
# add website link where you want to go
bot.get('https://web.whatsapp.com/')
time.sleep(6)
#set cordinates according to your screen size
#pyautogui.moveTo(x,y,{time to reach that point})

#actuall size is default of laptop screen and also default from firefox side no changing in size 
# for firefox and no any other screen

# x=-------------------------------->
#y=			            |
####################################|
####################################|
####################################|
####################################|
####################################|
####################################|
####################################|
####################################|
####################################|
####################################|
####################################\/
#set x and y acoording to your screen size
pyautogui.moveTo(73, 150, 2)
pyautogui.click()

def whatsup():
        mint=int(input("ENTER THE Minutes : "))
        mint=mint*60
        time.sleep(2)
        checker=0
        for i in range(mint+1):
                lft=mint-i
#set x and y acoording to your screen size
                pyautogui.moveTo(520, 850)
                pyautogui.click()
                time.sleep(0.1)
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('delete')
                checker=checker+1
                if checker==1:
                        symbl=" | "
                elif checker==2:
                        symbl=" / "
                elif checker==3:
                        symbl="--"
                elif checker==4:
                        symbl=" \\ "
                        checker=0
                a=time.time()
                b=time.ctime(a)
                b=str(b+symbl)
                
                
                pyautogui.typewrite(b)
                pyautogui.press('enter')
                print("Time Left To Over {in sec}:  ",lft)

while True:
        y=input("WANT TO CONTINUE Then Press Y : ")
        if y=="y":
                whatsup()
        else :print("SEE YOU Later")
        if y=="n":
                break










