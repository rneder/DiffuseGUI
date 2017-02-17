import tkinter as tk
from tkinter import ttk
from support import COLORS
from exit_button import create_exit_button
from file_stuff import file_open 
from lib_discus_suite import *
from suite_status import suite_status

def exit_command(parent,i):
    i=1
    line = 'exit'
    suite.discus_read_structure(line)

class READ_CELL_FR(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__ ( self, parent )
        self.config(borderwidth=2, relief=tk.RAISED, background=COLORS.fr_read)
        self.grid(row=2,column=0,columnspan=8,sticky='W')

        self.cell_type = tk.IntVar()
        self.cell_type.set(0)
        self.filename = tk.StringVar()
        self.filename.set('Filename undefined')
        self.caption = ttk.Label(self, text='Expand an asymmetric unit from file')
        self.fileb = ttk.Button(self, text='Open',
                command=self.open_file
                )
        self.treat = ttk.Label(self, text='Treat atoms with\nequal names as:')
        self.label_fle = ttk.Label(self, textvariable=self.filename,
                relief=tk.RAISED, foreground='#FF0000'
                )
        self.R1 = tk.Radiobutton(self,text='Equal types ', 
                variable=self.cell_type, value=0,
                activeforeground='#FF0000', foreground='#0000FF'
                )
        self.R2 = tk.Radiobutton(self,text='Sep. types',
                variable=self.cell_type, value=1,
                activeforeground='#FF9900', foreground='#0000FF'
                )
        self.exp = ttk.Label(self, text='Expand to unit cells:')
        self.nx_l = ttk.Label(self, text='NX:')
        self.ny_l = ttk.Label(self, text='NY:')
        self.nz_l = ttk.Label(self, text='NZ:')
        self.nx = tk.Spinbox(self, from_=1, to=1000, width=10,
                background='#FFFFFF', foreground='#0000FF')
        self.ny = tk.Spinbox(self, from_=1, to=1000, width=10,
                background='#FFFFFF', foreground='#0000FF')
        self.nz = tk.Spinbox(self, from_=1, to=1000, width=10,
                background='#FFFFFF', foreground='#0000FF')
        self.acc = ttk.Button(self, text='Run', command=lambda: self.display_file(parent))
        create_exit_button(self, 'discus', 6, 3, exit_command,(parent,0))
        #
        self.caption.grid(row=0, column=0, columnspan=5)
        self.fileb.grid(row=1, column=0)
        self.treat.grid(row=1, column=3)
        self.R1.grid(row=2, column=3, sticky=tk.W)
        self.R2.grid(row=3, column=3, sticky=tk.W)
        self.exp.grid(row=3, column=0, columnspan=2)
        self.nx_l.grid(row=4, column=0)
        self.ny_l.grid(row=5, column=0)
        self.nz_l.grid(row=6, column=0)
        self.nx.grid(row=4, column=1, sticky='W')
        self.ny.grid(row=5, column=1, sticky='W')
        self.nz.grid(row=6, column=1, sticky='W')
        self.acc.grid(row=5, column=3)
        self.label_fle.grid(row=2, column=0, columnspan=3, padx=(10,20), sticky='W')
        self.acc.configure(state='disabled')
        self.nx.configure(state='disabled')
        self.ny.configure(state='disabled')
        self.nz.configure(state='disabled')
        self.R1.configure(state='disabled')
        self.R2.configure(state='disabled')
        line = 'read'
        suite.suite_learn(line)

    def open_file(self):
        file_open(self)
        self.nx.configure(state='normal')
        self.ny.configure(state='normal')
        self.nz.configure(state='normal')
        self.R1.configure(state='normal')
        self.R2.configure(state='normal')


    def display_file(self, parent):
        if self.cell_type.get() == 0:
            cmd = 'cell'
        elif self.cell_type.get() == 1 :
            cmd = 'lcell'
        else :
            cmd = 'cell'
        line = (cmd + ' ' + str(self.filename.get()) + ',' + str(self.nx.get()) +
                            ',' + str(self.ny.get()) + ',' + str(self.nz.get())   )
        suite.discus_read_structure(line)
        parent.b_strumenu.menu.entryconfig(3, state='normal')
        parent.b_strumenu.menu.entryconfig(4, state='normal')
        parent.b_strumenu.menu.entryconfig(6, state='normal')
        parent.b_fourmenu.configure(state='normal')
        suite_status.set(0,1)
        # Close menu
        self.destroy()

class READ_STRU_FR(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__ ( self, parent )
        self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_read)
        self.grid(row=2,column=0,columnspan=8, sticky='W')

        self.cell_type = tk.IntVar()
        self.cell_type.set(0)
        self.filename = tk.StringVar()
        self.filename.set('Filename undefined')
        self.caption=ttk.Label(self, text='Read an old structure from file')
        self.fileb = ttk.Button(self, text='Open',
                   command=lambda: file_open(self))
        self.label_fle = ttk.Label(self, textvariable=self.filename, relief=tk.RAISED)
        self.acc = ttk.Button(self, text='Run', command=lambda: self.display_file(parent))
#       create_exit_button(self,'discus',6,3,create_exit_button.donothing,(0,0))
        create_exit_button(self, 'discus', 6, 3, exit_command,(parent,0))

        self.caption.grid(row=0,column=0, columnspan=5)
        self.fileb.grid(row=1, column=0)
        self.label_fle.grid(row=2, column=0, columnspan=3)
        self.acc.grid(row=5, column=3)
        self.acc.configure(state='disabled')
        line = 'read'
        suite.suite_learn(line)


    def display_file(self, parent):
        line = ('stru' + ' ' + str(self.filename.get()))
        suite.discus_read_structure(line)
        parent.b_strumenu.menu.entryconfig(3,state='normal')
        parent.b_strumenu.menu.entryconfig(4,state='normal')
        parent.b_strumenu.menu.entryconfig(6,state='normal')
        parent.b_fourmenu.configure(state='normal')
        #
        suite_status.set(0,1)
        # Close menu
        self.destroy()

