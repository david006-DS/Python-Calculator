import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, tk.END)
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, tk.END)
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, tk.END)

root = tk.Tk()
root.geometry("300x300")

text_result = tk.Text(root, width=20, height=2, font=("Arial", 20))
text_result.grid(columnspan=5)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation("1"), width=5, font=("Arial", 14))
btn_1.grid(column=1, row=2)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation("2"), width=5, font=("Arial", 14))
btn_2.grid(column=2, row=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation("3"), width=5, font=("Arial", 14))
btn_3.grid(column=3, row=2)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation("4"), width=5, font=("Arial", 14))
btn_4.grid(column=1, row=3)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation("5"), width=5, font=("Arial", 14))
btn_5.grid(column=2, row=3)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation("6"), width=5, font=("Arial", 14))
btn_6.grid(column=3, row=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation("7"), width=5, font=("Arial", 14))
btn_7.grid(column=1, row=4)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation("8"), width=5, font=("Arial", 14))
btn_8.grid(column=2, row=4)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation("9"), width=5, font=("Arial", 14))
btn_9.grid(column=3, row=4)
btn_0 = tk.Button(root, text="0", command=lambda: evaluate_calculation(), width=5, font=("Arial", 14))
btn_0.grid(column=2, row=5)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation("2"), width=5, font=("Arial", 14))
btn_2.grid(column=2, row=2)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(column=4, row=2)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(column=4, row=3)
btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_mul.grid(column=4, row=4)
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_div.grid(column=4, row=5)
btn_openb = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_openb.grid(column=1, row=5)
btn_closeb = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_closeb.grid(column=3, row=5)
btn_clear = tk.Button(root, text="C", command=clear_field, width=11, font=("Arial", 14))
btn_clear.grid(column=1, row=6, columnspan=2)
btn_equals = tk.Button(root, text="=", command=lambda: evaluate_calculation(), width=11, font=("Arial", 14))
btn_equals.grid(column=3, row=6, columnspan=2)
root.mainloop()
