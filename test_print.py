import sys

from rich.live import Live
from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.prompt import Prompt


#BASIC WRITE METHOD
"""
import sys
def write_text():
	valid_answer = {"1", "2", "3"}
	answer = ""
	sys.stdout.write("Test\n\n")
	sys.stdout.flush()
	while answer not in valid_answer:
		sys.stdout.write("\033[1A\033[2K")
		sys.stdout.write("Select an option: ")
		sys.stdout.flush()
		answer = sys.stdin.readline().strip()
"""

#BASIC PRINT METHOD
""" import sys
def print_text():
	valid_answer = {"1", "2", "3"}
	answer = ""
	print("Test\n")
	while answer not in valid_answer:
		print("\033[1A\033[2K", end="")
		print("Select an option: ", end="")
		answer = input()
print_text()
"""

#BASIC RICH METHOD
""" 
console = Console()

def print_rich_text_simple():
	valid_answer = {"1", "2", "3"}
	answer = ""
	console.print("Test\n")
	while answer not in valid_answer:
		console.file.write("\033[1A\033[2K")
		console.file.flush()
		console.print("Select an option: ", end="")
		answer = console.input()

print_rich_text_simple()
"""

#COLOR RICH METHOD
""" 
console = Console()

def print_rich_text_color():
	valid_answer = {"1", "2", "3"}
	answer = ""
	selection_text = Text("Select an option: ", style="bold blue", end="")
	console.print("Test\n")
	while answer not in valid_answer:
		console.file.write("\033[1A\033[2K")
		console.file.flush()
		console.print(selection_text, end="")
		answer = console.input()

print_rich_text_color()
"""

#BRUT FORCED CENTERED RICH METHOD
""" 
console = Console()

def print_rich_text_centered():
	valid_answer = {"1", "2", "3"}
	answer = ""
	selection_text = Text("Select an option: ", style="bold blue", end="")
	a_selection_text = Align(selection_text, align="center")
	console.print("Test\n")
	while answer not in valid_answer:
		console.file.write("\033[1A\033[2K")
		console.file.flush()
		console.print(a_selection_text, end=" ")
		console.file.write(f"\033[1A\033[50G")
		console.file.flush()
		answer = console.input()
		
print_rich_text_centered()
"""

#AUTOMATIC CENTERED RICH METHOD
import tty
import termios
import shutil

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

def print_rich_automatic_centered():
	valid_answer = {"1", "2", "3"}
	answer = ""

	width = shutil.get_terminal_size().columns

	selection_text = "Select an option: "
	padding = (width - len(selection_text)) // 2

	styled_text = Text(selection_text, style="bold blue")	
	styled_text.pad_left(padding)
	console.print("Test\n")

	while answer not in valid_answer:
		console.file.write("\033[1A\033[2K")
		console.file.flush()

		console.print(styled_text, end="")
		console.file.flush()

		_, col = get_cursor_position()
		console.file.write(f"\033[{col}G")
		console.file.flush()

		answer = console.input()
		
print_rich_automatic_centered()