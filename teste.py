import pyautogui as py
import time
# abrir o brave;
#Fazer refresh da página de 5sec em 5sec.
#repetir passo anterior de 1.5horas em 1.5horas;
#Caso o popup apareca, para este ciclo e fica novamente à espera que passe 1.5horas;
while True:
    py.press("win")
    time.sleep(0.2)
    py.write('Brave')
    time.sleep(0.2)
    py.press('Enter')
    time.sleep(1)
    for x in range(0, 20):
        py.press('f5')
        time.sleep(1)
    py.keyDown('alt')
    py.press('f4')
    py.keyUp('alt')
    break