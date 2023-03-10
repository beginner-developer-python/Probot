import win32com.client
import pyautogui
import time
import win32api
import win32con
from pynput import mouse
from tkinter import *
import keyboard

NumberOfMouseClicks = 0


class MyException(Exception):
    pass


listener = ""
xA = ""
yA = ""
tk = Tk()
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
    run_pos = mouse_pos("\nClick where run button is there: ")
    print(run_pos)
    attk_pos = mouse_pos("Click where attk button is there: ")
    print(attk_pos)
    falseswipe_pos = mouse_pos("Click where FalseSwipe Attk button is there: ")
    print(falseswipe_pos)
    bag_pos = mouse_pos("Click where bag button is there:")
    print(bag_pos)
    pokeball_pos = mouse_pos("Click where pokeball button is there: ")
    print(pokeball_pos)
    pokemon_location = mouse_pos("Click where pokemon button is there: ")
    print(pokemon_location)
    falseswipePoke_pos = mouse_pos("Click where Falseswipe_Pokemon is there: ")
    print(falseswipePoke_pos)
    tk.destroy()
    global Positions
    Positions = run_pos,attk_pos,falseswipe_pos,bag_pos,pokeball_pos,pokemon_location,falseswipe_pos
    for i in range(150):
        keyboard.unblock_key(i)


def mouse_pos(print_s):
    print(print_s)
    global listener
    with mouse.Listener(on_click=_on_click) as listener:
        try:
            listener.join()
        except MyException as e:
            print(e)
    return xA, yA


shell = win32com.client.Dispatch("WScript.Shell")


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
        print("Image not detected")


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
    tk.attributes('-fullscreen', True)
    tk.config(bg='black')
    tk.attributes('-alpha', 0.3)
    tk.bind('<ButtonRelease-1>', lossfocus)
    tk.mainloop()
    return Positions

