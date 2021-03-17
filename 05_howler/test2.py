from io import StringIO
import subprocess as sp
import os

list1 = ["Test1", "Test2"]
#list1_converted = ["243-0751", "309-2360", "064-1236"]
output_flags = ["-o", "--output"]
help_flags = ["-h", "--help"]

def test_uppercases():
        python_run_line = "python howler.py " + '"The quick brown fox jumps over the lazy dog."'
        results = sp.run(python_run_line, text=True, capture_output=True)
        result = results.stdout
        assert result == "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.\n"

def test_file_input():
        python_run_line = "python howler.py " + "../inputs/fox.txt"
        results = sp.run(python_run_line, text=True, capture_output=True)
        result = results.stdout
        assert result == "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.\n"

def test_file_output_from_file():
    for flag in output_flags:
        python_run_line = "python howler.py " + "../inputs/fox.txt" + " " + flag + "out_1.txt"
        sp.run(python_run_line, text=True, capture_output=True)
        test_file = open("out_1.txt", "rt")
        test_file_text_list = test_file.readlines()
        assert test_file_text_list[0] == "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.\n"
    test_file.close()
    os.remove("out_1.txt")

def test_file_output_from_argument():
    for flag in output_flags:
        number_position = 0
        python_run_line = "python howler.py " + str(list1[number_position]) + " " + flag + "out.txt"
        sp.run(python_run_line, text=True, capture_output=True)
        test_file = open("out.txt", "rt")
        test_file_text_list = test_file.readlines()
        assert test_file_text_list[0] == (str(list1[number_position]).upper() + "\n")
        number_position = number_position + 1
    test_file.close()
    os.remove("out.txt")
    

def test_no_flags():
        python_run_line = "python howler.py"
        results = sp.run(python_run_line, text=True, capture_output=True)
        result = results.stderr
        assert result.startswith("usage")

def test_help():
    for flag in help_flags:
        python_run_line = "python howler.py " + flag
        results = sp.run(python_run_line, text=True, capture_output=True)
        result = results.stdout
        assert result.startswith("usage")

    