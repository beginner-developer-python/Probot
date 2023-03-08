from pymem import *
from pymem.process import *
from pymem.ptypes import *
from Movement import *
try:
    def getPointerAddress(base, offsets):
        remote_pointer = RemotePointer(pm.process_handle, base)
        for offset in offsets:
            if offset != offsets[-1]:
                remote_pointer = RemotePointer(
                    pm.process_handle, remote_pointer.value + offset)
            else:
                return remote_pointer.value + offset
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

    pm = Pymem("PROClient.exe")
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
    Id_Input_1 = int(input("Press 1 for One pokemon. 2 for Many Pokemon: "))
    Pokemons = []
    if Id_Input_1 == 1:
        Id_Input = int(input("Enter Pokemon it u want Catch: "))
    elif Id_Input_1 == 2:
        Id_Input_2 = int(input("How many Pokemon: "))
        for x in range(Id_Input_2):
            Pokemons.append(int(input(f"Pokemon To catch {x}: ")))
    else:
        print("please Try Agian")

    def catch():
        while True:
            press_key("PROClient", "a")
            press_key("PROClient", "a")
            press_key("PROClient", "d")
            press_key("PROClient", "d")
            if detect_image("Images\\Dec.png") is not None:
                if (Id_Input_1 == 2):
                    for x in range(Id_Input_2):
                        if (pm.read_int(Id_Ads) == Pokemons[x]):
                            Markings()
                elif (Id_Input_1 == 1):
                    if (pm.read_int(Id_Ads) == Id_Input):
                        Markings()
                else:
                    pyautogui.moveTo(run_pos[0], run_pos[1])
                    click_Left()

    def Markings():
        while True:
            if (pm.read_int(Health_Ads) > 2):
                pyautogui.moveTo(attk_pos[0], attk_pos[1])
                click_Left()
                pyautogui.moveTo(falseswipe_pos[0], falseswipe_pos[1])
                click_Left()
            else:
                break
        while True:
            if detect_image("Images\\Dec.png") is not None:
                pyautogui.moveTo(bag_pos[0], bag_pos[1])
                click_Left()
                pyautogui.moveTo(pokeball_pos[0], pokeball_pos[1])
                click_Left()
                time.sleep(1.0)
            else:
                pm.write_int(Id_Ads, 1)
                catch()
    catch()
except Exception as e:
    print(e)
