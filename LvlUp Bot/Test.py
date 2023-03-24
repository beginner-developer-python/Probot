from Movement import * 
from pymem.process import *
from pymem import *
from pymem.ptypes import *
from pyautogui import *
pm = Pymem("PROClient.exe")
gameModule = module_from_name(
        pm.process_handle, "GameAssembly.dll").lpBaseOfDll
gameModule_2 = module_from_name(
        pm.process_handle, "UnityPlayer.dll").lpBaseOfDll


def getPointerAddress(base, offsets):
        remote_pointer = RemotePointer(pm.process_handle, base)
        for offset in offsets:
            if offset != offsets[-1]:
                remote_pointer = RemotePointer(
                    pm.process_handle, remote_pointer.value + offset)
            else:
                return remote_pointer.value + offset

def Keypress_Manytime(key, times):
    for x in range(times):
        press_key("PROClient", key=key)
        time.sleep(0.08)
def MoveToBattleField():
    focus_window("PROClient")
    pyautogui.keyDown("s")
    while True:
        if detect_image("H:\\GameHacking\\ProBot\\Probot\\LvlUp Bot\\Images\\Mailbox.png"):
            pyautogui.keyUp("s")
            break 
    press_key("PROClient", "1")
    time.sleep(1.0)
    Keypress_Manytime("d", 6)
    Keypress_Manytime("s", 15)
    Keypress_Manytime("a", 6)
    Keypress_Manytime("s", 21)
    Keypress_Manytime("a", 9)
    Keypress_Manytime("s", 5)
    Keypress_Manytime("d", 3)
def MovetoPokemonCenter():
    pass

def main():
    pass

MoveToBattleField()