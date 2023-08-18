from msvcrt import getwch, getch
from colorama import Fore


tecla_presionada = 'a'
while (tecla_presionada != 0):
    print("Presiona una tecla: ")
    tecla_presionada = getch()
    print(Fore.RED + f"Presionaste la tecla: {tecla_presionada.decode('utf-8')}")


