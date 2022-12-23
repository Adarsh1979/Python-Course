from tkinter import *


def button_clicked():
    print("button is clicked")


window = Tk()
window.title("Hello")
window.minsize(width=500, height=300)


# creating label
my_label = Label(text="My Label", font=("Times New Roman", 20))
my_label.grid(row=0, column=0)

my_label["text"] = "new text"
my_label.config(text="adarsh")


# creating button
button = Button(text="click me", command=button_clicked)
button.grid(row=1, column=1)


button2 = Button(text="click me", command=button_clicked)
button2.grid(row=0, column=2)


# Entry
my_entry = Entry(width=10)
entry_value = my_entry.get()
print(entry_value)
my_entry.grid(row=2, column=3)

window.mainloop()
