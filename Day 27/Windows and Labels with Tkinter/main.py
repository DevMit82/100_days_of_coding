from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#How to create Label:
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New text")

#Button
def button_clicked():
    my_label["text"] = input.get()

button = Button(text="Click me" , command=button_clicked)
button.pack()

#Entry

input = Entry(width=10)
input.pack()
print(input.get())

# has to be at the end of the programm
window.mainloop()