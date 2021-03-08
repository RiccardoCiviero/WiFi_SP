import os
import tkinter as tk
from tkinter import ttk

path = os.getenv("APPDATA") +  "\\CoreTech\\options.opt"
user = ""
passwd = ""

#Window definition
root = tk.Tk() 
root.title("Configurazione")
root.geometry('300x140+50-50')
root.resizable(tk.FALSE,tk.FALSE)
root.attributes("-topmost", 1)
root.iconbitmap("coretech_logo_icona.ico")

def buttonOk_handler():
    user = userEntry.get()
    passwd = passwdEntry.get()
    with open(path, "w") as opt_file:
        opt_file.writelines([user, "\n", passwd])
    root.quit()

def buttonClear_handler():
    userEntry.delete(0, tk.END)
    passwdEntry.delete(0, tk.END)

#Username:
username = tk.StringVar()
userEntry = ttk.Entry(root, width=35, textvariable=username)
userEntry.grid(column=2, row=1, sticky=('W', 'E'), padx=5, pady=15, columnspan=2)

#Password:
password = tk.StringVar()
passwdEntry = ttk.Entry(root, width=35, textvariable=password)
passwdEntry.grid(column=2, row=2, sticky=('W', 'E'), padx=5, pady=5, columnspan=2)

#Label Username:
userLabel = ttk.Label(text="Username:")
userLabel.grid(column=1, row=1, sticky=('W', 'E'), padx=5, pady=15)

#Label Password:
passwdLabel = ttk.Label(text="Password:")
passwdLabel.grid(column=1, row=2, sticky=('W', 'E'), padx=5, pady=5)

#Pulsante Ok:
buttonOk = ttk.Button(root, text="Ok", command=buttonOk_handler)
buttonOk.grid(row=3, column=2, padx=33, pady=15, sticky=('W'))

#Pulsante Clear:
buttonClear = ttk.Button(root, text="Clear", command=buttonClear_handler)
buttonClear.grid(row=3, column=3, pady=15, sticky=('W'))

root.mainloop()
