import os

import PyInstaller.__main__

programm_name = "moneybook"
programm_path = "/workspace/Pets/Our_Many/dist"
PyInstaller.__main__.run([
    f'{programm_name}.py',
    '--onefile',
])

command = f'export PATH="$PATH:~{programm_path}"'
err = os.system(f'echo $PATH | grep -q  {programm_path}')

if err:
    print("отсуствует", err)
    with open("/home/ledovskoy/.bashrc","a+") as file:
            file.write(command + "\n")
    os.system('sudo reboot')
else:
    print("есть!", err)
