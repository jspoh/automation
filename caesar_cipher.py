# caesar cipher
# just for fun

import pyperclip

alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'


class Encryption(object):
    def __init__(self):
        self.msg = ""
        self.shift = 0

    def contin(self):
        cont = input("Would you like to continue? (y/n)\n").lower()
        if cont == "y":
            self.start()
        elif cont == "n":
            print("Goodbye!")
        else:
            print("Input 'y' or 'n' only!")

    def start(self):
        self.msg = input("Message: ")
        self.shift = 0
        self.shiftf()

    def shiftf(self):
        try:
            self.shift = int(input("Shift: "))
            if self.shift > 25:
                print("Shift value cannot be higher than 25!")
                self.shiftf()
            else:
                self.edc()
        except ValueError:
            print("Shift value must be a valid integer!")
            self.shiftf()

    def edc(self):
        ed = input("Encrypt or decrypt? (e/d)\n").lower()

        result = ""

        if ed == 'e':
            for i in self.msg:
                if i in alphabet:
                    result += alphabet[alphabet.find(i) + self.shift]
                else:
                    result += i
        elif ed == 'd':
            for i in self.msg:
                if i in alphabet:
                    result += alphabet[alphabet.find(i) - self.shift]
                else:
                    result += i
        else:
            print("Input 'e' or 'd' only!")
            self.edc()
        print(result)
        pyperclip.copy(result)
        self.contin()


en = Encryption()
en.start()
