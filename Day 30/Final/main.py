from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def pw_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    entry_pw.insert(0, f"{password}")
    pyperclip.copy(password)
    # ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = entry_website.get()
    email = entry_email.get()
    pw = entry_pw.get()
    new_data = {
        website: {
            "email": email,
            "password": pw,
        }
    }

    if len(website) <= 0 or len(pw) <=0:
        messagebox.showerror(title="Oops", message="Dont leave any field empty!")

    else:
        try:
            with open("pw_list.json", "r") as pw_list:
                #reading old data
                data = json.load(pw_list)
        except FileNotFoundError:
             with open("pw_list.json", "w") as pw_list:
                json.dump(new_data, pw_list, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("pw_list.json", "w") as pw_list:
                #saving updated data
                json.dump(data, pw_list, indent=4)
        finally:
            entry_website.delete(0,END)
            entry_pw.delete(0,END)

#-----------------------------Search Password---------------------------#

def find_pw():
    website = entry_website.get()
    #open pw_list
    try:
        with open("pw_list.json", "r") as pw_list:
                #reading old data
                data = json.load(pw_list)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        # if website in pw_list
        if website in data:
            messagebox.showinfo(title=f"{website}", message= "Email: "+data[f"{website}"]["email"]+"\n"
                                                            +"Password: "+data[f"{website}"]["password"])
        # if website not in pw_list
        else:
            messagebox.showerror(title="No Data", message="There is no data for this website.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1,row=0)

##########################################################
###Labels:

lab_website = Label(text="Website:")
lab_website.grid(column=0, row=1)

lab_email = Label(text="Email/Username:")
lab_email.grid(column=0, row=2)

lab_pw = Label(text="Password:")
lab_pw.grid(column=0, row=3)
###########################################################
###Buttons:

btn_generate_pw = Button(text="Generate Password", command=pw_generator)
btn_generate_pw.grid(column=2, row=3)

btn_add = Button(text="Add", width=44, command=save)
btn_add.grid(column=1, row=4, columnspan=2)

btn_search = Button(text= "Search",width=14, command=find_pw)
btn_search.grid(column=2, row=1)
############################################################
###Entrys:

entry_website = Entry(width=34)
entry_website.grid(column=1, row=1,)
entry_website.focus()

entry_email = Entry(width=52)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, string="devmit@mail.com")

entry_pw = Entry(width=33)
entry_pw.grid(column=1, row=3)









window.mainloop()