import os
import tkinter as tk

path = os.getenv("APPDATA") +  "\\CoreTech\\options.opt"
user = ""
passwd = ""

window = tk.Tk()


def buttonOk_handler(event):
    user = userEntry.get()
    passwd = passwdEntry.get()
    with open(path, "w") as opt_file:
        opt_file.writelines([user, "\n", passwd])
    window.quit()

def buttonClear_handler(event):
    userEntry.delete(0, tk.END)
    passwdEntry.delete(0, tk.END)

title = tk.Label(
    text="CoreTech WiFi",
    bg="cyan"
)
userLabel = tk.Label(
    text="Username:",
    bg="cyan"
)
userEntry = tk.Entry(

)
passwdLabel = tk.Label(
    text="Password:",
    bg="cyan"
)
passwdEntry = tk.Entry(
    
)
buttonOk = tk.Button(
    text="OK"
)
buttonClear = tk.Button(
    text="Clear"
)

# Rendering
title.grid(row=0, columnspan=2)
userLabel.grid(row=1, columnspan=2)
userEntry.grid(row=2, columnspan=2)
passwdLabel.grid(row=3, columnspan=2)
passwdEntry.grid(row=4, columnspan=2)
buttonOk.grid(row=5)
buttonClear.grid(row=5, column=1)

# Wait button ok to get input
buttonOk.bind("<Button-1>", buttonOk_handler)
buttonClear.bind("<Button-1>", buttonClear_handler)

window.mainloop()

