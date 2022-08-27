from time import sleep
from os import system , name
from ctypes import windll

def slowType(msg, nl=None):
    for char in msg:
        print(char, end="", flush=True)
        if char is not " ":
            sleep(.08)
    if nl is not None:
        print()

def clear():
    system("cls" if name == "nt" else "clear")

def setConsoleName(Title):
    windll.kernel32.SetConsoleTitleW(Title)
