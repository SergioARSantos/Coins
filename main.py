import pyautogui as py
from PIL import Image
import time

# Converter Imagem para RGB.
Image.open('popup.png').convert('RGB').save('popup.png')

#Procurar PopUp
def Catch_Popup():
    try:
        #Localiza imagem no ecrã.
        position = py.locateCenterOnScreen('popup.png')
        #Caso não encontre passa ao próximo comando.
        if position is None:
            pass
        #Caso encontre a imagem.
        else:
            print(position)
            py.moveTo(position)
            py.click(position)
            time.sleep(3)
            #Fecha o separador criado pelo Popup.
            py.keyDown('ctrl')
            py.press('w')
            py.keyUp('ctrl')
    except():
        pass

print("Searching....")
while True:
    count = 0
    #Efectua uma contagem(contagem de segundos).
    while count <= 3600:
        #Por cada segundo, efectua uma pesquisa do Popup
        Catch_Popup()
        time.sleep(1)
        count = count + 1
        #Quando chegar a 1 hora efectua uma abertura de browser e faz 25 refresh.
        if count == 3600:
            print(count)
            try:
                py.press("win")
                time.sleep(0.2)
                py.write('Brave')
                time.sleep(0.2)
                py.press('Enter')
                time.sleep(1)
                #Loop para efectuar o Refresh.
                for x in range(0, 25):
                    py.press('f5')
                    time.sleep(1)
                #Quando termina, efectua o fecho do browser e reinicia a contagem.
                py.keyDown('alt')
                py.press('f4')
                py.keyUp('alt')
            except():
                print("Estava a mexer no PC!")
