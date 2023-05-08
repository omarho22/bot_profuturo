#pyautogui.displayMousePosition()
#https://www.youtube.com/watch?v=W2LCF3YYpIY /como crear entorno virtual
import pyautogui as robot
import time

pag_web = "http://www.consar.gob.mx/gobmx/aplicativo/siset/Series.aspx?cd=60&cdAlt=False"

abrir_google = 47,388
buscar_web = 265,54
click_formato = 237,593
click_csv = 215,643
click_detalle = 418,596
click_afore = 404,628
click_RCV_IMSS=213,525
click_RCV_ISSSTE=212,542
click_solidario=192,631
click_voluntario=192,650
click_exportar = 810,348

#función para mover mouse y dar click
def abrir(pos,click=1):
    robot.moveTo(pos)
    robot.click(clicks=click)

#abrir chrome 
abrir(abrir_google,click=2)
#maximizar la pestaña de google
time.sleep(2)
robot.hotkey("alt","space")
time.sleep(0.5)
robot.typewrite("x")

#seleccionar donde poner la url
time.sleep(4)
abrir(buscar_web)
robot.typewrite(pag_web)
time.sleep(5)
robot.hotkey("enter")
time.sleep(2)

#seleccionar formato
abrir(click_formato)
time.sleep(1.5)
abrir(click_csv)
time.sleep(1.5)

#seleccionar detalle
abrir(click_detalle)
time.sleep(1.5)
abrir(click_afore)
time.sleep(1.5)

#scroll hacia abajo
for i in range(1):
    robot.scroll(-300)
    time.sleep(0.5)

#seleccionar opciones
abrir(click_RCV_IMSS)
time.sleep(0.5)
robot.hotkey("enter")
time.sleep(0.5)
abrir(click_RCV_ISSSTE)
time.sleep(0.5)
robot.hotkey("enter")
abrir(click_voluntario)
time.sleep(0.5)
robot.hotkey("enter")
abrir(click_solidario)
time.sleep(0.5)
robot.hotkey("enter")
time.sleep(1)

#exportar
abrir(click_exportar)
time.sleep(0.5)
robot.hotkey("enter")
time.sleep(0.5)