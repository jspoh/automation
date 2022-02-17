# auto typing bot. can help with filling up forms that require eg. email addresses etc

import keyboard

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
        print("Enter the text you desire to autotype, press [Escape] when you're done.\n")
        auto_text_v2 = keyboard.record(until="esc")
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


    def intro_text():
        func = input('''
Which function would you like to use?
        
1. AutoTyper
2. AutoTyper v2

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


    intro_text()

