import tkinter
from tkinter import ttk


def convert():
    entry_select = entry_box.get()
    combo_select = conv_combo.get()
    if entry_select == combo_select:
        same = entry.get()
        return conv_calc.config(text=f"{same}")
    else:
        choice = eval(f"{entry_select}_to_{combo_select}()")
        return choice


def miles_to_kilometers():
    mile = float(entry.get())
    km = round(mile * 1.60934, 3)
    conv_calc.config(text=f"{km}")


def kilometers_to_miles():
    km = float(entry.get())
    mile = round(km * 0.62137119, 3)
    conv_calc.config(text=f"{mile}")


def feet_to_miles():
    feet = float(entry.get())
    mile = round(feet * 0.000189394, 3)
    conv_calc.config(text=f"{mile}")


def miles_to_feet():
    mile = float(entry.get())
    feet = round(mile * 5280, 3)
    conv_calc.config(text=f"{feet}")


def kilometers_to_feet():
    km = float(entry.get())
    feet = round(km * 3280.84, 3)
    conv_calc.config(text=f"{feet}")


def feet_to_kilometers():
    feet = float(entry.get())
    km = round(feet * 0.00003048, 3)
    conv_calc.config(text=f"{km}")


window = tkinter.Tk()
window.title("Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

equal_label = tkinter.Label(text="is equal to", font=("Arial", 12))
equal_label.grid(column=0, row=1)

entry = tkinter.Entry(width=10)
entry.grid(column=1, row=0)

entry_box = ttk.Combobox(state="readonly", values=["miles", "kilometers", "feet"])
entry_box.grid(column=2, row=0, padx=(10, 0))
entry_box.config(width=10)

conv_calc = tkinter.Label(text="0", font="Arial, 12")
conv_calc.grid(column=1, row=1)

conv_combo = ttk.Combobox(state="readonly", values=["miles", "kilometers", "feet"])
conv_combo.grid(column=2, row=1, padx=(10, 0))
conv_combo.config(width=10)

calculate_button = tkinter.Button(text="Convert", command=convert)
calculate_button.grid(column=1, row=3)

window.mainloop()
