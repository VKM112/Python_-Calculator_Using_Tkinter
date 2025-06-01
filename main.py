import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    update_display()

def update_display():
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        update_display()
    except Exception as e:
        clear_field()
        text_result.insert(1.0, f"Error")

def clear_field():
    global calculation
    calculation = ""
    update_display()

def delete_last():
    global calculation
    calculation = calculation[:-1]
    update_display()

root = tk.Tk()
root.title("Calculator")
root.geometry("380x320")
root.resizable(False, False)

text_result = tk.Text(root, height=2, width=20, font=("Arial", 24))
text_result.grid(columnspan=5)
text_result.bind("<Key>", lambda e: "break")  # Disable keyboard input

# Button layout
buttons = [
    ("1", 2, 1), ("2", 2, 2), ("3", 2, 3), ("+", 2, 4),
    ("4", 3, 1), ("5", 3, 2), ("6", 3, 3), ("-", 3, 4),
    ("7", 4, 1), ("8", 4, 2), ("9", 4, 3), ("*", 4, 4),
    ("(", 5, 1), ("0", 5, 2), (")", 5, 3), ("/", 5, 4),
    (".", 6, 1), ("C", 6, 2), ("⌫", 6, 3), ("=", 6, 4),
]

for (text, row, col) in buttons:
    if text == "=":
        cmd = evaluate_calculation
    elif text == "C":
        cmd = clear_field
    elif text == "⌫":
        cmd = delete_last
    else:
        cmd = lambda val=text: add_to_calculation(val)
    
    btn = tk.Button(root, text=text, command=cmd, width=5, height=1, font=("Arial", 14))
    btn.grid(row=row, column=col, padx=2, pady=2)

root.mainloop()
