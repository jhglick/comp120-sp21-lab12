# File: postfix_eval.py
# Date: April 14, 2020
# Author: COMP 120 class
# Description: Code to evaluate postfix expressions.

import stack

def postfix_eval_driver(filename):
    """ 
    Evaluates the postfix expressions contained
    in the file filename, one expression per line.
    """
    
    f = open(filename)
    for line in f:
        line = line.rstrip()
        value = postfix_eval(line)
        print("%s = %0.2f" % (line, value))

def postfix_eval(line):
    """ 
    Evaluates in the postfix expression contained in line.
    """
    print("Postfix = %s" % (line))
    tokens = line.split()
    operands = stack.Stack()
    for token in tokens: 
        try:
            num = float(token)
            operands.push(num)

        except ValueError:
            value = perform_operation(token, operands)
            operands.push(value)

    return operands.pop()

def perform_operation(token, operands):
    """ 
    Performs the operation specified by token on the
    operands specified by operands.
    Returns the result
    """
    right_operand = operands.pop()
    left_operand = operands.pop()
    if token == "+":
        return left_operand + right_operand
    elif token == "-":
        return left_operand - right_operand
    elif token == "*":
        return left_operand * right_operand
    else:   # token == "/":
        return left_operand / right_operand

if __name__ == "__main__":
    postfix_eval_driver("postfix_expressions.txt")

    # __name__ is a special variable whose value is '__main__' if the module is 
    # being run as a script, and the module name if it's imported.