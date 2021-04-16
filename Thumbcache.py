from pathlib import Path

entries = Path('C:/Users/Zelâl/AppData/Local/Packages/microsoft.windowscommunicationsapps_8wekyb3d8bbwe/LocalState')
for entry in entries.iterdir():
    print(entry.name)