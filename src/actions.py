#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Import modules
from tkinter import Toplevel, Label, Entry, Scale, Frame, Button, IntVar
from tkinter import StringVar as StrVar
import subprocess as sh

# Import sources
import messagebox as msgbox
import calc_mem as mem
import utils as ut


# Active swap in system
def active(win, intvar, st):
    passwd = ut.pass_root(win)
    if passwd != (-1) and passwd is not None:
        act_comm = 'sudo -S -k <<< ' + passwd + ' ' + ut.get_local('active_swap') + ' ' + str(intvar) + 'M'
        sh.run(act_comm, shell=True)
    if passwd is None:
        act_comm = ut.get_local('active_swap') + ' ' + str(intvar) + 'M'
        sh.run(act_comm, shell=True)
    st.config(text='Status: ' + mem.status_swap())


# Deactive swap in system
def deactive(win, st):
    passwd = ut.pass_root(win)
    if passwd != (-1) and passwd is not None:
        act_comm = 'sudo -S -k <<< ' + passwd + ' ' + ut.get_local('deactive_swap')
        sh.run(act_comm, shell=True)
    if passwd is None:
        act_comm = ut.get_local('deactive_swap')
        sh.run(act_comm, shell=True)
    st.config(text='Status: ' + mem.status_swap())


# Define swap priority in system
def apply_swappines(win, intvar):
    passwd = ut.pass_root(win)
    if passwd != (-1) and passwd is not None:
        act_comm = 'sudo -S -k <<< ' + passwd + ' ' + ut.get_local('sysctl_file') + ' ' + str(intvar)
        sh.run(act_comm, shell=True)
    if passwd is None:
        act_comm = ut.get_local('sysctl_file') + ' ' + str(intvar)
        sh.run(act_comm, shell=True)


# Reset swap priority in system
def reset_swappines(win, scale):
    passwd = ut.pass_root(win)
    if passwd != (-1) and passwd is not None:
        act_comm = 'sudo -S -k <<< ' + passwd + ' ' + ut.get_local('sysctl_rst')
        sh.run(act_comm, shell=True)
        scale.config(command='')
        scale.set(mem.get_swappines())
    if passwd is None:
        act_comm = ut.get_local('sysctl_rst')
        sh.run(act_comm, shell=True)
        scale.config(command='')
        scale.set(mem.get_swappines())


# Window for swap options
def options(main):
    # No necessary minimize window
    # noinspection PyUnusedLocal
    def on_unmap(*args):
        op_app.deiconify()
        op_app.focus_force()

    # Active button apply
    # noinspection PyUnusedLocal
    def on_apply(*args):
        b_options['state'] = 'normal'

    # Deactive button apply
    def off_apply():
        b_options['state'] = 'disabled'
        scale_mem.config(command=on_apply)

    op_app = Toplevel()
    op_app.title('Options')
    op_app.resizable(0, 0)

    # Focuses on the window and avoids clicking on the main window
    op_app.transient(main)
    op_app.focus_force()
    op_app.grab_set()

    # Define swappiness value for entry
    swp = StrVar()
    swp.set(mem.get_swappines())

    # Variable for Scale
    i_scale = IntVar()

    # Create frame for swappiness option
    frame = Frame(op_app, borderwidth=2, relief='groove')
    frame.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky='E, W')

    # Create entry for swappiness
    Label(frame, text='Swappiness:').grid(row=0, column=0, padx=(15, 10), pady=(12, 5), sticky='E')
    e_swap = Entry(frame, width=8, justify='right', fg='#000', textvariable=swp)
    e_swap.config(readonlybackground='#fff', state='readonly', highlightthickness=0)
    e_swap.grid(row=0, column=1, padx=(0, 15), pady=(12, 5), sticky='W')

    # Scale for ajust swap option
    scale_mem = Scale(frame, from_=1, to=100, orient='horizontal', length=180, variable=i_scale)
    scale_mem.set(mem.get_swappines())
    scale_mem.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

    # Buttons for options
    b_options = Button(frame, text='Apply', width=8, command=lambda: {apply_swappines(op_app, i_scale.get()),
                                                                      swp.set(mem.get_swappines()),
                                                                      off_apply()})
    b_options.grid(row=2, column=0, padx=2, pady=5)
    off_apply()

    b_reset = Button(frame, text='Reset', width=8, command=lambda: {reset_swappines(op_app, scale_mem),
                                                                    swp.set(mem.get_swappines()),
                                                                    off_apply()})
    b_reset.grid(row=2, column=1, padx=(2, 10), pady=5)

    op_app.bind("<Unmap>", on_unmap)  # For not minimize configuration window
    op_app.wait_visibility(op_app)
    op_app.attributes('-alpha', 0.85)
    op_app.mainloop()


# About application
def about(main):
    msgbox.message(main, 'About', 'SwapFile v1.1 - Swap file manager\n\n'
                                  'Maintainer: Mauricio Ferrari\n'
                                  'Contact: m10ferrari1200@gmail.com\n')
