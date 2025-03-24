import os
import webbrowser
import fade
from colorama import Fore
import pyfiglet

# Set terminal title
os.system("Solar Vortex")

# Colors
g = Fore.LIGHTGREEN_EX
b = Fore.LIGHTBLUE_EX
m = Fore.LIGHTMAGENTA_EX
r = Fore.RED

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def join_discord():
    clear()
    print(f"{b}Joining Discord server...")
    invite = "https://discord.gg/solarvortex"  # Replace with your invite
    webbrowser.open(invite)

def show_credits():
    clear()
    # Generate the ASCII art text with the standard font
    big_text = pyfiglet.figlet_format("Made by Unreleased", font="standard")
    print(f"{m}{big_text}\n")
    input("Press Enter to return...")

# Logo (Replace with your own)
logo = """
███████╗ ██████╗ ██╗      █████╗ ██████╗     ██╗   ██╗ ██████╗ ██████╗ ████████╗███████╗██╗  ██╗
██╔════╝██╔═══██╗██║     ██╔══██╗██╔══██╗    ██║   ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
███████╗██║   ██║██║     ███████║██████╔╝    ██║   ██║██║   ██║██████╔╝   ██║   █████╗   ╚███╔╝ 
╚════██║██║   ██║██║     ██╔══██║██╔══██╗    ╚██╗ ██╔╝██║   ██║██╔══██╗   ██║   ██╔══╝   ██╔██╗ 
███████║╚██████╔╝███████╗██║  ██║██║  ██║     ╚████╔╝ ╚██████╔╝██║  ██║   ██║   ███████╗██╔╝ ██╗
╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝      ╚═══╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
"""

menu = f"""
{b}╔═══════════════════════════════╗
║                               ║
║     [1] Join Discord Server   ║
║     [2] Credits               ║
║                               ║
╚═══════════════════════════════╝
"""

while True:
    clear()
    print(fade.greenblue(logo))
    print(menu)
    choice = input(f"{g}Enter choice: ")

    if choice == "1":
        join_discord()
    elif choice == "2":
        show_credits()
    else:
        print(f"{r}Invalid choice! Try again.")
        input("Press Enter to continue...")
