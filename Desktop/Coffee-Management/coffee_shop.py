import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
import json

# from PIL import ImageTk, Image

personal_cards = []  # all the persons
edit = False  # if the current form is editable
personal2 = None  # the person we editing if the form editable
index = 0  # the index of the editable person
opened = False  # if there is any open windows


# adds new person to the end of the file_________
def add_to_data(personal):
    personal_cards.append(personal)
    f = open("data.txt", "a")
    f.write(str(json.dumps(personal)))
    f.write("\n")
    f.close()


# rewrites all the data _________________
def refresh_data():
    f = open("data.txt", "w")
    for personal in personal_cards:
        f.write(str(json.dumps(personal)))
        f.write("\n")
    f.close()


# loads all the persons to the list
def load_all():
    if not os.path.exists("data.txt"):
        with open("data.txt", "w"):
            pass
    with open("data.txt") as file_in:
        for line in file_in:
            try:
                personal_cards.append(json.loads(line.replace("\'", "\"")))
            except:
                pass


# preview window to new workers______________
def clicked():
    global edit, opened

    if opened:
        return
    opened = True

    def back_to_menu():
        global edit, opened

        window1.destroy()

        # open the list if it was closed before
        if edit:
            edit = False
            opened = False
            open_list(personal_cards, True, "Edit Worker")

        edit = False
        opened = False

    window1 = Tk()
    window1.protocol("WM_DELETE_WINDOW", back_to_menu)
    window1.title("Worker Card")
    window1.geometry('800x500')
    window1.configure(bg="LightYellow3")

    personal = {"first_name": "", "last_name": "", "address": "", "date": "", "salary": "", "phone": "",
                "person_id": "",
                "person_type": "Employee", "gender": "Male", "has_license": False, "has_car": False}

    if edit:
        personal = personal2

    lbl0 = Label(window1, text="Details", bg="LightYellow3", fg="red", font=("Arial Bold", 40))
    lbl0.grid(column=0, row=0, columnspan=4)

    lbl = Label(window1, text="First Name:", bg="LightYellow3", font=("Arial Bold", 14), width=16)
    lbl.grid(column=0, row=1)
    txt = Entry(window1, width=9, font=("Arial Bold", 20))
    txt.grid(column=1, row=1)
    txt.insert(0, personal["first_name"])

    lbl1 = Label(window1, text="Last Name:", bg="LightYellow3", font=("Arial Bold", 14), width=16)
    lbl1.grid(column=2, row=1)
    txt1 = Entry(window1, width=9, font=("Arial Bold", 20))
    txt1.grid(column=3, row=1)
    txt1.insert(0, personal["last_name"])

    lbl4 = Label(window1, text="ID :", bg="LightYellow3", font=("Arial Bold", 14), width=16)
    lbl4.grid(column=0, row=2)
    txt4 = Entry(window1, width=9, font=("Arial Bold", 20))
    txt4.grid(column=1, row=2)
    txt4.insert(0, personal["person_id"])

    lbl5 = Label(window1, text="Salary:", bg="LightYellow3", font=("Arial Bold", 14), width=16)
    lbl5.grid(column=0, row=7)
    txt5 = Entry(window1, width=9, font=("Arial Bold", 20))
    txt5.grid(column=1, row=7)
    txt5.insert(0, personal["salary"])

    lbl6 = Label(window1, text="Date of birth:", bg="LightYellow3", font=("Arial Bold", 14), width=16)
    lbl6.grid(column=0, row=3)
    txt6 = Entry(window1, width=9, font=("Arial Bold", 20))
    txt6.grid(column=1, row=3)
    txt6.insert(0, personal["date"])

    lbl2 = Label(window1, text="Address:", bg="LightYellow3", font=("Arial Bold", 14), width=15)
    lbl2.grid(column=0, row=4)
    txt2 = Entry(window1, width=32, font=("Arial Bold", 20))
    txt2.grid(column=1, row=4, columnspan=3)
    txt2.insert(0, personal["address"])

    lbl3 = Label(window1, text="Phone Number:", bg="LightYellow3", font=("Arial Bold", 14), width=15)
    lbl3.grid(column=0, row=5)
    txt3 = Entry(window1, width=32, font=("Arial Bold", 20))
    txt3.grid(column=1, row=5, columnspan=4)
    txt3.insert(0, personal["phone"])

    gender_frame = LabelFrame(window1, text='Gender', bg="LightYellow3", padx=15, pady=15)
    gender_frame.grid(column=0, row=6)
    rad_var = StringVar(master=window1)
    rad_var.set(personal["gender"])
    rad1 = Radiobutton(gender_frame, text='Male   ', value='Male', bg="LightYellow3", variable=rad_var)
    rad2 = Radiobutton(gender_frame, text='Female', value='Female', bg="LightYellow3", variable=rad_var)
    rad1.grid(column=0, row=0)
    rad2.grid(column=0, row=1)

    typframe = LabelFrame(window1, text='Type', bg="LightYellow3", padx=15, pady=15)
    typframe.grid(column=1, row=6)
    rad_var2 = StringVar(master=window1)
    rad_var2.set(personal["person_type"])
    rad3 = Radiobutton(typframe, text='Employee   ', value='Employee', bg="LightYellow3", variable=rad_var2)
    rad4 = Radiobutton(typframe, text='Manager     ', value='Manager', bg="LightYellow3", variable=rad_var2)
    rad3.grid(column=0, row=0)
    rad4.grid(column=0, row=1)

    etcframe = LabelFrame(window1, bg="LightYellow3", padx=15, pady=15)
    etcframe.grid(column=2, row=6)
    chk_state = StringVar(master=window1)
    chk2_state = StringVar(master=window1)
    chk2_state.set(personal["has_license"])
    chk_state.set(personal["has_car"])

    Checkbutton(etcframe, text='License', bg="LightYellow3", var=chk_state).grid(column=0, row=0)
    Checkbutton(etcframe, text='Car       ', bg="LightYellow3", var=chk2_state).grid(column=0, row=1)

    # save worker___________________
    def save():
        person = {}
        first_name = txt.get()
        last_name = txt1.get()
        address = txt2.get()
        phone = txt3.get()
        person_id = txt4.get()
        date = txt6.get()
        salary = txt5.get()
        person_type = rad_var2.get()
        gender = rad_var.get()
        has_license = int(chk_state.get()) == 1
        has_car = int(chk2_state.get()) == 1

        # adding all to dict
        person["first_name"] = first_name
        person["last_name"] = last_name
        person["address"] = address
        person["date"] = date
        person["salary"] = salary
        person["phone"] = phone
        person["person_id"] = person_id
        person["person_type"] = person_type
        person["gender"] = gender
        person["has_license"] = has_license
        person["has_car"] = has_car

        # checking for vaild data
        if len(person_id) != 9:
            mb.showerror("Error", "ID must be 9 digits")
            return
        elif len(first_name) == 0:
            mb.showerror("Error", "must enter first name")
            return
        elif len(last_name) == 0:
            mb.showerror("Error", "must enter last name")
            return
        elif len(address) == 0:
            mb.showerror("Error", "must enter address")
            return
        elif len(date) == 0:
            mb.showerror("Error", "must enter date")
            return
        elif len(phone) < 7:
            mb.showerror("Error", "phone num must be at least 7 digits")
            return
        elif len(salary) == 0:
            mb.showerror("Error", "must enter salary")
            return

        try:
            int(salary)
        except:
            mb.showerror("Error", "salary must be a number")
            return

        try:
            int(phone)
        except:
            mb.showerror("Error", "phone must be a number")
            return

        if edit:
            # if edit mode then return to list and update data
            mb.showinfo("Success", "Person saved!")
            personal_cards[index] = person
            refresh_data()
            back_to_menu()

        else:
            # add to data
            mb.showinfo("Success", "Person saved!")
            add_to_data(person)

    # buttons________________________________

    btn = Button(window1, text="Save", command=save, font=("Helvetica Bold", 18), bg="LightYellow3", padx=60)
    btn2 = Button(window1, text="Exit", command=back_to_menu, font=("Helvetica Bold", 18), bg="LightYellow3", padx=60)
    btn3 = Button(window1, text="Back", command=back_to_menu, font=("Helvetica Bold", 18), bg="LightYellow3", padx=60)
    btn.place(x=50, y=400)
    btn2.place(x=300, y=400)
    btn3.place(x=550, y=400)
    window1.mainloop()


