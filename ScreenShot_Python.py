import pyautogui
import random

name=str(random.randint(10,1000))
pyautogui.screenshot("Screenshot"+name+".png",region=(100,100,100,100))