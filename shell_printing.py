import sys
import pyfiglet

from rich.live import Live
from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.prompt import Prompt

import tty
import termios
import shutil

TEXT_MENU = 1
TEXT_SELECT = 2
TEXT_BUILDING = 3
TEXT_QUIT = 42
WIDTH = 70

console = Console()

def get_cursor_position():
	old_settings = termios.tcgetattr(sys.stdin)

	try:
		tty.setcbreak(sys.stdin.fileno())

		sys.stdout.write("\033[06n")
		sys.stdout.flush()

		response=""
		while True:
			char = sys.stdin.read(1)
			response += char
			if char == "R":
				break
	
	finally:
		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

	try:
		_,position = response.split("[")
		row, col = map(int, position[:-1].split(";"))
		return row, col
	except ValueError:
		return None	

def print_centered(text, len):
	width = shutil.get_terminal_size().columns
	padding = (width - len) // 2
	text.pad_left(padding)

	console.print(text, end="")
	console.file.flush()


def input_centered():
	console.file.write("\033[1A\033[2K")
	console.file.flush()
	_, col = get_cursor_position()
	console.file.write(f"\033[1B\033[{col}G")
	console.file.flush()
	return console.input()


def gradient_text(text):
	rich_text = Text()
	for i, char in enumerate(text):
		r = min(255, 100 + i * 5)
		g = min(255, 80 + i * 3)
		b = 200
		rich_text.append(char, style=f"bold rgb({r},{g},{b})")
	return(rich_text)

def print_text(option):
	if option == TEXT_MENU:
		Welcome = gradient_text("Welcome to the Genius Tester\n")	
		Opt_1 = gradient_text("1 - General Tests\n")	
		Opt_2 = gradient_text("2 - Specific Tests\n")
		Opt_3 = gradient_text("3 - Quit\n\n")
		print_centered(Welcome, 30)
		print_centered(Opt_1, 20)
		print_centered(Opt_2, 20)
		print_centered(Opt_3, 20)
	elif option == TEXT_SELECT:
		valid_choice = {"1", "2", "3"}
		choice = ""
		text = Text("Select an option: ", style="bold blue")
		print_centered(text, 20)
		while choice not in valid_choice:
			choice = input_centered()
			if choice not in valid_choice:
				console.file.write(f"\033[1A\033[2K")
				console.print(text, end="")
				console.file.flush()
		return choice
	elif option == TEXT_BUILDING:
		build = gradient_text("Currently building the feature\n")
		print_centered(build, 30)
	elif option == TEXT_QUIT:
		quit = gradient_text("See you genius\n")	
		print_centered(quit, 15)


def print_centered_title(text):
	terminal_width = shutil.get_terminal_size().columns

	figlet_text = pyfiglet.figlet_format(text, font="slant")

	centered_text = "\n".join(line.center(terminal_width) for line in figlet_text.split("\n"))

	console.print(centered_text)
		