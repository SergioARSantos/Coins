import pyautogui as py
from PIL import Image
import time

# Converter Imagem para RGB.
Image.open('popup.png').convert('RGB').save('popup.png')

#Procurar PopUp
def Catch_Popup():
    try:
        position = py.locateCenterOnScreen('popup.png')
        if position is None:
            pass
        else:
            print(position)
            py.moveTo(position)
            py.click(position)
            time.sleep(3)
            py.keyDown('ctrl')
            py.press('w')
            py.keyUp('ctrl')
    except():
        pass

print("Searching....")
while True:
    count = 0
    while count <= 3600:
        Catch_Popup()
        time.sleep(1)
        count = count + 1
        if count == 3600:
            print(count)
            try:
                py.press("win")
                time.sleep(0.2)
                py.write('Brave')
                time.sleep(0.2)
                py.press('Enter')
                time.sleep(1)
                for x in range(0, 25):
                    py.press('f5')
                    time.sleep(1)
                py.keyDown('alt')
                py.press('f4')
                py.keyUp('alt')
            except():
                print("Estava a mexer no PC!")
