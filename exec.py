import subprocess
import os
import time
import animation
import Check_Result
import threading
import sys
import test_logs

from rich.live import Live

stop_event = threading.Event()
  
def make_prog():
	test_logs.append_to_test_file("TESTS MAKEFILE")
	path_to_make = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
	exec_make("make", path_to_make, "Test: \[make]", None)
	exec_make(["make", "fclean"], path_to_make, "Test: \[make fclean]", None)
	exec_make(["make", "re"], path_to_make, "Test: \[make re]", None)
	test_logs.append_to_test_file("\n\n\n")

def exec_make(prog, path, message, pipe=None):
	stop_event.clear()
	animation_thread = threading.Thread(target=animation.loading_animation, args=(stop_event, message,))
	animation_thread.start()
	try:
		subprocess.run(prog, capture_output=True, input=pipe, cwd=path, text=True, check=True)
		stop_event.set()
		animation_thread.join()
		sys.stdout.write("\033[F\033[2K")
		with Live ("", refresh_per_second=10) as live:
			live.update(f"{message} ✅")
		test_logs.append_to_test_file(message.replace("\\", "") + ": Success")
		return 0
	except subprocess.CalledProcessError as e:
		stop_event.set()
		animation_thread.join()
		sys.stdout.write("\033[F\033[2K")
		with Live ("", refresh_per_second=10) as live:
			live.update(f"{message} ❌")
		test_logs.append_to_test_file(message.replace("\\", "") + ": Failed\n" + e)
		return 1

def push_swap_prog(to_sort):
	prog_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
	prog_name = ["./push_swap"] + to_sort
	result, output_list = exec_push_swap(prog_name, prog_path, None)
	if result == 0:
		test_logs.append_to_test_file("Compilation: Success")
	else:
		test_logs.append_to_test_file("Compilation: Failed\n" + "Details:\n" + output_list)
		return 1
	if Check_Result.check_result(output_list.stdout, to_sort) == 1:
		return 1
	return 0
		
def exec_push_swap(prog, path, pipe=None):
	try:
		output_list = subprocess.run(prog, capture_output=True, input=pipe, cwd=path, text=True, check=True)
		return 0, output_list
	except subprocess.CalledProcessError as e:
		return 1, e 
