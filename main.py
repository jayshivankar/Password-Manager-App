from tkinter import *
from tkinter import messagebox
from random import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for letter in range(randint(8,10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2,4))]
    password_number = [choice(numbers) for num in range(randint(2,4))]

    password_list = password_number+password_symbols+password_letters
    shuffle(password_list)
    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.insert(0,password_list)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_get = website_entry.get()
    username_get = username_entry.get()
    password_get = password_entry.get()
    if len(website_get) == 0 or len(password_get) == 0 or len(username_get) ==0:
        messagebox.showerror(title="Error", message="Please don't leave any feilds empty")
    else:

        is_ok = messagebox.askokcancel(title=website_get,message=f"These are the details entered: \nEmail: {username_get} \nPassword: {password_get}\n Is it ok to save?")
        if is_ok:
            f = open("data.txt", "a")
            f.write(f"Website:{website_get} ,Email:{username_get} ,Password:{password_get}")
            f.write("\n")
            f.close()
            website_entry.delete(0, END)
            username_entry.delete(0,END)
            password_entry.delete(0, END)



def find_password():
    word_to_find = website_entry.get()
    file_path = "data.txt"

    found = False  # Flag to check if the website is found
    with open(file_path, "r") as file:
        for line in file:
            if word_to_find in line:
                found = True
                messagebox.showinfo(title="Found", message=f"Details: {line.strip()}")
                website_entry.delete(0, END)
                break  # Exit the loop once found

    if not found:
        messagebox.showerror(title="Error", message="No such website found.")


#  UI SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0,row=1)

username_label = Label(text="Email/Username: ")
username_label.grid(column=0,row=2)
password_label = Label(text="Password: ")
password_label.grid(column=0,row=3)

website_entry = Entry(width=17)
website_entry.grid(column=1,row=1,)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(column=1,row=2,columnspan=2)
password_entry = Entry(width=17)
password_entry.grid(column=1,row=3)


generate_pass_button = Button(text="Generate Password",command=generate)
generate_pass_button.grid(row=3,column=2)

search_button = Button(text="Search",command=find_password)
search_button.grid(row=1,column=2)


add_button = Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)
window.mainloop()
