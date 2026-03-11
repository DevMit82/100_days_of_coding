from tkinter import *

window = Tk()
window.title("Mile to km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def button_clicked():
    zero["text"] = int(input.get()) * 1.609344
    zero["text"] = round(zero["text"], 2)


############################Labels###################
is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

zero = Label(text="0")
zero.grid(column=1, row=1)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

km = Label(text="km")
km.grid(column=2, row=1)
#####################################################
#########################Buttons#####################
calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)
#####################################################
########################Entry########################
input = Entry(width=10)
input.grid(column=1, row=0)
####################################################


window.mainloop()