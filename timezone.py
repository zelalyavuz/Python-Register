import winreg
#connecting to key in registry
access_registry = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)

access_key = winreg.OpenKey(access_registry,r"SYSTEM\ControlSet001\Control\TimeZoneInformation")
#accessing the key to open the registry directories under
value = winreg.EnumKey()
print(value)
