import os

import PyInstaller.__main__

programm_name = "moneybook"
programm_path = "/dist"
path = os.path.dirname(__file__) + programm_path

PyInstaller.__main__.run([
    f'{programm_name}.py',
    '--onefile',
])

command = f'export PATH="$PATH:{path}"'
err = os.system(f'echo $PATH | grep -q  {path}')

if err:
    with open("~/.bashrc","a+") as file:
            file.write(command + "\n")
    os.system('sudo reboot')
    print("Программа добавлена в переменную PATH. \nПрограмма успешно установлена.")
else:
    print("Программа уже была добавлена в переменную PATH. \nПрограмма успешно установлена.")
