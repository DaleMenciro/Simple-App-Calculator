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
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
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

# function to clear

# function to allow user to try again

# function to exit the program

# create the GUI window and set its title

# setting the weights of the columns and rows to make them responsive

# create a label to prompt the user

# create Radiobuttons for each arithmetic operation and store in the operation_var variable

# create Entry fields

# create a button to perform the arithmetic operation

# create a label to display the result

# create buttons for user to clear

# create buttons for user to clear

# run the GUI window