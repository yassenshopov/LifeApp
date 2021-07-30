import tkinter as tk
from tkinter import *
import csv
import Initial_Setup

with open('admin_data.csv') as data:
        csv_reader = csv.reader(data, delimiter=',')
        
        i = 0
        for row in csv_reader:
            
            if i == 3:
                if row[0] != "Setup complete":
                    Initial_Setup.Initial_Setup()

            elif i == 1:
                admin_first = row[0]
                admin_last = row[1]
                assistant = row[2]
            
            i += 1


window = tk.Tk()

window.geometry("200x200")


text = "Hello, " + admin_first
greeting = tk.Label(text=text)
greeting.pack()
mainloop()
