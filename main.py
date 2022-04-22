import pyautogui
from PIL import Image

# Converter Imagem para RGB.
Image.open('popup.png').convert('RGB').save('popup.png')

while True:

    try:
        position = pyautogui.locateCenterOnScreen('popup.png')
        if position is None:
            pass
        else:
            print(position)
            pyautogui.moveTo(position)
            pyautogui.click(position)
    except():
        continue