#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Import modules
import logging as log
import subprocess as sh
import os

# Import sources
import messagebox as msgbox


# Verify if password is valid
def pass_root(win):
    passwd = None  # It's returned None for root user
    if os.geteuid() != 0:
        loop = 1
        while loop != 0:
            passwd = msgbox.showpass(win, 'Authentication required', 'Root password:')
            if passwd != (-1):
                com = get_local('get_root') + ' ' + passwd
                op = sh.run(com, shell=True)
                exitcode = getattr(op, 'returncode')
                loop = exitcode
                if exitcode != 0:
                    msgbox.showerror(win, 'Error', 'Invalid Password!')
            else:
                loop = 0  # Return 0 if password in None or window as closed.
    return passwd


# Search for files
def get_local(file):
    get_file = '/usr/share/swapfile/utils/' + file
    l_get_file = '../utils/' + file

    try:
        with open(get_file):
            return get_file
    except Exception as msg:
        log.warning("\033[33m %s.\033[32m Use a local icon...\033[m", msg)
        return l_get_file


# Define application icon
def set_icon():
    icon = '/usr/share/pixmaps/swapfile.png'
    l_icon = '../appdata/swapfile.png'

    try:
        with open(icon):
            return icon
    except Exception as msg:
        log.warning("\033[33m %s.\033[32m Use a local icon...\033[m", msg)
        try:
            with open(l_icon):
                return l_icon
        except Exception as msg:
            # Exception for icon not found
            log.error("\033[31m %s \033[m", msg)
            return None


# Open application in screen center
def center(win):
    # :param win: the main window or Toplevel window to center

    # Apparently a common hack to get the window size. Temporarily hide the
    # window to avoid update_idletasks() drawing the window in the wrong
    # position.
    win.update_idletasks()  # Update "requested size" from geometry manager

    # define window dimensions width and height
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    # Get the window position from the top dynamically as well as position from left or right as follows
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    # this is the line that will center your window
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # This seems to draw the window frame immediately, so only call deiconify()
    # after setting correct window position
    win.deiconify()