# sorted list_____________________
def clicked1():
    open_list(sorted(personal_cards, key=lambda x: int(x["salary"]), reverse=True), False, "Sorted Workers")


# veiw list_______________________
def clicked2():
    open_list(personal_cards, False, "Workers")


# edit list________________________
def clicked3():
    open_list(personal_cards, True, "Edit Worker")


# shows the list of persons_________________
def open_list(persons, with_edit, name):
    global opened
    if opened:
        return
    opened = True

    root = Tk()
    root.title(name)

    def close():
        global opened
        opened = False
        root.destroy()

    root.geometry('900x500')
    root.configure(bg="LightYellow3")
    root.protocol("WM_DELETE_WINDOW", close)

    listbox = Listbox(root)

    listbox.pack(side=LEFT, fill=BOTH)
    listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    listbox.configure(bg="LightYellow3")

    scrollbar = Scrollbar(root)

    scrollbar.pack(side=RIGHT, fill=BOTH)

    # show all the persons in the list_____________________
    for value in persons:
        str1 = value['first_name'] + " " + value['last_name'] + ",   ID:" + value["person_id"] + ",   Role:" + value[
            "person_type"] + ",   Salary:" + value["salary"] + ",   gender: " + value["gender"] + ",   Birthdate: " \
               + value["date"] + ",   Address: " + value["address"] + ",   Phone:" + value["phone"]

        if value["has_car"]:
            str1 += ",   Has Car"
        if value["has_license"]:
            str1 += ",   Has License"
        listbox.insert(END, str1)

    listbox.config(yscrollcommand=scrollbar.set)

    scrollbar.config(command=listbox.yview)

    btn3 = Button(root, text="Back", command=close, font=("Helvetica Bold", 18), bg="LightYellow3", padx=60)

    btn3.place(x=550, y=400)

    # if the person is clicked and editing is enabled, open edit window_________
    def callback(event):
        global personal2, edit, index
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            edit = True
            personal2 = personal_cards[index]
            close()
            clicked()

    if with_edit:
        listbox.bind("<<ListboxSelect>>", callback)

    root.mainloop()


# main window___________________________
load_all()
window = Tk()
window.title('Coffee Shop')
window.geometry("800x570")
window.configure(bg='black')

# set Image & Icon_______________________
# p1 = PhotoImage(file='icon.png')
# window.iconphoto(False, p1)
# myImage = ImageTk.PhotoImage(Image.open('coffee.jpg'))
# labelImg = Label(window, image=myImage).place(x=0, y=0)

Button(window, text='Worker card', font=('Arial Blod', 14), command=clicked, width=11, padx=15).place(x=20, y=250)
Button(window, text='Sorted Workers', font=('Arial Blod', 14), command=clicked1, width=11, padx=15).place(x=380, y=250)
Button(window, text='Workers', font=('Arial Blod', 14), command=clicked2, width=11, padx=15).place(x=200, y=250)
Button(window, text='Edit Worker', font=('Arial Blod', 14), command=clicked3, width=11, padx=15).place(x=560, y=250)
Button(window, text="Exit", bg='Black', fg='red', font=("Tahoma Bold", 14), command=window.destroy, padx=15).place(
    x=715, y=495)

window.mainloop()
