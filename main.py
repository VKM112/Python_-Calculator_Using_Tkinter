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
    except Exception:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    update_display()

def delete_last():
    global calculation
    calculation = calculation[:-1]
    update_display()

def handle_keypress(event):
    key = event.keysym
    if key in "0123456789":
        add_to_calculation(key)
    elif key in ("plus", "minus", "asterisk", "slash", "parenleft", "parenright", "period"):
        symbols = {
            "plus": "+", "minus": "-", "asterisk": "*",
            "slash": "/", "parenleft": "(", "parenright": ")",
            "period": "."
        }
        add_to_calculation(symbols[key])
    elif key == "Return":
        evaluate_calculation()
    elif key == "BackSpace":
        delete_last()
    elif key == "Escape":
        clear_field()
    return "break"

root = tk.Tk()
root.title("Compact Calculator")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#2e2e2e")

text_result = tk.Text(root, height=2, width=25, font=("Helvetica", 22), bg="#1e1e1e", fg="white", bd=0)
text_result.grid(columnspan=5, padx=5, pady=10)
text_result.bind("<Key>", handle_keypress)

btn_bg = "#3a3a3a"
btn_fg = "white"
btn_active_bg = "#505050"
btn_font = ("Helvetica", 13)

def on_enter(e):
    e.widget['background'] = btn_active_bg

def on_leave(e):
    e.widget['background'] = btn_bg

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

    btn = tk.Button(root, text=text, command=cmd, width=4, height=2,
                    font=btn_font, bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg, bd=0)
    btn.grid(row=row, column=col, padx=1, pady=1)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

root.mainloop()
