import winreg
#connecting to key in registry
access_registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

access_key = winreg.OpenKey(access_registry, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\S-1-5-80-3880006512-4290199581-1648723128-3569869737-3631323133")
#accessing the key to open the registry directories under
for n in range(20):
   try:
      x =winreg.EnumValue(access_key,n)
      print(x)
   except:
      break