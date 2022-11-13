import pyautogui as pg
import time

time.sleep(10)

a = "ini adalah spaming bot"

for i in a:
    pg.write(a)
    pg.press('Enter')