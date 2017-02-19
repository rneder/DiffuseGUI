import tkinter as tk
from tkinter import ttk
from loop_defs import *
from support import COLORS, CreateToolTip

#
#   This module contains the details for setting up an "if" construction
#
class  if_gui(tk.Frame):
    def __init__(self, parent_frame, parent_menu, prog, mode):
        tk.Frame.__init__ ( self, parent_frame )
        if prog == 'suite':
            self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_read)
            self.grid(row=1, column=0, columnspan=6)
        elif prog == 'discus':
            self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_read)
            self.grid(row=2, column=0, columnspan=6)
        elif prog == 'kuplot':
            self.config(borderwidth=2, relief=tk.RAISED, background=COLORS.fr_read)
            self.grid(row=3, column=0, columnspan=6)
        elif prog == 'diffev':
            self.config(borderwidth=2, relief=tk.RAISED, background=COLORS.fr_read)
            self.grid(row=3, column=0, columnspan=6)

        self.counter   = tk.StringVar()
        self.start     = tk.StringVar()
        self.finish    = tk.StringVar()
        self.increment = tk.StringVar()
        self.counter.set('')
        self.start.set('')
        self.finish.set('')
        self.increment.set('1')
        self.section_name = prog
        self.parent = parent_frame
        self.par_menu = parent_menu

        if mode == 'if_start':
            self.if_start()
        if mode == 'if_else':
            self.if_elseif()
        if mode == 'else':
            self.if_else()
        if mode == 'endif':
            self.if_endif()

    def if_start(self):
        self.l_tit = ttk.Label(self,text = 'If conditional')
        self.l_var = ttk.Label(self,text = 'Condition')
        self.e_var   = tk.Entry(self, textvariable=self.counter, bg=COLORS.en_back)
        self.run     = ttk.Button(self, text='Define Content', 
                command=lambda:self.initiate()
                )
        self.cancel  = ttk.Button(self, text='Exit', command=self.destroy)

#       create_exit_button(self, self.section_name, 4,5,create_exit_button.donothing,(0,0))

        self.l_tit.grid(row=0,column=0,columnspan=2)
        self.l_var.grid(row=1,column=0)
        self.e_var.grid(row=1,column=1)
        self.run.grid(row=2,column=2)
        self.cancel.grid(row=3,column=2)

    def if_elseif(self):
        self.l_tit = ttk.Label(self,text = 'ElseIf conditional')
        self.l_var = ttk.Label(self,text = 'Condition')
        self.e_var   = tk.Entry(self, textvariable=self.counter,
                bg=COLORS.en_back
                )
        self.run     = ttk.Button(self, text='Define Content', 
                command=lambda:self.ifif_elseif()
                )
        self.cancel  = ttk.Button(self, text='Exit', command=self.destroy)

        self.l_tit.grid(row=0,column=0,columnspan=2)
        self.l_var.grid(row=1,column=0)
        self.e_var.grid(row=1,column=1)
        self.run.grid(row=2,column=2)
        self.cancel.grid(row=3,column=2)

    def if_else(self):
        self.l_tit = ttk.Label(self,text = 'Else block')
        self.run     = ttk.Button(self, text='Define Content', 
                command=lambda:self.ifif_else()
                )
        self.cancel  = ttk.Button(self, text='Exit', command=self.destroy)

        self.l_tit.grid(row=0,column=0,columnspan=2)
        self.run.grid(row=1,column=2)
        self.cancel.grid(row=2,column=2)

    def if_endif(self):
        line='endif'
        suite.gui_do_insert(self.section_name,line)
        number = LOOPS.level-1
        LOOPS.set_level(number)
        if LOOPS.level < 0:
            LOOPS.set_lblock_read(False)
            self.par_menu.entryconfig(1, state='disabled')
            self.par_menu.entryconfig(2, state='disabled')
            self.par_menu.entryconfig(3, state='disabled')
            LOOPS.set_level(0)

    def initiate(self):
        global suite_gui_lblock_read
        line = ('if (' + str(self.counter.get()) + ') then' )
        self.par_menu.entryconfig(1, state='normal')
        self.par_menu.entryconfig(2, state='normal')
        self.par_menu.entryconfig(3, state='normal')
        #
        if LOOPS.level == 0 and LOOPS.lblock_read == False:
            suite.gui_do_init(self.section_name, line)
            number = LOOPS.level
            LOOPS.set_lblock_read(True)
            self.destroy()
        else:
            suite.gui_do_insert(self.section_name, line)
            number = LOOPS.level+1
            LOOPS.set_level(number)
            LOOPS.set_lblock_read(True)
            self.destroy()

    def ifif_elseif(self):
        global suite_gui_lblock_read
        line = ('elseif (' + str(self.counter.get()) + ') then' )
        self.par_menu.entryconfig(1, state='normal')
        self.par_menu.entryconfig(2, state='normal')
        self.par_menu.entryconfig(3, state='normal')
        suite.gui_do_insert(self.section_name, line)
        LOOPS.set_lblock_read(True)
        self.destroy()

    def ifif_else(self):
        global suite_gui_lblock_read
        line = ('else')
        self.par_menu.entryconfig(1, state='normal')
        self.par_menu.entryconfig(2, state='normal')
        self.par_menu.entryconfig(3, state='normal')
        suite.gui_do_insert(self.section_name, line)
        LOOPS.set_lblock_read(True)
        self.destroy()
#
#  Build an If SubMenuButton
#
def create_if_submenu(parent,grandpa, prog):
#
    parent.b_if = tk.Menu(parent, tearoff=0)
    parent.b_if.add_command(label='If', 
            command=lambda : if_gui(grandpa, parent.b_if, prog, 'if_start'),
            activeforeground=COLORS.ok_active,
            foreground=COLORS.ok_front,
            background=COLORS.bg_normal, activebackground=COLORS.bg_active 
            )
    parent.b_if.add_command(label='Else if',
            command=lambda : if_gui(grandpa, parent.b_if, prog, 'if_else'),
            activeforeground=COLORS.ok_active,
            foreground=COLORS.ok_front,
            background=COLORS.bg_normal, activebackground=COLORS.bg_active 
            )
    parent.b_if.add_command(label='Else',
            command=lambda : if_gui(grandpa, parent.b_if, prog, 'else'),
            activeforeground=COLORS.ok_active,
            foreground=COLORS.ok_front,
            background=COLORS.bg_normal, activebackground=COLORS.bg_active 
            )
    parent.b_if.add_command(label='Finish If',
            command=lambda : if_gui(grandpa, parent.b_if, prog, 'endif'),
            activeforeground=COLORS.ok_active,
            foreground=COLORS.ok_front,
            background=COLORS.bg_normal, activebackground=COLORS.bg_active 
            )
    parent.b_if.entryconfig(0, state='normal')
    parent.b_if.entryconfig(1, state='disabled')
    parent.b_if.entryconfig(2, state='disabled')
    parent.b_if.entryconfig(3, state='disabled')
    parent.b_if_ttp = CreateToolTip(parent.b_if,\
            'Define conditions that control the execution of command '
            'blocks.')
