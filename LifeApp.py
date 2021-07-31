import tkinter as tk
import os
from os import path
from tkinter import *
import csv
from datetime import datetime, date, time, timedelta
import Initial_Setup

#Check if 'admin_data.csv' exists and whether element[4,1] is "Setup complete"

if os.path.exists('admin_data.csv'):
    
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

#Open window at Page 0

window = tk.Tk()

window.geometry("600x600")

title = "👾 " + assistant + " - your personal assistant"
window.title(title)

text = admin_first + "!"
clock_now = datetime.now().strftime('%H:%M')
hour_now = int(clock_now[:2])

if hour_now >= 5 and hour_now <=11:
    text = "Good morning, "  + text
elif hour_now > 11 and hour_now <= 17:
    text = "Good afternoon, " + text
elif hour_now > 17:
    text = "Good evening, " + text
else:
    text = "Hello there, " + text

greeting = tk.Label(text=text)
greeting.pack()

clock_widget = tk.Label(text=clock_now)
clock_widget.pack()

Button(window, text="Quit app", command=window.destroy).pack()

mainloop()
