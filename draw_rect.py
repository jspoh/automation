# in case you ever want to draw a proper rectangle/square

import pyautogui
import keyboard
import sys

drag_duration = 0
hotkey = 'F8'
q_program = 'F7'

width = int(input("Width of rectangle(in px): "))
height = int(input("Height of rectangle(in px): "))
if width == height:
    print(f"Your square dimensions are {width}x{height}")
elif not width == "" and not height == "":
    print(f"Your rectangle dimensions are {width}x{height}")
print(f"Press {hotkey} to start drawing or {q_program} to terminate program")

running = True
while running:
    if keyboard.is_pressed(hotkey):
        pyautogui.drag(width, 0, drag_duration, button='left')
        pyautogui.drag(0, height, drag_duration, button='left')
        pyautogui.drag(-width, 0, drag_duration, button='left')
        pyautogui.drag(0, -height, drag_duration, button='left')
    if keyboard.is_pressed(q_program):
        sys.exit()
