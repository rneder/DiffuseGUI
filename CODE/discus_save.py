import tkinter as tk
from tkinter import ttk
import numpy as np
from support import COLORS, is_empty, get_scat
from exit_button import create_exit_button
from file_stuff import file_new 
from discus_prop import * # prop_gui and var_p_*
from lib_discus_suite import *
from suite_status import suite_status

def exit_command(parent,i):
    i=1
    line = 'exit'
    suite.discus_read_structure(line)

class SAVE_STRU_FR(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__ ( self, parent )
        self.config(borderwidth=2, relief=tk.RAISED, background=COLORS.fr_read)
        self.grid(row=2,column=0,columnspan=8,sticky='W')
        #
        self.nscat, self.at_list = get_scat()
        #
        bsavefile, file_length, sel_atom, w_scat, w_ncell, w_mol, w_dom, w_obj, \
                w_gen, w_sym, \
                w_start, w_end, p_all, p_nor, p_mol, p_dom, p_out, p_ext, \
                p_int, p_lig = suite.discus_get_save()
        #
        line = bsavefile.decode()[0]
        for j in range(file_length-1):
            line = line + bsavefile.decode()[j+1]
        self.filename = tk.StringVar()
        if bsavefile.decode() != ' ':
            self.filename.set(line)
        else:
            self.filename.set('Filename undefined')
        self.wr_all  = tk.IntVar()
        self.wr_scat = tk.IntVar()
        self.wr_ncell = tk.IntVar()
        self.wr_molec = tk.IntVar()
        self.wr_object = tk.IntVar()
        self.wr_domain = tk.IntVar()
        self.wr_gener = tk.IntVar()
        self.wr_symme = tk.IntVar()
        #
        self.var_p_all = tk.IntVar()
        self.var_p_nor = tk.IntVar()
        self.var_p_mol = tk.IntVar()
        self.var_p_dom = tk.IntVar()
        self.var_p_out = tk.IntVar()
        self.var_p_ext = tk.IntVar()
        self.var_p_int = tk.IntVar()
        self.var_p_lig = tk.IntVar()
        #
        self.var_sel_all = tk.IntVar()
        self.var_sel_atoms = np.ones((self.nscat+1))
        self.var_sel_all.set(1)
        self.atom_check = []
        for i in range(self.nscat+1):
            number=tk.IntVar()
            number.set(1)
            self.atom_check.append(number)
            print(' SELECT ATOM ? ' + str(i) + ' ' + str(self.atom_check[i].get()))
        #
        if w_scat==1 and w_ncell==1 and w_mol==1 and w_dom==1 and w_obj==1 \
                and w_gen==1 and w_sym==1:
            self.wr_all.set(1)
        else:
            self.wr_all.set(0)
        self.wr_scat.set(w_scat)
        self.wr_ncell.set(w_ncell)
        self.wr_molec.set(w_mol)
        self.wr_domain.set(w_dom)
        self.wr_object.set(w_obj)
        self.wr_gener.set(w_gen)
        self.wr_symme.set(w_sym)
        self.var_p_all.set(p_all)
        self.var_p_nor.set(p_nor)
        self.var_p_mol.set(p_mol)
        self.var_p_dom.set(p_dom)
        self.var_p_out.set(p_out)
        self.var_p_ext.set(p_ext)
        self.var_p_int.set(p_int)
        self.var_p_lig.set(p_lig)
        #
        typestring = 'DISCUS files'
        typeext    = '*.cell *.stru *.CELL *.STRU'
        self.caption=ttk.Label(self, text='Save a structure to file')
        self.fileb = ttk.Button(self, text='Save as:',
                   command=lambda: file_new(self, typestring, typeext))
        self.label_fle = ttk.Label(self, textvariable=self.filename, 
                   foreground=COLORS.ok_active, relief=tk.RAISED)
        #
        self.sub_menu = 'save'
        self.sel_at = ttk.Button(self, text='Select Atom types',
                   command=lambda: atsel_gui(self, self.sub_menu, 3, 4))
        self.propb = ttk.Button(self, text='Properties',
                   command=lambda: prop_gui(self, self.sub_menu, 3, 4))
        self.keywd = ttk.Button(self, text='Keywords',
                   command=lambda: key_gui(self, self.sub_menu, 4, 4))
        #
        self.show = ttk.Button(self, text='Show', command=lambda: self.do_show(parent))
        self.acc = ttk.Button(self, text='Run', command=lambda: self.do_save(parent))
        create_exit_button(self, 'discus', 8, 4, exit_command,(parent,0))

        self.caption.grid(row=0,column=0, columnspan=5, pady=(10,10))
        self.fileb.grid(row=1, column=0)
        self.label_fle.grid(row=2, column=0, columnspan=4, sticky='W')
        self.sel_at.grid(row=3, column=0, columnspan=1, pady=(10,0))
        self.propb.grid(row=3, column=2, columnspan=1, pady=(10,0))
        self.keywd.grid(row=4, column=2, columnspan=1, pady=(10,0))
        self.show.grid(row=6, column=4)
        self.acc.grid(row=7, column=4)
        if self.filename.get == 'Filename undefined':
            self.acc.configure(state='disabled')
        else:
            self.acc.configure(state='normal')
        line = 'save'
        suite.suite_learn(line)

    def do_save(self, parent):
        self.send_save(self)
        line = 'run'
        suite.discus_run_save(line)
        #
        suite_status.set(0,1)
        # Close menu
        self.destroy()

    def do_show(self, parent):
        self.send_save(self)
        line = 'show'
        suite.discus_run_save(line)

    def send_save(self, parent):
        line = ('outf ' + str(self.filename.get()))
        suite.discus_run_save(line)
        self.send_write(self.wr_scat.get(),   'scat')
        self.send_write(self.wr_scat.get(),   'adp')   # ADP is linked to scat!!!
        self.send_write(self.wr_ncell.get(),  'ncell')
        self.send_write(self.wr_molec.get(),  'molec')
        self.send_write(self.wr_domain.get(), 'domain')
        self.send_write(self.wr_object.get(), 'object')
        self.send_write(self.wr_gener.get(),  'gener')
        self.send_write(self.wr_symme.get(),  'symme')
        print('NORMAL   ', self.var_p_nor.get())
        print('Molecule ', self.var_p_mol.get())
        print('Domain   ', self.var_p_mol.get())
        #
        line = 'des all'
        suite.discus_run_save(line)
        for i in range(self.nscat+1):
            if self.atom_check[i].get() == 1:
               line = 'sel ' + str(i)
            else:
               line = 'des ' + str(i)
            suite.discus_run_save(line)

    def send_write(self, value, string):
        if value == 1:
            line = 'write '  + string
            suite.discus_run_save(line)
        else:
            line = 'omit ' + string
            suite.discus_run_save(line)

def exit_subframe(parent,i):
    i=1

class atsel_gui(tk.Frame):
    def __init__(self, parent, sub_menu, pos_row, pos_col):
        tk.Frame.__init__ ( self, parent )
        self.config(borderwidth=4, relief=tk.RAISED, background=COLORS.fr_sub)
        self.grid(row=pos_row,column=pos_col,columnspan=8,sticky='W')
        #
        self.caption = ttk.Label(self, text='Atom type selection')
        self.all = ttk.Checkbutton(self, text='Select all types',
                variable = parent.var_sel_all)
        self.all.bind('<ButtonRelease-1>',
            lambda eff: self.press_all(eff, parent)
            ) 
        create_exit_button(self, 'discus', 1, 2, exit_subframe,(parent,0))
        #
        atom_list = []
        for i in range(parent.nscat+1):
            line = 'Type no. ' + str(i) + ' = ' + parent.at_list[i]
            cb = ttk.Checkbutton(self, text=line, variable=parent.atom_check[i])
            cb.bind('<ButtonRelease-1>',
                lambda eff: self.press_one(eff, parent)
                ) 
            atom_list.append(cb)
            cb.grid(row=2+i, column=0, sticky='EW')
            
        self.caption.grid(row=0,column=0, columnspan=5, pady=(10,10))
        self.all.grid(row=1,column=0, pady=(0,10), sticky='W')

    def press_all(self, eff=None, parent=0):
        j = 1 - int(parent.var_sel_all.get())
        for i in range(parent.nscat+1):
            parent.atom_check[i].set(j)
    def press_one(self, eff=None, parent=0):
        parent.var_sel_all.set(0)

class key_gui(tk.Frame):
    def __init__(self, parent, sub_menu, pos_row, pos_col):
        tk.Frame.__init__ ( self, parent )
        self.config(borderwidth=4, relief=tk.RAISED, background=COLORS.fr_sub)
        self.grid(row=pos_row,column=pos_col,columnspan=8,sticky='W')
        #
        self.caption=ttk.Label(self, text='Keyword selection')
        self.label_all  = ttk.Label(self, text='All values')
        self.check_all  = ttk.Checkbutton(self, text='Write', variable=parent.wr_all)
        self.label_scat = ttk.Label(self, text='scat/ADP')
        self.check_scat = ttk.Checkbutton(self, text='Write', variable=parent.wr_scat)
        self.label_ncell= ttk.Label(self, text='ncell')
        self.check_ncell= ttk.Checkbutton(self, text='Write', variable=parent.wr_ncell)
        self.label_molec= ttk.Label(self, text='Molecules')
        self.check_molec= ttk.Checkbutton(self, text='Write', variable=parent.wr_molec)
        self.label_domain=ttk.Label(self, text='Domains')
        self.check_domain=ttk.Checkbutton(self, text='Write', variable=parent.wr_domain)
        self.label_object= ttk.Label(self, text='Objects')
        self.check_object= ttk.Checkbutton(self, text='Write', variable=parent.wr_object)
        self.label_gener= ttk.Label(self, text='Generators')
        self.check_gener= ttk.Checkbutton(self, text='Write', variable=parent.wr_gener)
        self.label_symme= ttk.Label(self, text='Symmetry')
        self.check_symme= ttk.Checkbutton(self, text='Write', variable=parent.wr_symme)
        create_exit_button(self, 'discus', 8, 4, exit_subframe,(parent,0))
        #
        self.caption.grid(row=0,column=0, columnspan=5, pady=(10,10))
        self.label_all.grid(row=4, column=0, sticky='EW')
        self.check_all.grid(row=4, column=1)
        self.label_scat.grid(row=5, column=0, sticky='EW')
        self.check_scat.grid(row=5, column=1)
        self.label_ncell.grid(row=6, column=0, sticky='EW')
        self.check_ncell.grid(row=6, column=1)
        self.label_molec.grid(row=7, column=0, sticky='EW')
        self.check_molec.grid(row=7, column=1)
        self.label_domain.grid(row=8, column=0, sticky='EW')
        self.check_domain.grid(row=8, column=1)
        self.label_object.grid(row=9, column=0, sticky='EW')
        self.check_object.grid(row=9, column=1)
        self.label_gener.grid(row=10, column=0, sticky='EW')
        self.check_gener.grid(row=10, column=1)
        self.label_symme.grid(row=11, column=0, sticky='EW')
        self.check_symme.grid(row=11, column=1)

