import animation
import exec
import random
import sys
import pyfiglet
import threading
import time
import test_logs
import shell_printing as sp

from rich.live import Live
from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.prompt import Prompt

console = Console()
stop_event = threading.Event()
INT_MAX = 2147483647
INT_MIN = -2147483648
TEXT_MENU = 1
TEXT_SELECT = 2
TEXT_BUILDING = 3
TEXT_QUIT = 42
WIDTH = 70


def menu():	
	sp.print_centered_title("GENIUS TESTS")

	sp.print_text(TEXT_MENU)
	choice = sp.print_text(TEXT_SELECT)

	print("\n")  # Move to the next line after valid input

	if choice == "1":
		automatic_tester()
	elif choice == "2":
		sp.print_text(3)
	elif choice == "3":
		sp.print_text(TEXT_QUIT)
		return 0  # Exits gracefully

def selected_tests(lst_size):
	list_2 = [
		['10', '20'],
		['0', '-1'],
		['-1', '0'],
		['42', '-42']
	]

	list_3 = [
		['1', '2', '3'],
		['2', '3', '1'],
		['3', '1', '2'],
		['-10', '-1', '42'],
		['-500', '-1000000', '-1'],
		['-1', '0', '-2'],
		['0', '-4', '42']
	]

	list_max = [
		[str(INT_MAX), str(INT_MIN)],
		[str(INT_MIN), str(INT_MAX)],
		['0', str(INT_MAX), str(INT_MIN)],
		[str(INT_MAX), str(INT_MIN), '-42'],
		[str(INT_MIN), str(INT_MAX), '-42'],
		['-42', str(INT_MIN), str(INT_MAX)],
	]
	if lst_size == 2:
		return list_2
	elif lst_size == 3:
		return list_3
	elif lst_size == INT_MAX:
		return list_max

def tester(inputs, test_nbr):
	message = "Test: " + str(test_nbr + 1)
	test_logs.append_to_test_file(message)
	test_logs.append_to_test_file("Input: " + str(inputs))
	stop_event.clear()
	animation_thread = threading.Thread(target=animation.loading_animation, args=(stop_event, message))
	animation_thread.start()
	result = exec.push_swap_prog(inputs)
	test_logs.append_to_test_file("\n\n")

	stop_event.set()
	animation_thread.join()
	if result == 0:
		sys.stdout.write("\033[F\033[2K")
		with Live ("", refresh_per_second=10) as live:
			live.update(f"{message} ✅")
	else:
		sys.stdout.write("\033[F\033[2K")
		with Live ("", refresh_per_second=10) as live:
			live.update(f"{message} ❌")

def automatic_tester():
	exec.make_prog()
	#Test Invalid Input
	#Test Empty List	
	#Test Selected Inputs
	test_nbr = 0
	test_logs.append_to_test_file("TEST TWO INPUTS")
	test_two = selected_tests(2)
	for input in test_two:
		tester(input, test_nbr)
		test_nbr += 1
	test_logs.append_to_test_file("\n\n") 

	test_logs.append_to_test_file("TEST THREE INPUTS") 
	test_three = selected_tests(3)
	for input in test_three:
		tester(input, test_nbr)
		test_nbr += 1
	test_logs.append_to_test_file("\n\n") 

	test_logs.append_to_test_file("TEST INT_MAX/INT_MIN") 
	test_max = selected_tests(INT_MAX)
	for input in test_max:
		tester(input, test_nbr)
		test_nbr += 1
	test_logs.append_to_test_file("\n\n") 

	#Test Random Inputs
	test_logs.append_to_test_file("100 RANDOM TESTS") 
	for i in range(100):
		inputs = [str(random.randint(INT_MIN, INT_MAX)) for _ in range(random.randint(2, 1000))]
		tester(inputs, test_nbr)
		test_nbr += 1

if __name__ == "__main__":
	test_logs.create_folder()
	test_logs.create_test_file()
	menu()
	