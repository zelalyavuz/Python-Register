import winreg
#connecting to key in registry
access_registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)

access_key = winreg.OpenKey(access_registry, r"Software\Microsoft\Office\16.0\Outlook\Search")
#accessing the key to open the registry directories under
for n in range(20):
   try:
      x =winreg.EnumValue(access_key,n)
      print(x)
   except:
      break
