from pathlib import Path

entries = Path('C:/Users/Zelâl/Documents/Outlook Dosyaları')
for entry in entries.iterdir():
    print(entry.name)
