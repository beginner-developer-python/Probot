import win32com.client
import pyautogui
import time
import win32api
import win32con
from pynput import mouse
import keyboard
from pynput.mouse import Controller

NumberOfMouseClicks = 0
class MyException(Exception):pass
listener = ""
xA=""
yA=""

def _on_click(x, y, button, pressed):
    if pressed:
        global xA,yA
        xA = x
        yA = y
        listener.stop()


def mouse_pos(print_s):
    print(print_s)
    global listener
    with mouse.Listener(on_click=_on_click) as listener:
        try:
            listener.join()
        except MyException as e:
            print(e)
    return xA,yA

shell = win32com.client.Dispatch("WScript.Shell")

def press_key(Windown_Name, key):
    shell.AppActivate(Windown_Name)
    shell.SendKeys(key, 0)
    time.sleep(0.1)

shell = win32com.client.Dispatch("WScript.Shell")
def focus_window(Windown_Name):
    shell.AppActivate(Windown_Name)

def locate_image(Image):
    start = pyautogui.locateCenterOnScreen(Image, region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    if start is not None:
        pyautogui.moveTo(start) 
        print("Image detected")
    else:
        print("Image not detected")
    return start

def detect_image(Image):
    start = pyautogui.locateCenterOnScreen(Image, region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    return start

def click_Left():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.1)

def click_Right():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
    time.sleep(0.1)
