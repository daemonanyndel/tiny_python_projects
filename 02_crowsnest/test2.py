from io import StringIO
import subprocess as sp
import os

#consonants = ["boat", "tiger", "lion"]
#vowels = ["airplane", "octopus", "item"]
help_flags = ["-h", "--help"]


def test_consonant():
    results = sp.run("python solution.py narwhal", text=True, capture_output=True)
    result = results.stdout
    assert result == "Ahoy, Captain, a narwhal off the larboard bow!\n"

def test_vowel():
    results = sp.run("python solution.py octopus", text=True, capture_output=True)
    result = results.stdout
    assert result == "Ahoy, Captain, an octopus off the larboard bow!\n"

def test_usage():
    results = sp.run("python solution.py", text=True, capture_output=True)
    result = results.stdout
    assert result.startswith("usage")
    
def test_help():
    for flag in help_flags:
        python_run_line = "python solution.py " + flag
        results = sp.run(python_run_line, text=True, capture_output=True)
        result = results.stdout
        assert result.startswith("usage")



    
