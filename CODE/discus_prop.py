import tkinter as tk
from tkinter import ttk
from exit_button import create_exit_button
from support import *
from lib_discus_suite import *

def exit_command(parent,i):
    i=1

class prop_gui(tk.Frame):
    def __init__(self, parent, sub_menu, pos_row, pos_col):
        tk.Frame.__init__ ( self, parent )
        self.config(borderwidth=4, relief=tk.RAISED, background=COLORS.fr_sub)
        self.grid(row=pos_row,column=pos_col,columnspan=8,sticky='W')
        #
        parent.var_p_all = tk.IntVar()
        parent.var_p_nor = tk.IntVar()
        parent.var_p_mol = tk.IntVar()
        parent.var_p_dom = tk.IntVar()
        parent.var_p_out = tk.IntVar()
        parent.var_p_ext = tk.IntVar()
        parent.var_p_int = tk.IntVar()
        parent.var_p_lig = tk.IntVar()
        parent.var_p_all.set(0)
        parent.var_p_nor.set(0)
        parent.var_p_mol.set(0)
        parent.var_p_dom.set(0)
        parent.var_p_out.set(0)
        parent.var_p_ext.set(0)
        parent.var_p_int.set(0)
        parent.var_p_lig.set(0)
        #
        self.caption=ttk.Label(self, text='Property selection')
        #
        self.label_p_all = ttk.Label(self, text='All props')
        self.r0_p_all = tk.Radiobutton(self, text='ignore',
                variable=parent.var_p_all, value=0,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                command=lambda: self.set_access(parent, 0, 0)
                )
        self.r1_p_all = tk.Radiobutton(self, text='present',
                variable=parent.var_p_all, value=1,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                command=lambda: self.set_access(parent, 0, 1)
                )
        self.r2_p_all = tk.Radiobutton(self, text='absent',
                variable=parent.var_p_all, value=2,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                command=lambda: self.set_access(parent, 0, 2)
                )
        self.r3_p_all = tk.Radiobutton(self, text='individually set', 
                variable=parent.var_p_all, value=3,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                command=lambda: self.set_access(parent, 0, 3)
                )
        #
        self.label_p_nor = ttk.Label(self, text='Atom is normal ')
        self.r0_p_nor = tk.Radiobutton(self, text='ignore',
                variable=parent.var_p_nor, value=0,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        self.r1_p_nor = tk.Radiobutton(self, text='present',
                variable=parent.var_p_nor, value=1,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        self.r2_p_nor = tk.Radiobutton(self, text='absent',
                variable=parent.var_p_nor, value=2,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        #
        self.label_p_mol = ttk.Label(self, text='Atom is in molecule')
        self.r0_p_mol = tk.Radiobutton(self, text='ignore',
                variable=parent.var_p_mol, value=0,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        self.r1_p_mol = tk.Radiobutton(self, text='present',
                variable=parent.var_p_mol, value=1,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        self.r2_p_mol = tk.Radiobutton(self, text='absent',
                variable=parent.var_p_mol, value=2,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        #
        self.label_p_dom = ttk.Label(self, text='Atom is in domain')
        self.r0_p_dom = tk.Radiobutton(self, text='ignore',
                variable=parent.var_p_dom, value=0,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        self.r1_p_dom = tk.Radiobutton(self, text='present',
                variable=parent.var_p_dom, value=1,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        self.r2_p_dom = tk.Radiobutton(self, text='absent',
                variable=parent.var_p_dom, value=2,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        #
        self.label_p_out = ttk.Label(self, text='Atom outside crystal')
        self.r0_p_out = tk.Radiobutton(self, text='ignore',
                variable=parent.var_p_out, value=0,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        self.r1_p_out = tk.Radiobutton(self, text='present',
                variable=parent.var_p_out, value=1,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        self.r2_p_out = tk.Radiobutton(self, text='absent',
                variable=parent.var_p_out, value=2,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        #
        self.label_p_ext = ttk.Label(self, text='Atom at ext. surf.')
        self.r0_p_ext = tk.Radiobutton(self, text='ignore',
                variable=parent.var_p_ext, value=0,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        self.r1_p_ext = tk.Radiobutton(self, text='present',
                variable=parent.var_p_ext, value=1,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        self.r2_p_ext = tk.Radiobutton(self, text='absent',
                variable=parent.var_p_ext, value=2,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        #
        self.label_p_int = ttk.Label(self, text='Atom at int. surf.')
        self.r0_p_int = tk.Radiobutton(self, text='ignore',
                variable=parent.var_p_int, value=0,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        self.r1_p_int = tk.Radiobutton(self, text='present',
                variable=parent.var_p_int, value=1,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        self.r2_p_int = tk.Radiobutton(self, text='absent',
                variable=parent.var_p_int, value=2,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        #
        self.label_p_lig = ttk.Label(self, text='Atom is in ligand')
        self.r0_p_lig = tk.Radiobutton(self, text='ignore',
                variable=parent.var_p_lig, value=0,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        self.r1_p_lig = tk.Radiobutton(self, text='present',
                variable=parent.var_p_lig, value=1,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        self.r2_p_lig = tk.Radiobutton(self, text='absent',
                variable=parent.var_p_lig, value=2,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                justify='left',
                )
        #
#       self.acc = ttk.Button(self, text='Accept', command=lambda: self.set_prop(sub_menu))
        create_exit_button(self, 'discus', 8, 4, exit_command,(parent,0))
        #
        self.caption.grid(row=0,column=0, columnspan=5, pady=(10,10))
        self.label_p_all.grid(row=1, column=0, sticky='EW', pady=(0,10))
        self.r0_p_all.grid(row=1, column=1, pady=(0,10))
        self.r1_p_all.grid(row=1, column=2, pady=(0,10))
        self.r2_p_all.grid(row=1, column=3, pady=(0,10))
        self.r3_p_all.grid(row=1, column=4, pady=(0,10))
        self.label_p_nor.grid(row=2, column=0, sticky='EW')
        self.r0_p_nor.grid(row=2, column=1)
        self.r1_p_nor.grid(row=2, column=2)
        self.r2_p_nor.grid(row=2, column=3)
        self.label_p_mol.grid(row=3, column=0, sticky='EW')
        self.r0_p_mol.grid(row=3, column=1)
        self.r1_p_mol.grid(row=3, column=2)
        self.r2_p_mol.grid(row=3, column=3)
        self.label_p_dom.grid(row=4, column=0, sticky='EW')
        self.r0_p_dom.grid(row=4, column=1)
        self.r1_p_dom.grid(row=4, column=2)
        self.r2_p_dom.grid(row=4, column=3)
        self.label_p_out.grid(row=5, column=0, sticky='EW')
        self.r0_p_out.grid(row=5, column=1)
        self.r1_p_out.grid(row=5, column=2)
        self.r2_p_out.grid(row=5, column=3)
        self.label_p_ext.grid(row=6, column=0, sticky='EW')
        self.r0_p_ext.grid(row=6, column=1)
        self.r1_p_ext.grid(row=6, column=2)
        self.r2_p_ext.grid(row=6, column=3)
        self.label_p_int.grid(row=7, column=0, sticky='EW')
        self.r0_p_int.grid(row=7, column=1)
        self.r1_p_int.grid(row=7, column=2)
        self.r2_p_int.grid(row=7, column=3)
        self.label_p_lig.grid(row=8, column=0, sticky='EW')
        self.r0_p_lig.grid(row=8, column=1)
        self.r1_p_lig.grid(row=8, column=2)
        self.r2_p_lig.grid(row=8, column=3)
#       self.acc.grid(row=7, column=4)
        #
        self.set_access(parent, 0, 0)

    def set_access(self, parent, mode, value):
        if mode == 0:
            if value == 0:
                self.set_radio(parent, value)
                self.dis_en_radio('disabled')
            elif value == 1:
                self.set_radio(parent, value)
                self.dis_en_radio('disabled')
            elif value == 2:
                self.set_radio(parent, value)
                self.dis_en_radio('disabled')
            elif value == 3:
                self.dis_en_radio('normal')
        elif mode == 1:
           parent.var_p_all.set(3)


    def set_radio(self, parent, value):
        parent.var_p_nor.set(value)
        parent.var_p_mol.set(value)
        parent.var_p_dom.set(value)
        parent.var_p_out.set(value)
        parent.var_p_ext.set(value)
        parent.var_p_int.set(value)
        parent.var_p_lig.set(value)

    def dis_en_radio(self, value):
        self.r0_p_nor.configure(state=value)
        self.r0_p_mol.configure(state=value)
        self.r0_p_dom.configure(state=value)
        self.r0_p_out.configure(state=value)
        self.r0_p_ext.configure(state=value)
        self.r0_p_int.configure(state=value)
        self.r0_p_lig.configure(state=value)
        self.r1_p_nor.configure(state=value)
        self.r1_p_mol.configure(state=value)
        self.r1_p_dom.configure(state=value)
        self.r1_p_out.configure(state=value)
        self.r1_p_ext.configure(state=value)
        self.r1_p_int.configure(state=value)
        self.r1_p_lig.configure(state=value)
        self.r2_p_nor.configure(state=value)
        self.r2_p_mol.configure(state=value)
        self.r2_p_dom.configure(state=value)
        self.r2_p_out.configure(state=value)
        self.r2_p_ext.configure(state=value)
        self.r2_p_int.configure(state=value)
        self.r2_p_lig.configure(state=value)

#   def set_prop(self, sub_menu):
#       print(sub_menu)
