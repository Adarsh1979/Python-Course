# ****************************** Password Manager Project using Tkinter GUI ********************************************

# we have different sections of code to achieve this project i.e.
# -> Password Generator
# -> Saving the details (Website_name, Email/username, Password) in .json file
# -> Finding the Email and Password with the help of Website_name
# -> Creating UI for above three functionality


from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip        # for copying password to clipboard
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for item in range(randint(8, 10))]      # This list will have random no. of elements betn 8 to 10 (8 or 9 or 10) and the elements will come randomly from lettres list
    password_symbols = [choice(symbols) for item2 in range(randint(2, 4))]
    password_numbers = [choice(numbers) for item3 in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)        # Here we are using PYPERCLIP module to save the generated pass. to the clipboard


# ---------------------------- SAVE WEBSITE, EMAIL & PASSWORD DATA ------------------------------- #
def save_data():
    website_data = website_entry.get()      # Getting the data (string) inside the website entry field
    email_data = email_entry.get()
    password_data = password_entry.get()

    # With the help of above data, we've made a dictionary 'new_data'. So that we can further add it in data.json file
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data
        }
    }

    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=f"Confirmation Message", message=f"Entered details are:\nWeb"
                                                                    f"site: {website_data}\nPassword:{password_data}")
        if is_ok:
            # we have put below code in try except block becoz if we save the data first time, there will not be any
            # data.json present. So opening it in read mode will coz FileNotFoundError
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:       # Since data.json is not there for 1st time, we are
                    #                                             creating it with 'w' mode
                    json.dump(new_data, data_file, indent=4)    # here we are putting that new_data dictionary in
                    #                                        data_file variable which contains the opened file data.json
            else:
                data.update(new_data)       # if try block got executed successfully, then in this else block we are
                # updating our current data by adding new_data in it
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)  # and then here we are putting this updated data in .json file
            finally:
                website_entry.delete(0, END)        # deleting the previously entered data in the entry field
                password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_data = website_entry.get()  # .get() is method to get the string written inside entry

    try:  # When there is no data.json file, then it will throw a FileNotFoundError,
        #   to catch that we've used this try and except block
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File found.")  # just showing msg that no data is avail

    else:
        # Method 1: (My method)
        # for (key, value) in data.items():
        #     if key == website_data:
        #         email = data[key]["email"]
        #         password = data[key]["password"]
        #         messagebox.showinfo(title=website_data, message=f"Email: {email}\nPassword: {password}")
        #         break

        # Method 2: (Angela's method)
        if website_data in data:
            email = data[website_data]["email"]
            password = data[website_data]["password"]
            messagebox.showinfo(title=website_data, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Message", message=f"No details for {website_data} exists")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=20)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=20)
email_entry.insert(0, "adarsh@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=26)
password_entry.grid(row=3, column=1)

# Buttons
generate_pass_btn = Button(text="Generate Password", width=13, command=generate_password)
generate_pass_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)

search_btn = Button(text="Search", width=10, command=find_password)
search_btn.grid(row=1, column=2)

window.mainloop()

