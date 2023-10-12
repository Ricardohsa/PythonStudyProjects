from tkinter import *
CONVERTION = 1.609

def convert_to_km():
    miles = int(entry_miles.get())
    km = round(miles * CONVERTION)
    label_converted.config(text=km)



window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=300)
window.eval('tk::PlaceWindow . center')
window.config(padx=50, pady=50)

label_equal = Label()
label_equal.config(text="is equal to")
label_equal.grid(column=2, row=1)

entry_miles = Entry(width=10)
entry_miles.grid(column=3, row=0)


label_miles = Label()
label_miles.config(text="Miles")
label_miles.grid(column=4, row=0)

label_converted = Label()
label_converted.config(text="0")
label_converted.grid(column=3, row=1)


label_km = Label()
label_km.config(text="Km")
label_km.grid(column=4, row=1)


button_calculate = Button()
button_calculate.config(text="Calculate", command=convert_to_km)
button_calculate.grid(column=3, row=2)


window.mainloop()