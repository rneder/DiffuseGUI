import tkinter as tk
from tkinter import ttk
from support import control_label, COLORS, command_gui, CreateToolTip
from loop_section import create_loop_submenu
from conditional_section import create_if_submenu

#
#   This module contains all stuff related to command language use
#   Interactive sessions
#   The "command language" button for:
#         sessions
#         a single interactive command
#         loops and if-constructions
#
def suite_session(parent, prog):
    #
    #   despite the (old) name, a generic interface to start an
    #   interactive session
    #
#   turn_off(self.b_command, self.b_macro, self.b_loop, 
#       self.b_if, self.b_help,self.b_exit)
    control_label(parent, 'interactive', prog, 3)
#   turn_on(self.b_command, self.b_macro, self.b_loop,
#       self.b_if, self.b_help,self.b_exit)

def create_command_language(parent, prog, pos_row, pos_col):
    #
    #  The generic command language menu
    #  Can be used from all sections
    #
    parent.b_cmd = tk.Menubutton(parent, text='Command\nlanguage',
        activeforeground=COLORS.ok_active,
        foreground=COLORS.ok_front,
        background=COLORS.bg_normal, activebackground=COLORS.bg_active 
        )
    parent.b_cmd.menu = tk.Menu(parent.b_cmd, tearoff=0)
    parent.b_cmd.configure(menu=parent.b_cmd.menu)
    parent.b_cmd.menu.add_command(label='Interactive session', 
        command=lambda : suite_session(parent, prog),
        activeforeground=COLORS.ok_active,
        foreground=COLORS.ok_front,
        background=COLORS.bg_normal, activebackground=COLORS.bg_active 
        )
    parent.b_cmd.menu.add_command(label='Single Command',
        command=lambda: command_gui(parent, prog),
        activeforeground=COLORS.ok_active,
        foreground=COLORS.ok_front,
        background=COLORS.bg_normal, activebackground=COLORS.bg_active 
        )
    create_loop_submenu(parent.b_cmd, parent, prog)
    parent.b_cmd.menu.add_cascade(label='Loop',
        menu=parent.b_cmd.b_loop,
        activeforeground=COLORS.ok_active,
        foreground=COLORS.ok_front,
        background=COLORS.bg_normal, activebackground=COLORS.bg_active 
        ) 
    create_if_submenu(parent.b_cmd, parent, prog)
    parent.b_cmd.menu.add_cascade(label='Conditionals',
        menu=parent.b_cmd.b_if,
        activeforeground=COLORS.ok_active,
        foreground=COLORS.ok_front,
        background=COLORS.bg_normal, activebackground=COLORS.bg_active 
        ) 
    parent.b_cmd.menu.entryconfig(0,state='normal')
    parent.b_cmd.menu.entryconfig(1,state='normal')
    parent.b_cmd.menu.entryconfig(2,state='normal')
    parent.b_cmd.menu.entryconfig(3,state='normal')
    parent.b_cmd_ttp = CreateToolTip(parent.b_cmd,\
    'Gives access to all command language details.\n'
    'You can switch to a interactive session at the '
    'command prompt, \nstart a GUI for individual '
    'commands,\ndefine and run loops or \ndefine'
    ' conditions for the execution of command(s)\n'
    'Toggle the Advanced mode to activate' 
    )
    parent.b_cmd.grid(row=pos_row, column=pos_col, sticky=tk.W)
