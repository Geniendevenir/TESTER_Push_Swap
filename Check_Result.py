
import platform
import os
import exec
import re

def check_invalid_input():
	""" """

def check_result(output_list, to_sort):
	nbr_of_moves = is_valid_move(output_list)
	check_nbr_move(to_sort, nbr_of_moves)
	#is_sorted(output_list, to_sort)

def is_valid_move(output_list):
	valid_move = {
		"sa\n", 
		"sb\n", 
		"ss\n", 
		"pa\n", 
		"pb\n", 
		"ra\n", 
		"rb\n", 
		"rr\n", 
		"rra\n", 
		"rrb\n", 
		"rrr\n",
		}
	print(output_list)
	if len(output_list) == 0:
		print("Output_list empty")
	pattern = rf'(?<=\n)'
	output_moves = re.split(pattern, output_list)
	print(output_moves) 
	for move in output_moves: 
		if len(move) != 0 and move not in valid_move:
			print(f"{repr(move)} is not a valid move")
			exit(1)
	print("Valid Moves")
	return (len(output_moves))	

def check_nbr_move(to_sort, nbr_of_moves):
	print(f"Nbr_to_sort = {len(to_sort)}")
	print(f"Move_to_sort = {nbr_of_moves - 1}") 


def is_sorted(output_list, to_sort):
	os_name = platform.system()
	path_to_checker = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
	prog = "./checker_" + os_name.lower()  
	result = exec.exec_prog([prog] + to_sort, path_to_checker, "Test: Result", output_list)
	if result.stdout == "OK\n":
		print("Success: The list is Sorted")
	else:
		print("Error: The list is not Sorted")
