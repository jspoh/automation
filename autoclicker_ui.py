# autoclicker with pyautogui instead of mouse
# made a gui for this but some hotkey stuff is broken now :/
# everything else seems to work fine though, can't really test stop button though
# program crashes when it starts clicking on the window

import keyboard
import pyautogui
import time
import PySimpleGUI as sg

sg.theme("DarkAmber")

layout_size = (40, 1)

font = "Arial"
font_size = 12

layout = [
    [sg.Text("Autoclicker by JS", size=(20, 1), font=(font, 20))],
    [sg.Text("")],
    [sg.Text("Select your desired speed mode below", size=layout_size, font=(font, font_size))],
    [sg.Radio("Slow", group_id="speed", key="slow", default=False, enable_events=True),
     sg.Radio("Fast", group_id="speed", key="fast", default=True, enable_events=True),
     sg.Radio("Faster", group_id="speed", key="faster", default=False, enable_events=True),
     sg.Radio("Fastest", group_id="speed", key="fastest", default=False, enable_events=True)],
    [sg.Text("")],
    [sg.Button("Start(F8)", key="start"), sg.Button("Stop(F8)", key="stop")],
    [sg.Text("Note: Start hotkey will only work when this window is selected!", font=("Arial", 7))]
]

window = sg.Window("Autoclicker by JS", layout, return_keyboard_events=True)

pyautogui.PAUSE = 0.0001

hotkey = "F8:119"
k_hotkey = "F8"
q_hotkey = "F7:118"


def click0():
    pyautogui.click(button='left', interval=0.5)


def click1():
    pyautogui.click(button='left')


def click2():
    pyautogui.doubleClick(button='left')


def click3():
    pyautogui.tripleClick(button='left')


def stop_click():
    print("autoclick stopped!")
    sg.popup("Autoclick stopped!")
    time.sleep(0.5)


running = True

while running:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        running = False
    elif keyboard.is_pressed(k_hotkey) or event == hotkey or event == "start":
        time.sleep(0.5)
        print("autoclick started!")
        while values["slow"]:
            click0()
            if keyboard.is_pressed(k_hotkey) or event == "stop":
                stop_click()
                break
        while values["fast"]:
            click1()
            if keyboard.is_pressed(k_hotkey) or event == "stop":
                stop_click()
                break
        while values["faster"]:
            click2()
            if keyboard.is_pressed(k_hotkey) or event == "stop":
                stop_click()
                break
        while values["fastest"]:
            click3()
            if keyboard.is_pressed(k_hotkey) or event == "stop":
                stop_click()
                break
