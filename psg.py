
# Password Generator By Cedric Arts

# Import Necessary Modules/Libraries
import random
import tkinter as tk
from tkinter import ttk, messagebox

# Window Instance
app = tk.Tk()
app.geometry('400x300')
app.title("Password Generator By CA")

# Boolean Variables
char_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
sym_var = tk.BooleanVar()

password = ""

#Function To Generate A Password
def GeneratePassword():

    pass1 = []

    # Executes when characters checkbox is True
    if char_var.get():
        pass1.extend(['a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                      'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                      'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                      'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'H',
                      'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
                      'R', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ])
        
     # Executes when digits checkbox is True
    if digits_var.get():
        pass1.extend(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

     # Executes when symbols checkbox is True
    if sym_var.get():
        pass1.extend(['!', '@', '#', '$', '%', '^', '&', '*', '/', '\\', 
                      ']', '[', '\'', ';', '"', '?', '>', '<', '~', '`',
                      '.', ',', '=', '_', '-', '+', '', '(', ')', '|'])
   
    password = ""

    # For-loop to generate password
    for x in range(entry_length.get()):
        password = password + random.choice(pass1)[0]

    result_label.config(text=f"Your new password is:\n {password}")
    #messagebox.showinfo("Your new password is:", password)

def CopyPassword():
    if password:
        app.clipboard_append(password)  # Append password to clipboard
        result_label.config(text="Password copied to clipboard!")

# Input Widgets
input_frame = ttk.Frame(master = app, )

# Entries
entry_label = ttk.Label(master = input_frame, text = 'Enter length of password:', font = 'Arial 16')
entry_label2 = ttk.Label(master = input_frame, text="Choose your options:", font = 'Arial 16')
entry_length = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable=entry_length)
chkChar = ttk.Checkbutton(master = input_frame, text = "Charaters", variable = char_var)
chkNumber = ttk.Checkbutton(master = input_frame, text = "Digits", variable = digits_var)
chkSym = ttk.Checkbutton(master = input_frame, text = "Symbols", variable = sym_var)

# Buttons
button = ttk.Button(master = input_frame, text = 'Generate', command=GeneratePassword)
button_copy = ttk.Button(master=input_frame, text='Copy Password', command=CopyPassword)
result_label = ttk.Label(master=input_frame, text="", font = 'Arial 12')

# To Display On Window/App
entry_label.pack(pady = 5)
entry.pack(pady = 5)
entry_label2.pack(pady = 5)
chkChar.pack()
chkNumber.pack()
chkSym.pack()
button.pack(side = 'left')
button_copy.pack(side = 'right')
result_label.pack(side = 'bottom')
input_frame.pack(pady = 2)

# Run Application
app.mainloop()