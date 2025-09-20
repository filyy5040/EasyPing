import subprocess
import sys
from colorama import init, Fore, Style
import os

init(autoreset=True)

def clear_screen():
    os.system('cls' if sys.platform.startswith('win') else 'clear')

def print_banner():
    print(Fore.CYAN + Style.BRIGHT + "="*40)
    print(Fore.CYAN + Style.BRIGHT + "      IP PING UTILITY (Terminal GUI)")
    print(Fore.CYAN + Style.BRIGHT + "="*40 + Style.RESET_ALL)

def ping_ip(ip_address):
    try:
        param = '-n' if sys.platform.startswith('win') else '-c'
        result = subprocess.run(['ping', param, '4', ip_address], capture_output=True, text=True)
        if result.returncode == 0:
            print(Fore.GREEN + result.stdout)
        else:
            print(Fore.RED + result.stdout)
    except Exception as e:
        print(Fore.YELLOW + f"Error: {e}")

if __name__ == "__main__":
    while True:
        clear_screen()
        print_banner()
        ip = input(Fore.CYAN + "Enter IP address to ping (or 'q' to quit): " + Style.RESET_ALL)
        if ip.lower() == 'q':
            print(Fore.MAGENTA + "Goodbye!")
            break
        ping_ip(ip)
        input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)