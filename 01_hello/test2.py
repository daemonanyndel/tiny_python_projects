import subprocess as sp
import logging
help_flags = ["-h", "--help"]
optional_names = ["Universe", "Galaxy", "Friend", "Tiger", "Solar_system"]

def logAssert(test,msg):
    if not test:
        logging.error(msg)
        assert test,msg

def test_hello_world():
    result = sp.run("python hello.py", text=True, capture_output=True)
    result_output = result.stdout
    logging.info("Testing Hello World!")
    logAssert(result_output == "Hello, World!\n", "Hello world isnt working!")
  
def test_optional_name():
    name_number = 1
    for name in optional_names:
        python_run_line = "python hello.py --name " + name
        result = sp.run(python_run_line, text=True, capture_output=True)
        result_output = result.stdout
        logging.info("Testing optional name {}!".format(name_number))
        name_number = name_number + 1
        logAssert(result_output == "Hello, " + name + "!\n", "Optional name {} isnt working!".format(name_number))
        
def test_help():
     for flag in help_flags:
        python_run_line = "python hello.py " + flag
        result = sp.run(python_run_line, text=True, capture_output=True)
        result_output = result.stdout
        assert result_output.startswith("usage")
