from tkinter import *
from tkinter import messagebox
from dat import Database


ps = Database()
def populate_list():
    
    parts_list.delete(0, END)
    for row in ps.fetch():
        parts_list.insert(END, row)


def add_item():
    if number_plate.get() == '' or phone_number.get() == '' or id.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
        
    # if number_plate.get() in number_plate:
    #     messagebox.showerror('should be unique')
    #     return
    try:
        ps.insert(number_plate.get(), phone_number.get(),id.get())

    except:
        messagebox.showerror('Already exist', 'The number plate already exist')
        # print("it alredy exist")

    parts_list.delete(0, END)
    parts_list.insert(END, (number_plate.get(), phone_number.get(),id.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        number_plate_entry.delete(0, END)
        number_plate_entry.insert(END, selected_item[0])
        phone_number_entry.delete(0, END)
        phone_number_entry.insert(END, selected_item[1])
        id_entry.delete(0, END)
        id_entry.insert(END, selected_item[2])
    except IndexError:
        pass


def remove_item():
    ps.remove(selected_item[0])
    clear_text()
    populate_list()


# def details():
#     ps.get_details(plate_entry)
#     for row in ps.get_details():
#        parts_list.insert(END, row)

#     clear_text()
#     populate_list()




def update_item():
    ps.update(selected_item[0],number_plate.get(), phone_number.get(),id.get())
    populate_list()


def clear_text():
    number_plate_entry.delete(0, END)
    phone_number_entry.delete(0, END)
    id_entry.delete(0, END)


# Create window object
app = Tk()
app.configure(bg="black",highlightthickness=7,highlightcolor="blue")

# Part
number_plate = StringVar()
part_label = Label(app, text='NumberPlate', font=('bold', 14), pady=20,bg="black",fg="blue")
part_label.grid(row=0, column=0, sticky=W)
number_plate_entry = Entry(app, textvariable=number_plate,bg="gray")
number_plate_entry.grid(row=0, column=1)
# Customer
phone_number = StringVar()
customer_label = Label(app, text='PhoneNUmber', font=('bold', 14),bg="black",fg="blue")
customer_label.grid(row=0, column=2, sticky=W)
phone_number_entry = Entry(app, textvariable=phone_number,bg="gray")
phone_number_entry.grid(row=0, column=3)
# Retailer
id = StringVar()
retailer_label = Label(app, text='Identification', font=('bold', 14),bg="black",fg="blue")
retailer_label.grid(row=1, column=0, sticky=W)
id_entry = Entry(app, textvariable=id,bg="gray")
id_entry.grid(row=1, column=1)



# get details of owner
# plate = StringVar()
# plate_label = Button(app, text='Plate', font=('bold', 14), pady=20,bg="black",fg="blue",command=details)
# plate_label.grid(row=0, column=4, sticky=W)
# plate_entry = Entry(app, textvariable=number_plate,bg="gray")
# plate_entry.grid(row=0, column=5)



# Parts List (Listbox)
plate_list = Listbox(app, height=8, width=50,border=0,bg="gray")
plate_list.grid(row=4, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Create scrollbar





# Parts List (Listbox)
parts_list = Listbox(app, height=8, width=50,border=0,bg="gray")
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3,rowspan=6, column=3)
# Set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)
# Bind select
parts_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Add Part', width=12, command=add_item,bg="black",fg="blue")
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove Part', width=12, command=remove_item,bg="black",fg="blue")
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Part', width=12, command=update_item,bg="black",fg="blue")
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text,bg="black",fg="blue")
clear_btn.grid(row=2, column=3)

app.title('Car registration system')
app.geometry('750x400')

# Populate data
populate_list()

# Start program
app.mainloop()

