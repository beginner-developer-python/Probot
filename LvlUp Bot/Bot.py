from pymem import *
from pymem.process import *
from pymem.ptypes import *
from Movement import *
import tkinter as tk

try:

    def getPointerAddress(base, offsets):
        remote_pointer = RemotePointer(pm.process_handle, base)
        for offset in offsets:
            if offset != offsets[-1]:
                remote_pointer = RemotePointer(
                    pm.process_handle, remote_pointer.value + offset)
            else:
                return remote_pointer.value + offset

    pm = Pymem("PROClient.exe")
    gameModule = module_from_name(
        pm.process_handle, "GameAssembly.dll").lpBaseOfDll
    gameModule_2 = module_from_name(
        pm.process_handle, "UnityPlayer.dll").lpBaseOfDll
    Op_Id_Ads = getPointerAddress(gameModule_2+0x01A5A978,
                               offsets=[0x8, 0x10, 0x28, 0x0, 0x78, 0X28, 0x8AC])
    print(pm.read_int(Op_Id_Ads))
    Op_Health_Ads = getPointerAddress(gameModule+0x00DD83D0,
                                   offsets=[0xB8, 0x0, 0x8B4])
    print(pm.read_int(Op_Health_Ads))


except Exception as e:
    print(e)
