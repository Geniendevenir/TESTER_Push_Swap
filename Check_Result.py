import test_logs
import platform
import os
import exec
import re

def check_invalid_input():
	""" """

def check_result(output_list, to_sort):
	result, nbr_of_moves = is_valid_move(output_list)
	if result == 1:
		return 1
	if check_nbr_move(to_sort, nbr_of_moves):
		return 1
	if is_sorted(output_list, to_sort) == 1:
		return 1
	return 0

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
	if len(output_list) == 0:
		test_logs.append_to_test_file("Outputs_Valid: Valid -> Empty List")
		return 0, 0
	pattern = rf'(?<=\n)'
	output_moves = re.split(pattern, output_list)
	for move in output_moves: 
		if len(move) != 0 and move not in valid_move:
			test_logs.append_to_test_file("Ouputs_Validity: Invalid -> " + repr(move) + " is not a valid move")
			return 1, 0
	return (0, len(output_moves))	

def check_nbr_move(to_sort, nbr_of_moves):
	test_logs.append_to_test_file("Nbr_to_sort/Nbr_of_Moves: " + str(len(to_sort)) + "/" + str(nbr_of_moves - 1))
	test_logs.append_to_test_file("Limit_of_Move: No Limit")
	#print(f"Nbr_to_sort = {len(to_sort)}")
	#print(f"Move_to_sort = {nbr_of_moves - 1}") 
	return 0

def is_sorted(output_list, to_sort):
	os_name = platform.system()
	checker_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
	prog_name = "./checker_" + os_name.lower()  
	_, checker_result = exec.exec_push_swap([prog_name] + to_sort, checker_path, output_list)
	if checker_result.stdout == "OK\n":
		test_logs.append_to_test_file("Is_Sorted: Success")
		return 0
	else:
		test_logs.append_to_test_file("Is_Sorted: Failed -> List is not sorted")
		return 1