import tkinter as tk

calculation=""

def add_to_calculation(symbol):
    global calculation
    calculation +=str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")


root=tk.Tk()
root.geometry("300x275")
text_result = tk.Text(root,height=2,width=16,font=("Arial",26))
text_result.grid(columnspan=5)

btn_1= tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))

root.mainloop()