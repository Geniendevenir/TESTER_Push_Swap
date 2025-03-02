import subprocess
import os
import threading
import time
import animation
import Check_Result
from rich.live import Live

stop_event = threading.Event()
  
def make_prog():
	path_to_make = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
	exec_prog("make", path_to_make, "Test: \[make]", None)
	exec_prog(["make", "fclean"], path_to_make, "Test: \[make fclean]", None)
	exec_prog(["make", "re"], path_to_make, "Test: \[make re]", None)

def push_swap_prog(to_sort):
	path_to_ps = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
	prog = ["./push_swap"] + to_sort
	output_list = exec_prog(prog, path_to_ps, "Test: Compiling", None)
	Check_Result.check_result(output_list.stdout, to_sort)

def exec_prog(prog, path, message, pipe=None):
	stop_event.clear()
	animation_thread = threading.Thread(target=animation.loading_animation, args=(stop_event, message,))
	animation_thread.start()
	try:
		output_list = subprocess.run(prog, capture_output=True, input=pipe, cwd=path, text=True, check=True)
		stop_event.set()
		animation_thread.join()
		with Live ("", refresh_per_second=10) as live:
			live.update(f"{message} ✅")	
		return output_list
	except subprocess.CalledProcessError as e:
		stop_event.set()
		animation_thread.join()
		print(f"\nCompilation failed! {prog} ❌")
		print("🔹 error output:\n", e.stderr)
		exit(1)

