import tkinter


def calculate():
    txt_result.delete("1.0", "end")
    convert_to = conversion_type.get()
    try:
        float(txt_value.get())
    except ValueError:
        print()
        txt_result.insert(tkinter.END, "Invalid Input!")
        return
    if convert_to == "C to F":
        answer = ((float(txt_value.get()) * 9)/5)+32
        txt_result.insert(tkinter.END, answer)
        return
    elif convert_to == "F to C":
        answer = ((float(txt_value.get()) - 32) * 5) / 9
        txt_result.insert(tkinter.END, answer)
        return
    elif convert_to == "Meters to Feet":
        answer = float(txt_value.get()) * 3.28
        txt_result.insert(tkinter.END, answer)
        return
    elif convert_to == "Feet to Meters":
        answer = float(txt_value.get()) / 3.28
        txt_result.insert(tkinter.END, answer)
        return
    elif convert_to == "KM to Miles":
        answer = float(txt_value.get()) / 1.609
        txt_result.insert(tkinter.END, answer)
        return
    elif convert_to == "Miles to KM":
        answer = float(txt_value.get()) * 1.609
        txt_result.insert(tkinter.END, answer)
        return

root = tkinter.Tk()

root.title("Unit Converter")
root.minsize(400, 200)
root.resizable(False, False)

lbl_value = tkinter.Label(root, text='Value', font=('Arial', 14, 'normal'), justify=tkinter.LEFT)
lbl_value.grid(column=1, row=1, padx=(30, 0))
txt_value = tkinter.Entry(root, width=50)
txt_value.grid(column=2, row=1, padx=(30, 0), pady=(15, 15))


# Dropdown menu options
options = [
    "C to F",
    "F to C",
    "Meters to Feet",
    "Feet to Meters",
    "KM to Miles",
    "Miles to KM",
]

# datatype of menu text
conversion_type = tkinter.StringVar()

# initial menu text
conversion_type.set("C to F")

lbl_options = tkinter.Label(root, text='Units', font=('Arial', 14, 'normal'), justify=tkinter.LEFT)
lbl_options.grid(column=1, row=2, padx=(30, 0))
conversion_options = tkinter.OptionMenu(root, conversion_type, *options)
conversion_options.grid(column=2, row=2, padx=(30, 0), pady=(15, 15))

lbl_result = tkinter.Label(root, text='Result', font=('Arial', 14, 'normal'), justify=tkinter.LEFT)
lbl_result.grid(column=1, row=3, padx=(30, 0))
txt_result = tkinter.Text(root, height=1, width=24)
txt_result.grid(column=2, row=3, padx=(20, 0), pady=(15, 15))


btn_calculate = tkinter.Button(root, text="Calculate", command=calculate)
btn_calculate.grid(column=2, row=4, pady=(15, 15))



root.mainloop()