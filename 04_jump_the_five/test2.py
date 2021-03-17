from io import StringIO
import subprocess as sp
import os

list1 = ["867-5309", "751-8745", "546-9874"]
list1_converted = ["243-0751", "309-2360", "064-1236"]
help_flags = ["-h", "--help"]

def test_one_item():
    for item in list1:
        number_position = 0
        python_run_line = "python jump.py " + list1[number_position]
        results = sp.run(python_run_line, text=True, capture_output=True)
        result = results.stdout
        assert result == "{}\n".format(list1_converted[0])
        number_position = number_position + 1 

def test_no_flags():
        python_run_line = "python jump.py"
        results = sp.run(python_run_line, text=True, capture_output=True)
        result = results.stderr
        assert result.startswith("usage")

def test_help():
    for flag in help_flags:
        python_run_line = "python jump.py " + flag
        results = sp.run(python_run_line, text=True, capture_output=True)
        result = results.stdout
        assert result.startswith("usage")
