from tkinter import *
from tkinter import messagebox
import random
from pyperclip import copy

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list_1 = []
    for char in range(nr_letters):
        choice = random.choice([True, False])
        if choice:
            password_list_1.append(chr(random.randint(ord("A"), ord("Z"))))
        else:
            password_list_1.append(chr(random.randint(ord("a"), ord("z"))))

    password_list_2 = [chr(random.randint(ord("0"), ord("9"))) for char in range(nr_numbers)]
    password_list_3 = [chr(random.randint(ord("!"), ord("+"))) for char in range(nr_symbols)]
    password_list = password_list_1+password_list_2+password_list_3
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(END, password)
    copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(email_entry.get()) == 0 or len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the detials entered: "
                                                                  f"\n\nEmail: {email_entry.get()} \n"
                                                                  f"Password: {password_entry.get()} "
                                                                  f"\n\nIs it okay to save?")
        if is_ok:
            with open("passwords.txt", "a") as file:
                file.write("%-30s | %-30s | %-30s\n" % (website_entry.get(), email_entry.get(), password_entry.get()))
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.focus()
website.grid(row=1, column=0)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

password_name = Label(text="Password:")
password_name.grid(row=3, column=0)

website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=52)
email_entry.insert(END, "alex_and_ye@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(row=3, column=2)

add = Button(text="Add", width=43, command=save)
add.grid(row=4, column=1, columnspan=2)


window.mainloop()
