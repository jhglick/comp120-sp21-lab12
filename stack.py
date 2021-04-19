# File: stack.py
# Date: April 14, 2020
# Author: COMP 120 class
# Description: List implementation of Stack ADT.

class EmptyStackException(Exception): pass

class Stack:
    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.items = []  # items stores the stack - top is the rightmost
                        # element in the stack.

    def is_empty(self):
        """
        Returns True if the stack is empty, and False if not.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Pushes item onto the top of the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Pops and returns the element on the top of stack.
        Raises EmptyStackException if stack is empty.
        """
        if len(self.items) == 0:
            raise EmptyStackException()

        return self.items.pop()
        
    def peek(self):
        """
        Returns without popping the element on the top of stack.
        Raises EmptyStackException if stack is empty.
        """
        if len(self.items) == 0:
            raise EmptyStackException()

        return self.items[-1]

    def size(self):
        """ 
        Returns the number of items in the stack.
        """
        return len(self.items) 

    def __str__(self):
        """
        Returns a string representation of the stack
        """
        return "Bottom" + str(self.items) + "Top"
