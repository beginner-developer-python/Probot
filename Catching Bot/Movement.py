import win32com.client
import pyautogui
import time
import win32api
import win32con
from pynput import mouse
from tkinter import *
import keyboard
import json
from colorama import Fore

NumberOfMouseClicks = 0


class MyException(Exception):
    pass

listener = ""
xA = ""
yA = ""
tk = ''
click = 0
Positions = []
def _on_click(x, y, button, pressed):
    if pressed:
        global xA, yA
        xA = x
        yA = y
        listener.stop()


def lossfocus(event):
    for i in range(150):
        keyboard.block_key(i)
    # label.config(text="Click where Run button is there")
    run_pos = mouse_pos("\nClick where run button is there: ")
    print(Fore.GREEN+run_pos)
    attk_pos = mouse_pos("Click where attack button is there: ")
    # label.config(text="Click where Attack button is there")
    print(Fore.GREEN+attk_pos)
    falseswipe_pos = mouse_pos("Click where FalseSwipe Attk button is there: ")
    # label.config(text="Click where FalseSwipe Attack button is there")
    print(Fore.GREEN+falseswipe_pos)
    bag_pos = mouse_pos("Click where bag button is there:")
    # label.config(text="Click where Bag button is there")
    print(Fore.GREEN+bag_pos)
    pokeball_pos = mouse_pos("Click where pokeball button is there: ")
    # label.config(text="Click where pokeball button is there Pokeballs should be more then 70")
    print(Fore.GREEN+pokeball_pos)
    pokemon_location = mouse_pos("Click where Change pokemon button is there: ")
    # label.config(text="Click where Change Pokemon button is there")
    print(Fore.GREEN+pokemon_location)
    falseswipePoke_pos = mouse_pos("Click where Falseswipe_Pokemon is there: ")
    # label.config(text="Click where Falseswipe_Pokemon is there")
    print(Fore.GREEN+falseswipePoke_pos)
    tk.destroy()
    global Positions
    Positions = run_pos, attk_pos, falseswipe_pos, bag_pos, pokeball_pos, pokemon_location, falseswipe_pos
    for i in range(150):
        keyboard.unblock_key(i)


def mouse_pos(print_s):
    print(Fore.GREEN+print_s)
    global listener
    with mouse.Listener(on_click=_on_click) as listener:
        try:
            listener.join()
        except MyException as e:
            print(Fore.RED+e)
    return xA, yA


shell = win32com.client.Dispatch("WScript.Shell")

def focus_window(Windown_Name):
    shell.AppActivate(Windown_Name)

def press_key(Windown_Name, key):
    shell.AppActivate(Windown_Name)
    shell.SendKeys(key, 0)
    time.sleep(0.06)


def locate_image(Image):
    start = pyautogui.locateCenterOnScreen(Image, region=(
        0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    if start is not None:
        pyautogui.moveTo(start)
    else:
        print(Fore.RED+"Image not detected")


def detect_image(Image):
    start = pyautogui.locateCenterOnScreen(Image, region=(
        0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    return start


def click_Left():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.1)


def click_Right():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
    time.sleep(0.1)


def blockScreen():
    global Positions
    As = int(input("Press 1 to Use Saved Locations or Press 2 to Choose Locations: "))
    if As == 1:
        with open('Locations.txt') as f:
            for line in f:
                a = line.strip()
                Positions.append(a)
            f.close()
            pos = []
            for x in range(len(Positions)):
                pos.append(eval(Positions[x]))
            Positions = pos
            f.close()
    elif As == 2:
        global tk
        tk = Tk()
        tk.title('Input')
        tk.attributes('-fullscreen', True)
        tk.config(bg='black')
        tk.attributes('-alpha', 0.3)
        focus_window("PROClient")
        focus_window("Input")
        tk.bind('<ButtonRelease-1>', lossfocus)
        tk.mainloop()
        f = open("Locations.txt", 'w+')
        for x in range(len(Positions)):
            jsonString = json.dumps(Positions[x])
            jsonFile = f
            jsonFile.write("%s\n" % jsonString)
        jsonFile.close()
    return Positions
