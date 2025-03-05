import datetime
import os

RESULT_FOLDER = "test_results"
BASE_FILENAME = "output_test_"
global_file_path = None

def create_folder():
	if not os.path.exists(RESULT_FOLDER):
		os.makedirs(RESULT_FOLDER)

def get_next_filename():
	number = 0
	while True:
		filemane = BASE_FILENAME + str(number) + ".txt"
		file_path = os.path.join(RESULT_FOLDER, filemane)
		if not os.path.exists(file_path):
			return file_path
		number += 1	

def create_test_file():
	global global_file_path
	os.makedirs(RESULT_FOLDER, exist_ok=True)		
	global_file_path = get_next_filename()


def append_to_test_file(content):
	if global_file_path:
		with open(global_file_path, "a") as file:
			file.write(content + "\n")
