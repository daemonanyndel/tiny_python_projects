from io import StringIO
import subprocess as sp
import os

#consonants = ["boat", "tiger", "lion"]
#vowels = ["airplane", "octopus", "item"]
help_flags = ["-h", "--help"]


def test_consonant():
    results = sp.run("python crowsnest.py narwhal", text=True, capture_output=True)
    result = results.stdout
    assert result == "Ahoy, Captain, a narwhal off the larboard bow!\n"

def test_vowel():
    results = sp.run("python crowsnest.py octopus", text=True, capture_output=True)
    result = results.stdout
    assert result == "Ahoy, Captain, an octopus off the larboard bow!\n"

def test_usage():
    results = sp.run("python crowsnest.py", text=True, capture_output=True)
    result = results.stderr
    assert result.startswith("usage")
    
def test_help():
    for flag in help_flags:
        python_run_line = "python crowsnest.py " + flag
        results = sp.run(python_run_line, text=True, capture_output=True)
        result = results.stdout
        assert result.startswith("usage")



    
