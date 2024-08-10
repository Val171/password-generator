from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

LIGHT_BLUE = "#ADD8E6"
PINK = "#F13B98"
GREEN = "#68C451"

#WINDOW SETUP

window = Tk()
window.title("Password Generator")
window.config(height=600, width=600, bg=LIGHT_BLUE, padx=50, pady=50)
canvas = Canvas(width=200, height=200,bg=LIGHT_BLUE, highlightthickness=0)
lock = PhotoImage(file="/Users/vrish/Downloads/password-manager-start/logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=2, row=1, padx=20, pady=20)

website = Label(text="Website:", font=("Courier", 12, "bold"), bg=LIGHT_BLUE)
website.grid(column=1, row=2)
website_filler = Entry(width=35)
website_filler.focus()
website_filler.grid(column=2, row=2, columnspan=2, pady=10)

email = Label(text="Email:", font=("Courier", 12, "bold"), bg=LIGHT_BLUE)
email.grid(column=1, row=3)
email_filler = Entry(width=35)
email_filler.grid(column=2, row=3, columnspan=2)

pw = Label(text="Password:", font=("Courier", 12, "bold"), bg=LIGHT_BLUE)
pw.grid(column=1, row=4)
pw_filler = Entry(width=21)
pw_filler.grid(column=2, row=4, columnspan=1)

#THE BRAINS
def generate_pw():
    pw_filler.delete(first=0, last=END)
    # Password Generator
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C',
               'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_let = [choice(letters) for i in range(randint(8, 10))]
    pass_sym = [choice(symbols) for i in range(randint(2, 6))]
    pass_num = [choice(numbers) for i in range(randint(2, 5))]
    pass_list = pass_num + pass_sym + pass_let
    shuffle(pass_list)

    password = "".join(pass_list)
    pw_filler.insert(0, password)
    pyperclip.copy(password)

gen = Button(text="Generate", command=generate_pw, bg=PINK, border=4, font=("Courier", 11), width=8)
gen.grid(column=3, row=4, padx=10, pady=10)


#ADD THE PASSWORD TO FILE

def save():
    web = website_filler.get()
    pw = pw_filler.get()
    em = email_filler.get()

    if len(web) < 3 or len(pw) < 6 or len(em) < 7:
        messagebox.showinfo(title="Error", message="Empty Field(s). Try Again")

    else:
        issok = messagebox.askokcancel(title="Info entered:", message=f"\nweb:{web}\nemail:{em}\n"
                                     f"password:{pw}")
        if issok is True:
            with open("Passwords", 'a') as pw_file:
                pw_file.write(f"|{web} | {em} | {pw}|\n")
                pw_filler.delete(first=0, last=END)
                website_filler.delete(first=0, last=END)





add =  Button(text="Add", command=save, bg=GREEN, border=4, font=("Courier", 11), width=36)
add.grid(column=2, row=5, padx=5, pady=5, columnspan=2)





window.mainloop()

