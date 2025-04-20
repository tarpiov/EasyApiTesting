import os
from colorama import Fore

banner = f"""
{Fore.LIGHTCYAN_EX}
  ______                               _ _______        _   _              
 |  ____|                  /\         (_)__   __|      | | (_)             
 | |__   __ _ ___ _   _   /  \   _ __  _   | | ___  ___| |_ _ _ __   __ _  
 |  __| / _` / __| | | | / /\ \ | '_ \| |  | |/ _ \/ __| __| | '_ \ / _` | 
 | |___| (_| \__ \ |_| |/ ____ \| |_) | |  | |  __/\__ \ |_| | | | | (_| | 
 |______\__,_|___/\__, /_/    \_\ .__/|_|  |_|\___||___/\__|_|_| |_|\__, | 
                   __/ |        | |                                  __/ | 
                  |___/         |_|                                 |___/  
{Fore.RESET}
"""

class Screen:

    def clearScreen():
        os.system("clear || cls")

    def printBanner():
        print(banner)

class Colors:

    cyan = Fore.LIGHTCYAN_EX
    magenta = Fore.LIGHTMAGENTA_EX
    reset = Fore.RESET
    green = Fore.LIGHTGREEN_EX
    white = Fore.LIGHTWHITE_EX
    red = Fore.LIGHTRED_EX