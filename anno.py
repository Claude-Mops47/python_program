import random

import pyautogui as pg

import time

animal =("monkey","donkey", "dog")

time.sleep(8)

for i in range(23):
    a = random.choice(animal)
    pg.write("you are a" + a)
    pg.press('enter')
    pg.click('mop')