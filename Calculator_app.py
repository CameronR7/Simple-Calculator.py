import tkinter as tk
from tkinter import messagebox

# Basic calculator operations
def add():
    calculate(lambda x, y: x + y)

def subtract():
    calculate(lambda x, y: x - y)

def multiply():
    calculate(lambda x, y: x * y)

def divide():
    def safe_div(x, y):
        if y == 0:
            raise ValueError("Denominator cannot be 0!")
        return x / y
    calculate(safe_div)

# The function that handles input, calculation, and result display
def calculate(operation):
    try:
        x = float(entry1.get())
        y = float(entry2.get())
        result = operation(x, y)
        result_label.config(text=f"Result: {result}")
        entry1.delete(0, tk.END)
        entry1.insert(0, str(result))  # Reuse result as first number
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def clear_inputs():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")

# Create the main window
root = tk.Tk()
root.title("Calculator App")
root.geometry("300x300")

# Entry fields for numbers
tk.Label(root, text="First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Buttons for operations
tk.Button(root, text="Add", command=add).pack(pady=5)
tk.Button(root, text="Subtract", command=subtract).pack(pady=5)
tk.Button(root, text="Multiply", command=multiply).pack(pady=5)
tk.Button(root, text="Divide", command=divide).pack(pady=5)

# Clear button
tk.Button(root, text="Clear", command=clear_inputs).pack(pady=5)

# Label to display the result
result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
