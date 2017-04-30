from PIL import Image
from pytesser import *
import timeit
import PIL.ImageOps
import pyautogui
import time
import re
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
i = 0

while (i < 100):
    #print currentMouseX
    #print currentMouseY
    #time.sleep(0.1)
    im0 = PIL.ImageGrab.grab()
    im = im0.crop((945,570,1020,600))
    nom = "screen.png"
    im.save(nom)
    #im = Image.open(image_file)
    text = image_to_string(im)
    text = image_file_to_string(nom)
    text = image_file_to_string(nom, graceful_errors=True)

    #print "=====output11=======\n"
    #print text
    res = re.findall("\d+",text)
    #print res[0]
    i = i + 1
    if len(res) > 0 and int(res[0]) > 11:
        print "found it"
        break
    pyautogui.moveTo(935,212)
    pyautogui.click()

    if i == 100:
        print "FAL TO REACH 11+, unlucky",i