import time
from colorama import Fore, init

init(autoreset=True)

print(Fore.RED + "[!] FIGYELEM: Bitcoin Bányász modul indítása...")
time.sleep(1)
print(Fore.YELLOW + "Rendszer erőforrások átvétele...")
time.sleep(2)
print(Fore.GREEN + "Csatlakozva Alex tárcájához.")
print("Bányászat folyamatban az Ön villanyszámlájának terhére...")

for i in range(100):
    time.sleep(0.1)
    print(f"BTC kibányászva: {i * 0.0001} -> Küldés Alexnek...")

# Ez csak vicc, nem csinál semmit valójában :)