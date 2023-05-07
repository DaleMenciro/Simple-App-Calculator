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
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operation = operation_var.get()

        # execute selected arithmeric operation
        if operation == "Addition":
            result = add(num1, num2)
        elif operation == "Subtraction":
            result = subtract(num1, num2)
        elif operation == "Multiplication":
            result = multiply(num1, num2)
    #Exception for value error
    except ValueError:
    #Exception for zero division error
    except ZeroDivisionError as e:

# function to clear

# function to allow user to try again

# function to exit the program

# create the GUI window and set its title
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("350x350")

# setting the weights of the columns and rows to make them responsive

# create a variable to store the user's selected arithmetic operation
operation_var = tk.StringVar(value="Addition")

# create a label to prompt the user for arithmeric operation
operation_label = tk.Label(root, text="Select operation:")
operation_label.grid(row=0, column=0)

# create Radiobuttons for each arithmetic operation and store in the operation_var variable
addition_radio = tk.Radiobutton(root, text="Addition", variable=operation_var, value="Addition")
addition_radio.grid(row=1, column=0)

subtraction_radio = tk.Radiobutton(root, text="Subtraction", variable=operation_var, value="Subtraction")
subtraction_radio.grid(row=2, column=0)

multiplication_radio = tk.Radiobutton(root, text="Multiplication", variable=operation_var, value="Multiplication")
multiplication_radio.grid(row=3, column=0)

division_radio = tk.Radiobutton(root, text="Division", variable=operation_var, value="Division")
division_radio.grid(row=4, column=0)

# create Entry fields
num1_label = tk.Label(root, text="Enter first number:")
num1_label.grid(row=0, column=1)

num1_entry = tk.Entry(root)
num1_entry.grid(row=1, column=1)

num2_label = tk.Label(root, text="Enter second number:")
num2_entry = tk.Entry(root)
num2_entry.grid(row=2, column=1)
# create a button to perform the arithmetic operation

# create a label to display the result
result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=1, sticky="NSEW")

# create buttons for user to clear

# create buttons for user to clear

# run the GUI window