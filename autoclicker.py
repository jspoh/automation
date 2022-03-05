# autoclicker with pyautogui instead of mouse
# ~64 cps

import sys

import keyboard
import pyautogui
import time

pyautogui.PAUSE = 0.0001

start_stop_key = "f8"

print("Initializing program..")
print('''
_________________________________
|Start/stop key              F8  |
|CPS                         64  |
|--------------------------------|
|Quit                        F7  |
|________________________________|           
''')

running = True
while running:
    if keyboard.is_pressed(start_stop_key):
        time.sleep(0.5)
        print("autoclick started!")
        mouse_click = True
        while mouse_click:
            pyautogui.click(button='left')  # feel free to change this to doubleClick/tripleClick if your application can handle it
            if keyboard.is_pressed(start_stop_key):
                mouse_click = False
                print("autoclick stopped!")
                time.sleep(0.5)
    elif keyboard.is_pressed("f7"):
        sys.exit()
