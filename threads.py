""" 
    Has two threads
    One thread takes a global string and checks if it is in upper case
    If the string is in uppercase it prints that it is in uppercase and exits.
    If the string is not in uppercase, it converts it to uppercase and prints
    the string on the screen.

    The second thread does the same but for lowercase.

    Both threads run infinitely.

    Run this program many times and compare how each of the times run
"""
from time import sleep
from threading import Thread

class CapitalLetters(Thread):
    """ The capital letters thread """
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True #daemon runs the program continuously
        self.start()

    def run(self):
        
        global string # use the global string defined in the main function
        while True:
            if string.isupper(): 
                print ("\nThe string is already in UPPERCASE")
            else:
                string = string.upper()
                print (f"\nConverting to uppercase :: {string}")

            print ('\n---Exiting uppercase thread---\n')
            sleep(2)

class SmallLetters(Thread):
    """ The small letters thread """
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        global string
        while True:
            if string.islower(): 
                print ("\nThe string is already in lowercase")
            else:
                string = string.lower()
                print (f"\nConverting to lowercase :: {string}")
                    
            print ('\n---Exiting lowercase thread---\n')
            sleep(2)


if __name__ == "__main__":
    # "\x1b[1;33m  just changes the color of the output
    print ("\x1b[1;33m To stop, press Ctrl+C\n")
    string = "i love python"
    CapitalLetters()
    SmallLetters()
    while True:
        pass
