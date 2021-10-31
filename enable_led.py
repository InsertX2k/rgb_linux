from colorama import Fore, init
from os import name, system
import sys
# initializing colorama.
init(autoreset=True)

def enable_rgb():
    """
    Enables the Keyboard LED Backlight.

    Return codes are:
    0 when successed.

    1 when raised a KeyboardInterrupt event, or when an Exception in the mainloop happens.

    10 when running on Windows.

    20 when not running on any compatible OS Type. (not windows, or mac, or linux)

    """
    if name == 'posix': # if on linux.
        try:
            system('xset led named "Scroll Lock"')
            return 0
        except Exception or KeyboardInterrupt:
            print(f"{Fore.RED}[Exception] an Exception has occured that caused the program to terminate it's event loop")
            return 1
    elif name == 'nt': # if on windows.
        print(f"{Fore.RED}[ERROR] Incompatible OS type for script file.")
        print(f"{Fore.YELLOW}[INFO] The script file will close.")
        return 10 # error code 10 is for incompatible OS type.
    else: # if not either windows or linux (but not mac)
        print(f"{Fore.RED}[ERROR] Incompatible OS type {name}")
        print(f"{Fore.YELLOW}[INFO] The script file will close.")
        return 20 # error code 20 is for incompatible OS Type (not windows).
    



if __name__ == '__main__': # if double clicked on.
    ret_code = enable_rgb()
    sys.exit(ret_code)
else: # if program was imported as a Python module.
    raise ImportError("You can't import this.")