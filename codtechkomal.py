import tkinter as tk
from tkinter import messagebox

# Functions for calculator operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to handle button clicks
def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Creating the UI
window = tk.Tk()
window.title("Simple Calculator")

# Increase window size
window.geometry("400x300")  # Set the window size to 400x300

# Input fields
entry1 = tk.Entry(window, width=25)
entry1.grid(row=0, column=1, padx=10, pady=10)

entry2 = tk.Entry(window, width=25)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Labels
label1 = tk.Label(window, text="First Number:")
label1.grid(row=0, column=0)

label2 = tk.Label(window, text="Second Number:")
label2.grid(row=1, column=0)

# Buttons for operations with increased size
add_button = tk.Button(window, text="Add", command=lambda: calculate('add'), width=10, height=2)
add_button.grid(row=2, column=0, padx=10, pady=10)

subtract_button = tk.Button(window, text="Subtract", command=lambda: calculate('subtract'), width=10, height=2)
subtract_button.grid(row=2, column=1, padx=10, pady=10)

multiply_button = tk.Button(window, text="Multiply", command=lambda: calculate('multiply'), width=10, height=2)
multiply_button.grid(row=2, column=2, padx=10, pady=10)

divide_button = tk.Button(window, text="Divide", command=lambda: calculate('divide'), width=10, height=2)
divide_button.grid(row=2, column=3, padx=10, pady=10)

# Result label
result_label = tk.Label(window, text="Result: ", font=("Arial", 12))
result_label.grid(row=3, columnspan=4, pady=10)

# Run the application
window.mainloop()
