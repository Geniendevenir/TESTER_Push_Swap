import animation
import exec
import random
import sys
import pyfiglet

from rich.live import Live
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt

console = Console()

def menu():
	title = pyfiglet.figlet_format("GENIUS TESTS", font="slant")
	console.print(title)

	console.print("Welcome to the Genius Tester\n")
	console.print("[bold cyan]1 - Automatic Tester[/]")
	console.print("[bold cyan]2 - Test your own[/]")
	console.print("[bold red]3 - Quit[/]\n")  # Ensures "Quit" remains visible
	console.print("")

	choice = ""

	while choice not in {"1", "2", "3"}:
		sys.stdout.write("\033[F\033[2K")  # Keep menu intact
		sys.stdout.write("Select an option: ")
		sys.stdout.flush()
		choice = input().strip()

	print("\n")  # Move to the next line after valid input

	if choice == "1":
		automatic_tester()
	elif choice == "2":
		console.print("Currently Building the feature")
	elif choice == "3":
		console.print("See you, Genius!")
		return 0  # Exits gracefully

def automatic_tester():
	INT_MAX = 2147483647
	INT_MIN = -2147483648
	lst_size = 10
	exec.make_prog()
	for _ in range(10):
		test = [str(random.randint(INT_MIN, INT_MAX)) for _ in range(lst_size)]
		exec.push_swap_prog(test)

menu()