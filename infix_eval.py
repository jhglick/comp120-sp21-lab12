# File: infix_eval.py
# Date: April 20, 2021
# Author: COMP 120 class
# Description: Code to evaluate infix expressions.

import stack
import postfix_eval

def infix_eval_driver(filename):
    """ 
    Evaluates the infix expressions contained
    in the file filename, one expression per line.
    """
    f = open(filename)
    for line in f:
        line = line.strip()
        value = infix_eval(line)
        print("%s = %0.2f" % (line, value))

def infix_eval(line):
    """ 
    Evaluates in the infix expression contained in line,
    and returns its value.
    """
    return None  # You will replace this

def infix_to_postfix(infix_expr):
    """
    Converts the infix expression infix_expr to postfix
    and returns the postfix expression as a string.
    The tokens of infix_expr are separated by space characters,
    and the tokens of the returned postfix expression should
    also be separated by space characters.
    """
    
    return None   # You will replace this
    
if __name__ == "__main__":
    infix_eval_driver("expressions.txt")

    # __name__ is a special variable whose value is '__main__' if the module is 
    # being run as a script, and the module name if it's imported.