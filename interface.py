import tkinter as tk
from tkinter import *
import functions
from tkinter import filedialog

class application:
    def __init__(self, mainFrame):
        showPassword = StringVar()
        Label(mainFrame, text="Current Password: ").grid(row=0,column=0)
        Label(mainFrame, textvariable= showPassword).grid(row=0,column=1)
        Label(mainFrame, text="Password: ").grid(row=1,column=0)
        Entry(mainFrame, bd=5, textvariable= showPassword).grid(row=1,column=1)

        input_file_path = StringVar()
        Label(mainFrame, textvariable= input_file_path).grid(row=2,column=0)
        Button(mainFrame, text= "Sources Files", command=(lambda value=input_file_path: value.set(filedialog.askopenfilename()))).grid(row=2,column=1)
        output_file_path = StringVar()
        Label(mainFrame, textvariable=output_file_path).grid(row=3,column=0)
        Button(mainFrame, text="Destination Folder", command=(lambda value=output_file_path: value.set(filedialog.askdirectory()))).grid(row=3,column=1)

        Button(mainFrame, text="encrytion", command= (lambda value=showPassword, source=input_file_path, destination=output_file_path: functions.encrytion(value,source,destination))).grid(row=4,column=0)
        Button(mainFrame, text="dencrytion", command= (lambda value=showPassword, source=input_file_path, destination=output_file_path: functions.decrytion(value, source, destination))).grid(row=4,column=1)

root = tk.Tk()
app = application(root)
root.mainloop()