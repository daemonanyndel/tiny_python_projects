from io import StringIO
import subprocess as sp
import os

list1 = ["boat", "tiger", "lion"]
list2 = ["airplane", "octopus", "item"]
list3 = ["kangaroo", "banana", "leopard"]
list4 = ["car", "taxi", "van"]
help_flags = ["-h", "--help"]


def test_one_item():
    for item in list1:
        python_run_line = "python picnic.py " + item
        results = sp.run(python_run_line, text=True, capture_output=True)
        result = results.stdout
        assert result == "You are bringing {}.\n".format(item)

def test_two_items():
    for item in list1:
        item_number = 0
        python_run_line = "python picnic.py " + item + " " + list2[item_number]
        results = sp.run(python_run_line, text=True, capture_output=True)
        result = results.stdout
        assert result == "You are bringing {} and {}.\n".format(item, list2[item_number])
        item_number = item_number + 1

def test_three_items():
    for item in list1:
        item_number = 0
        python_run_line = "python picnic.py " + item + " " + list2[item_number] + " " + list3[item_number]
        results = sp.run(python_run_line, text=True, capture_output=True)
        result = results.stdout
        assert result == "You are bringing {}, {}, and {}.\n".format(item, list2[item_number], list3[item_number])
        item_number = item_number + 1

def test_four_items():
    for item in list1:
        item_number = 0
        python_run_line = "python picnic.py " + item + " " + list2[item_number] + " " + list3[item_number] + " " + list4[item_number]
        results = sp.run(python_run_line, text=True, capture_output=True)
        result = results.stdout
        assert result == "You are bringing {}, {}, {}, and {}.\n".format(item, list2[item_number], list3[item_number], list4[item_number])
        item_number = item_number + 1

def test_sorted_flag():
        sorted_list_test = sorted([list1[0], list2[0], list3[0]])
        python_run_line = "python picnic.py " + list1[0] + " " + list2[0] + " " + list3[0] + " --sorted"
        results = sp.run(python_run_line, text=True, capture_output=True)
        result = results.stdout
        assert result == "You are bringing {}, {}, and {}.\n".format(sorted_list_test[0], sorted_list_test[1], sorted_list_test[2])

def test_no_flags():
        python_run_line = "python picnic.py"
        results = sp.run(python_run_line, text=True, capture_output=True)
        result = results.stderr
        assert result.startswith("usage")

def test_help():
    for flag in help_flags:
        python_run_line = "python picnic.py " + flag
        results = sp.run(python_run_line, text=True, capture_output=True)
        result = results.stdout
        assert result.startswith("usage")
