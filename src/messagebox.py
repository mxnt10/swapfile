#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Import tkinter module
import tkinter as tk
import utils as ut

# Global variable for showpass
passwd = None


# Necessary for no interrupt code
def close_msg(win, strvar=None, close=False):
    win.quit()
    win.destroy()
    global passwd
    if strvar is not None:
        passwd = strvar.get()
    if close:
        passwd = (-1)


# Function for view message
def message(win, title, txt, image='', entry=False):
    # No necessary minimize window

    # noinspection PyUnusedLocal
    def on_unmap(*args):
        msg.deiconify()
        msg.focus_force()

    # noinspection PyUnusedLocal
    def enter_entry(*args):
        close_msg(msg, strvar=strvar)

    # noinspection PyUnusedLocal
    def enter(*args):
        close_msg(msg)

    msg = tk.Toplevel()
    msg.wait_visibility(msg)
    msg.attributes('-alpha', 0.0)
    msg.title(title)
    msg.resizable(False, False)

    # Focuses on the window and avoids clicking on the main window
    msg.transient(win)
    msg.focus_force()
    msg.grab_set()

    # Create frame for full organization
    frame = tk.Frame(msg)
    frame.pack()

    # Label logo
    logo = tk.Label(frame, image=image)
    logo.grid(row=0, column=0, pady=(10, 10), padx=(20, 10))

    # Insert options for entry:
    if entry:
        nm = 0
        strvar = tk.StringVar()
        l_entry = tk.Entry(frame, justify='right', show='*', textvariable=strvar)
        l_entry.grid(row=0, column=2, pady=(10, 10), padx=(10, 30))
        l_entry.focus()
        button = tk.Button(msg, text="OK", command=lambda: close_msg(msg, strvar=strvar), width=10)
        msg.bind('<Return>', enter_entry)
    else:
        nm = 30
        button = tk.Button(msg, text="OK", command=lambda: close_msg(msg), width=10)
        msg.bind('<Return>', enter)

    # Create button
    button.pack(pady=(0, 10))

    # Insert text
    text = tk.Label(frame, text=txt, font='-weight bold -size 10')
    text.grid(row=0, column=1, pady=(10, 10), padx=(10, nm))

    ut.center(msg)
    msg.attributes('-alpha', 1.0)
    msg.bind("<Unmap>", on_unmap)  # For not minimize message dialog
    msg.protocol("WM_DELETE_WINDOW", lambda: close_msg(msg, close=True))
    msg.mainloop()


# Dialog for information
def showpass(win, title, text):
    image = '::tk::icons::information'
    message(win, title, text, image=image, entry=True)
    global passwd
    return passwd


# Dialog for error
def showerror(win, title, text):
    image = '::tk::icons::error'
    message(win, title, text, image=image)
