from tkinter import *


def miles_to_km():
    miles_value = float(entry.get())
    km_value = round((miles_value * 1.60934), 5)
    label3.config(text=f"{km_value}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
# window.minsize(width=100, height=100)


label1 = Label(text="Miles", font=("Arial", 12))
label1.grid(row=0, column=2)

label2 = Label(text="is equal to ", font=("Arial", 12))
label2.grid(row=1, column=0)

label3 = Label(text="0", font=("Arial", 12))
label3.grid(row=1, column=1)

label4 = Label(text="Km", font=("Arial", 12))
label4.grid(row=1, column=2)

entry = Entry(width=10)
entry.grid(row=0, column=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

window.mainloop()
