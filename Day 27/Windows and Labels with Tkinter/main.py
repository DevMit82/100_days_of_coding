from tkinter import *

#Button
def button_clicked():
    my_label["text"] = input.get()

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#How to create Label:
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New text")
my_label.grid(column=0, row=0)

#Button
button = Button(text="Click me" , command=button_clicked)
button.grid(column=1, row=2)

#New Button
new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)


# has to be at the end of the programm
window.mainloop()