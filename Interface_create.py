#!/usr/bin/env python
from tkinter import *
import os
import tkinter.messagebox
import json

if "Pheonix_Save_File/PheonixList" in os.listdir('.'):
    Dict_file = open("Pheonix_Save_File/PheonixList.txt", "r")
    Dict_List = json.load(Dict_file)
else:
    Dict_List = {}

def retrive_input():
    global Dict_List
    inputValue = textBox.get("1.0", "end-1c").split(", ")
    Dict_List.update({inputValue[0]: inputValue[1]})
    text1 = "Show Added, Wanna see the result?"
    answer = tkinter.messagebox.askokcancel("Status", text1)
    if answer == True:
        tkinter.messagebox.showinfo("List", Dict_List)

def save():
    global Dict_List
    if "Pheonix_Save_File" not in os.listdir('.'):
        os.mkdir("Pheonix_Save_File")
    text1 = "You are overwriting old data, all changes "
    text2 = "will be permanent, you wanna contiue?"
    answer_overwrite = tkinter.messagebox.askokcancel("Status", text1 + text2)
    if answer_overwrite == True:
        Saving_file = open("Pheonix_Save_File/PheonixList.txt", "w")
        json.dump(Dict_List, Saving_file)
        Saving_file.close()
        tkinter.messagebox.showinfo("Status", "Save Successful")
    else:
        tkinter.messagebox.showinfo("Status", "Save aborted")

root = Tk()
save_or_quit = Menu(root)
root.config(menu=save_or_quit)

save_or_quit.add_command(label="Save", command=save)
save_or_quit.add_command(label="Quit", command=quit)

textBox= Text(root, height = 2, width= 20)
textBox.pack()

Buttoncommit = Button(root, height=1, width=10, text="Commit",
                        command=lambda: retrive_input())
Buttoncommit.pack()
root.mainloop()
