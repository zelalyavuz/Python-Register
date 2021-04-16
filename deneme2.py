from winreg import *
from contextlib import suppress
import itertools

def subkeys(path, hkey=HKEY_LOCAL_MACHINE, flags=0):
    with suppress(WindowsError), OpenKey(hkey, path, 0, KEY_READ|flags) as k:
        for i in itertools.count():
            yield EnumKey(k, i)
            for key in subkeys(r'SOFTWARE\Microsoft\Windows\CurrentVersion'):

                print (subkeys())