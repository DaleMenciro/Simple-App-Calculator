#tkinter for GUI
import tkinter as tk
#messagebox for error message
from tkinter import messagebox

# define arithmetic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # raise an exception if y is 0 to avoid division by zero error

    return x / y

# function to perform arithmetic operation according to user input
def calculate():
    try:
        # get user inputs from Entry fields and option selected in Radiobutton

        # execute selected arithmeric operation
    #Exception for value error
    except ValueError:
    #Exception for zero division error
    except ZeroDivisionError as e: