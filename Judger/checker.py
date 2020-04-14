from subprocess import run, PIPE, CalledProcessError
import os
import importlib

def py_run_check(inp, out, pyfile):
    """
    run_check(string input, string output answer, python file full address)
    return True when the output of python program(with specified input) is the same with
    the output answer. 
    """
    proc = run(['python3', pyfile], stdout=PIPE, stderr=PIPE,input=inp, encoding="ascii")
    try:
        code = proc.check_returncode()
    except CalledProcessError as e:
        return proc.stderr
    out1 = proc.stdout
    if (out==out1):
        return True
    return "Wrong answer"

# def check_two_program(correct, answer):

def py_check_input_output(inp, out, pyfile):    
    """
    its the same with py_run_check(), but with automatic read the inp and out as file
    """
    if (os.access(inp, os.R_OK) and os.access(out, os.W_OK)):
        with open(inp, "r+") as rf:
            inp1 = rf.read()
        with open(out, "r+") as rf:
            out1 = rf.read()        
        return py_run_check(inp1, out1, pyfile)
    else:
        return "Server Error"


def py_static_check(writeuppy, pyfile):
    """
    py_static_check(string writeuppy)
    writeuppy is a python file that contain static_in, static_out
    """
    pyans = importlib.import_module(writeuppy, __name__)
    for i in range(len(pyans.static_in)):
        test = py_run_check(pyans.static_in[i], pyans.static_out[i], pyfile)
        if (test!=True):
            return test 
    return True

if (__name__=="__main__"):
    print(py_static_check("problems.example.answer", "problems/example/writeup/static.py"))