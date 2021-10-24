#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Import modules
from tkinter import Tk, Label, Entry, Scale, Frame, Button, IntVar
from tkinter import StringVar as StrVar
from tkinter import PhotoImage as Ico

# Import sources
import actions as ac
import calc_mem as mem
import utils as ut


# Verify scale state
def state_scale(scale):
    if mem.total_swap() == '0.0B':
        scale.config(state='normal', takefocus=1)
        scale.set(mem.min_mem())
    else:
        scale.set(0)
        scale.config(state='disabled', takefocus=0)


# Verify button state
def state_button(act, deact):
    if mem.total_swap() == '0.0B':
        act['state'] = 'normal'
        deact['state'] = 'disabled'
    else:
        act['state'] = 'disabled'
        deact['state'] = 'normal'


# Main function
def launcher_swapfile():
    main_app = Tk()
    main_app.title('Swap File')
    main_app.resizable(0, 0)

    # Set program icon case function is not None
    ico = ut.set_icon()
    if ico is not None:
        main_app.iconphoto(True, Ico(file=ico))

    # Variables for Entry
    s_min = StrVar()
    s_min.set(mem.min_mem())
    s_rec = StrVar()
    s_rec.set(mem.rec_mem())
    s_max = StrVar()
    s_max.set(mem.max_mem())

    # Variable for Scale
    i_scale = IntVar()

    # Functions for select entry e_min
    # noinspection PyUnusedLocal
    def sel_min(*args):
        main_app.focus()
        scale_mem.set(mem.min_mem())

    # Functions for select entry e_min
    # noinspection PyUnusedLocal
    def sel_rec(*args):
        main_app.focus()
        scale_mem.set(mem.rec_mem())

    # Functions for select entry e_min
    # noinspection PyUnusedLocal
    def sel_max(*args):
        main_app.focus()
        scale_mem.set(mem.max_mem())

    # Frame for memory informations
    frame_mem = Frame(main_app, borderwidth=2, relief='groove')
    frame_mem.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky='E, W')

    # Frame for Scale
    frame_scale = Frame(main_app, borderwidth=2, relief='groove')
    frame_scale.grid(row=1, column=0, padx=(5, 5), pady=(0, 5), sticky='E, W')

    # Frame for Buttons
    frame_button = Frame(main_app)
    frame_button.grid(row=2, column=0)

    # For minimal recommended
    Label(frame_mem, text='Minimal recommended:').grid(row=0, column=0, padx=(20, 10), pady=(12, 5), sticky='E')
    Label(frame_mem, text='MB').grid(row=0, column=2, pady=(12, 5), sticky='W')
    e_min = Entry(frame_mem, width=12, justify='right', fg='#000', textvariable=s_min)
    e_min.config(readonlybackground='#fff', state='readonly')
    e_min.bind('<FocusIn>', sel_min)
    e_min.grid(row=0, column=1, pady=(12, 5))

    # For recommended
    Label(frame_mem, text='Recommended:').grid(row=1, column=0, padx=(20, 10), pady=5, sticky='E')
    Label(frame_mem, text='MB').grid(row=1, column=2, pady=5, sticky='W')
    e_rec = Entry(frame_mem, width=12, justify='right', fg='#000', textvariable=s_rec)
    e_rec.config(readonlybackground='#fff', state='readonly')
    e_rec.bind('<FocusIn>', sel_rec)
    e_rec.grid(row=1, column=1, pady=5)

    # For maximum recommended
    Label(frame_mem, text='Maximum recommended:').grid(row=2, column=0, padx=(20, 10), pady=5, sticky='E')
    Label(frame_mem, text='MB').grid(row=2, column=2, padx=(0, 20), pady=5, sticky='W')
    e_max = Entry(frame_mem, width=12, justify='right', fg='#000', textvariable=s_max)
    e_max.config(readonlybackground='#fff', state='readonly')
    e_max.bind('<FocusIn>', sel_max)
    e_max.grid(row=2, column=1, pady=5)

    # Scale for select the amount of RAM memory
    Label(frame_scale, text='Select the amount of RAM memory:').grid(row=0, column=0, padx=10, pady=(12, 5), sticky='W')
    scale_mem = Scale(frame_scale, from_=16, to=mem.max_mem(), orient='horizontal', length=320, variable=i_scale)
    scale_mem.grid(row=1, column=0, padx=10, pady=(0, 10))
    state_scale(scale_mem)

    # Buttons for options
    b_active = Button(frame_button, text='Active', width=8, command=lambda: {ac.active(main_app, i_scale.get(), status),
                                                                             state_button(b_active, b_deactive),
                                                                             state_scale(scale_mem)})
    b_active.grid(row=0, column=0, padx=2, pady=(0, 5))

    b_deactive = Button(frame_button, text='Deactive', width=8, command=lambda: {ac.deactive(main_app, status),
                                                                                 state_button(b_active, b_deactive),
                                                                                 state_scale(scale_mem)})
    b_deactive.grid(row=0, column=1, padx=2, pady=(0, 5))

    b_options = Button(frame_button, text='Options', width=8, command=lambda: ac.options(main_app))
    b_options.grid(row=0, column=2, padx=2, pady=(0, 5))

    b_about = Button(frame_button, text='About', width=8, command=lambda: ac.about(main_app))
    b_about.grid(row=0, column=3, padx=2, pady=(0, 5))

    status = Label(frame_button, text='Status: ' + mem.status_swap())
    status.grid(row=1, column=0, padx=2, pady=5, sticky='W', columnspan=4)

    # Ajust state for Buttons
    state_button(b_active, b_deactive)

    # Others properties
    ut.center(main_app)
    main_app.wait_visibility(main_app)
    main_app.attributes('-alpha', 0.85)
    main_app.mainloop()


# Start application
if __name__ == '__main__':
    launcher_swapfile()
