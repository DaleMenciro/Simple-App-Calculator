#tkinter for GUI
import tkinter as tk
#messagebox for error message
from tkinter import messagebox

# define arithmetic functions
def add(x, y):
    return int(x + y)

def subtract(x, y):
    return int(x - y)

def multiply(x, y):
    return int(x * y)

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
        elif operation == "Division":
            result = divide(num1, num2)

        result_label.config(text=f"Result: {result}")
    #Exception for value error
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter a valid number.")
    #Exception for zero division error
    except ZeroDivisionError as e:
        messagebox.showerror("Error", e)

# function to clear and result label
def clear():
    num1_entry.delete(0, tk.END)
    num2_entry.delete(0, tk.END)
    result_label.config(text="Result:")

# function to allow user to try again
def try_again():
    clear()
    messagebox.showinfo("Try Again", "Please enter new values and operation.")

# function to exit the program
def exit_program():
    root.destroy()

# create the GUI window and set its title
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("350x350")

# setting the weights of the columns and rows to make them responsive
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)

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
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=1, sticky="NSEW")

# create a label to display the result
result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=1, sticky="NSEW")

# create buttons for user to clear
clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=5, column=0, sticky="NSEW")

try_again_button = tk.Button(root, text="Try Again", command=try_again)
try_again_button.grid(row=5, column=1, sticky="NSEW")

# create buttons for user to clear
exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.grid(row=5, column=2, sticky="NSEW")

# run the GUI window
root.mainloop()