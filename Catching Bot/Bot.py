from pymem import *
from pymem.process import *
from pymem.ptypes import *
from Movement import *
import tkinter as tk
from colorama import Fore
# import pyfiglet

try:
    def resource_path0(relative_path):
        base_path = getattr(
            sys,
            '_MEIPASS',
            os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def resource_path(relative):
        return os.path.join(
            os.environ.get(
                "_MEIPASS2",
                os.path.abspath(".")
            ),
            relative
        )
        return os.path.join(base_path, relative_path)

    def resource_path2(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    print(Fore.RED + "ProBot")

    def Quit():
        print(Fore.GREEN + "ProBot Closed\n")
        os._exit(os.EX_OK)
    keyboard.add_hotkey("B", Quit)
    pokemon = 0
    print(Fore.GREEN + "\nPress B to Close Probot")

    def getPointerAddress(base, offsets):
        remote_pointer = RemotePointer(pm.process_handle, base)
        for offset in offsets:
            if offset != offsets[-1]:
                remote_pointer = RemotePointer(
                    pm.process_handle, remote_pointer.value + offset)
            else:
                return remote_pointer.value + offset
    Postions = []
    Postions = blockScreen()
    Image1 = resource_path('Dec.png') 
    pm = Pymem("PROClient.exe")
    if (pm > 1):
        print(Fore.GREEN + "ProClient Opened")
        gameModule = module_from_name(
            pm.process_handle, "GameAssembly.dll").lpBaseOfDll
        gameModule_2 = module_from_name(
            pm.process_handle, "UnityPlayer.dll").lpBaseOfDll
        Id_Ads = getPointerAddress(gameModule_2+0x01A5A978,
                                   offsets=[0x8, 0x10, 0x28, 0x0, 0x78, 0X28, 0x8AC])
        print(pm.read_int(Id_Ads))
        Health_Ads = getPointerAddress(gameModule+0x00DD83D0,
                                       offsets=[0xB8, 0x0, 0x8B4])
        print(pm.read_int(Health_Ads))
        Pokemons = []
        Id_Input_2 = input("[Ex: 14, 52, 64] Enter Pokemons Id: ")
        Pokemons = Id_Input_2.split(",")
        Pokemons = [eval(i) for i in Pokemons]
        # time.sleep(50)

        def catch():
            while True:
                if pokemon == 40:
                    os._exit(os.EX_OK)

                press_key("PROClient", "a")
                press_key("PROClient", "a")
                press_key("PROClient", "d")
                press_key("PROClient", "d")
                if detect_image(Image1) is not None:
                    for x in range(len(Pokemons)):
                        if (pm.read_int(Id_Ads) == Pokemons[x]):
                            Markings()
                        else:
                            if x == len(Pokemons):
                                pyautogui.moveTo(
                                    Postions[0][0], Postions[0][1])
                                click_Left()

        def Markings():
            sycn = True
            while True:
                if sycn == True:
                    time.sleep(7.0)
                    pyautogui.moveTo(Postions[5][0], Postions[5][1])
                    click_Left()
                    pyautogui.moveTo(
                        Postions[6][0], Postions[6][1])
                    click_Left()
                    sycn = False
                    time.sleep(3.0)
                if (pm.read_int(Health_Ads) > 2):
                    pyautogui.moveTo(Postions[1][0], Postions[1][1])
                    click_Left()
                    pyautogui.moveTo(Postions[2][0], Postions[2][1])
                    click_Left()
                else:
                    break
            while True:
                if detect_image(Image1) is not None:
                    pyautogui.moveTo(Postions[3][0], Postions[3][1])
                    click_Left()
                    pyautogui.moveTo(Postions[4][0], Postions[4][1])
                    click_Left()
                    time.sleep(1.0)
                else:
                    print(Fore.GREEN +
                          f"Pokemon Catched Id: {pm.read_int(Id_Ads)}")
                    pm.write_int(Id_Ads, 1)
                    global pokemon
                    pokemon = pokemon+1
                    sycn == True
                    catch()
        catch()
    else:
        print(Fore.RED + "Please Open ProClient First")
except Exception as e:
    print(Fore.RED + e)
