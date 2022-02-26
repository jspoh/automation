# auto typing + auto clicking bot. can help with filling up forms that require eg. email addresses etc

import keyboard
import mouse
import time

start_stop_key = keyboard.KEY_DOWN

running = True
while running:

    def auto_type():
        a_type = True
        auto_text = input("Enter the text you desire to auto-type:\n")
        print('''
Press [arrow down] to start typing
Press 'Q' to go back
''')
        while a_type:
            if keyboard.is_pressed(start_stop_key):
                keyboard.write(auto_text)
            elif keyboard.is_pressed("q"):
                a_type = False


    # auto typer that allows you to customize typing speed


    def auto_type_v2():

        a_type_v2 = True
        print('''
        
Auto Typer v2 will record all keystrokes at the speed and sequence you type it at, 
including pauses, mistakes etc.

''')
        print("Enter the text you desire to autotype, press [Enter] when you're done.\n")
        auto_text_v2 = keyboard.record(until="Enter")
        input()  # to prevent the program from going straight to input in the next line
        type_speed = input('''
How fast would you like the bot to type your text?
Enter '0' for instant, '1' for 1x, '2' for 2x etc..
''')
        while a_type_v2:
            if keyboard.is_pressed(start_stop_key):
                if type_speed in "1234567890":
                    keyboard.play(auto_text_v2, speed_factor=int(type_speed))
                else:
                    print("You may only enter integers into the speed multiplier!")
                    auto_type_v2()
            elif keyboard.is_pressed("q"):
                a_type_v2 = False


    def auto_click():
        print('''
Press [arrow down] to start/stop clicking the left mouse button.
This program does ~30 clicks per second
''')
        #cps = float(input("Clicks per second: "))
        autoclick = True
        while autoclick:
            if keyboard.is_pressed(start_stop_key):
                print("Auto click starting in 3 seconds")
                time.sleep(3)
                print("Auto click started!")
                aclick_running = True
                while aclick_running:
                    mouse.click("left")
                    time.sleep(0.02)  # ~30cps
                    if keyboard.is_pressed(start_stop_key):
                        print("Autoclick stopped!")
                        aclick_running = False
                        time.sleep(0.5)



    def test():
        while True:
            if keyboard.is_pressed(start_stop_key):
                print("lol")
                time.sleep(0.5)



    def intro_text():
        func = input('''
Which function would you like to use?
        
1. AutoTyper
2. AutoTyper v2
3. Auto clicker

Hotkey to start/stop is [arrow down]
Alternatively, enter 'Q' to quit program.
        
''').lower()

        if func == "q":
            global running
            running = False
        elif func == "1":
            auto_type()
        elif func == "2":
            auto_type_v2()
        elif func == "3":
            auto_click()
        elif func == "0":
            test()


    intro_text()
