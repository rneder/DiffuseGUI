import tkinter as tk
from tkinter import ttk
from support import COLORS
from exit_button import create_exit_button
from file_stuff import file_new 
from lib_discus_suite import *

def exit_command(parent,four_last):
    line = 'exit'
    suite.discus_output(line, four_last)

class DISCUS_OUTPUT_FR(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__ ( self, parent )
        self.config(borderwidth=2, relief=tk.RAISED, background=COLORS.fr_read)
        self.grid(row=2,column=0,columnspan=8,sticky='W')
        #
        four_last = suite.discus_get_four_last()
        #
        self.filename = tk.StringVar()
        self.filename.set('Filename undefined')
        self.caption = ttk.Label(self, text='Write Fourier pattern to disk')
        self.fileb = ttk.Button(self, text='Save as',
                command=lambda: file_new(self)
                )
        self.label_fle = ttk.Label(self, textvariable=self.filename,
                relief=tk.RAISED, foreground=COLORS.warning
                )
        #
        self.label_val = ttk.Label(self, text='Value')
        self.valScroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.val = tk.Listbox(self, height=2, width=15, selectbackground=COLORS.en_back,
                selectforeground=COLORS.ok_front, selectmode=tk.SINGLE,
                yscrollcommand=self.valScroll.set
                )
        self.valScroll['command'] = self.val.yview
        self.val.configure(exportselection=False)
        if four_last > 0 and four_last < 4:  # Standard Fourier 
            self.val_list = ['inten', 'ampl', 'real', 'imag', 'phase', 'f2aver', 'faver2']
            self.val.insert(0, 'Intensity')
            self.val.insert(1, 'Amplitude')
            self.val.insert(2, 'Real part')
            self.val.insert(3, 'Imaginary part')
            self.val.insert(4, 'Phase angle')
            self.val.insert(5, '<form^2>')
            self.val.insert(6, '<form>^2')
        elif four_last < 0 or four_last == 4:  # Lots, zone axis
            self.val_list = ['inten']
            self.val.insert(0,'Intensity')
        elif four_last ==8 or four_last == 9:  # powder
            self.val_list = ['inten', 'S(Q)', 'F(Q)', 'f2aver', 'faver2']
            self.val.insert(0, 'Intensity')
            self.val.insert(1, 'S(Q)')
            self.val.insert(2, 'F(Q)')
            self.val.insert(3, '<form^2>')
            self.val.insert(4, '<form>^2')
        elif four_last > 4 and four_last < 8:  # Patterson Inverse Diff-Four
            self.val_list = ['ampl']
            self.val.insert(0,'Amplitude')
        else:
            self.val_list = ['inten']
            self.val.insert(0,'None')
        self.val.selection_set(0)
        #
        self.label_frm = ttk.Label(self, text='Format')
        self.frmScroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.frm = tk.Listbox(self, height=2, width=10, selectbackground=COLORS.en_back,
                selectforeground=COLORS.en_fore, selectmode=tk.SINGLE,
                yscrollcommand=self.frmScroll.set
                )
        self.frmScroll['command'] = self.frm.yview
        self.frm.configure(exportselection=False)
        if four_last > 0 and four_last < 8:  # Standard Fourier , Zone axis, Patterson
            self.frm_list = ['stan', 'mrc']
            self.frm.insert(0, 'Standard')
            self.frm.insert(1, 'MRC')
        elif four_last == 8 or four_last ==9 :  # Powder
            self.frm_list = ['powder', 'powder, tth', 'powder, q']
            self.frm.insert(0, 'Powder')
            self.frm.insert(1, 'Powder 2Theta')
            self.frm.insert(1, 'Powder Q-scale')
        else:
            self.frm_list = ['stan']
            self.frm.insert(0,'None')
        self.frm.selection_set(0)
        if four_last == 3 or four_last == -3:
            self.frm.selection_set(1)
        #

        self.acc = ttk.Button(self, text='Run', 
                command=lambda: self.write_file(parent, four_last))
#       create_exit_button(self, 'discus', 6, 6, create_exit_button.donothing, (0, 0))
        create_exit_button(self, 'discus', 6, 6, exit_command,(parent,four_last))
        #
        self.caption.grid(  row=0, column=0, columnspan=5, pady=(10,10))
        self.fileb.grid(    row=1, column=0)
        #
        self.label_fle.grid(row=2, column=0, columnspan=5, padx=(10,20), sticky='W')
        self.label_val.grid(row=3, column=0, sticky='EWNS')
        self.val.grid(      row=3, column=1, sticky='EWNS', pady=(5,0))
        self.valScroll.grid(row=3, column=2, sticky='E', pady=(5,0))
        self.label_frm.grid(row=3, column=3, sticky='EWNS', padx=(5,0))
        self.frm.grid(      row=3, column=4, sticky='EWNS', pady=(5,0))
        self.frmScroll.grid(row=3, column=5, sticky='E', pady=(5,0))
        self.acc.grid(      row=5, column=6)
        #
        self.acc.configure(state='disabled')
        #
        line = 'output'
        suite.suite_learn(line)

    def write_file(self, parent, four_last):

        line = ('outf' + ' ' + self.filename.get())
        suite.discus_output(line, four_last)
        line = ('value' + ' ' + self.val_list[int(self.val.curselection()[0]) ] )
        suite.discus_output(line, four_last)
        line = ('form' + ' ' + self.frm_list[int(self.frm.curselection()[0]) ] )
        suite.discus_output(line, four_last)
        line = 'run'
        suite.discus_output(line, four_last)
        line = 'exit'
        suite.discus_output(line, four_last)
        # Close menu
        self.destroy()
