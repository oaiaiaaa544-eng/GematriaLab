from pathlib import Path
p=Path('GematriaLabAndroid/app/src/main/assets/index.html')
s=p.read_text()
print('UI patch placeholder', len(s))
