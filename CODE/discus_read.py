import tkinter as tk
from tkinter import ttk
from support import COLORS, get_spcgr, is_empty
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
                relief=tk.RAISED, foreground=COLORS.ok_active
                )
        self.R1 = tk.Radiobutton(self,text='Equal types ', 
                variable=self.cell_type, value=0,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front
                )
        self.R2 = tk.Radiobutton(self,text='Sep. types',
                variable=self.cell_type, value=1,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front
                )
        self.exp = ttk.Label(self, text='Expand to unit cells:')
        self.nx_l = ttk.Label(self, text='NX:')
        self.ny_l = ttk.Label(self, text='NY:')
        self.nz_l = ttk.Label(self, text='NZ:')
        self.nx = tk.Spinbox(self, from_=1, to=1000, width=10,
                background=COLORS.en_back, foreground=COLORS.ok_front)
        self.ny = tk.Spinbox(self, from_=1, to=1000, width=10,
                background=COLORS.en_back, foreground=COLORS.ok_front)
        self.nz = tk.Spinbox(self, from_=1, to=1000, width=10,
                background=COLORS.en_back, foreground=COLORS.ok_front)
        self.acc = ttk.Button(self, text='Run', command=lambda: self.display_file(parent))
        create_exit_button(self, 'discus', 6, 3, exit_command,(parent,0))
        #
        self.caption.grid(row=0, column=0, columnspan=5, pady=(10,10))
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
        typestring = 'DISCUS / CIF / CMAKER files'
        typeext    = '*.cell *.stru *.cif *.txt *.CELL *.STRU *.CIF *.TXT'
        file_open(self, typestring, typeext)
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

        self.filename = tk.StringVar()
        self.filename.set('Filename undefined')
        typestring = 'DISCUS / CIF / RMCprofile CMAKER files'
        typeext    = '*.cell *.stru *.cif *.cssr *.txt *.CELL *.STRU *.CIF *.cssr *.TXT'
        self.caption=ttk.Label(self, text='Read an old structure from file')
        self.fileb = ttk.Button(self, text='Open',
                   command=lambda: file_open(self, typestring, typeext))
        self.label_fle = ttk.Label(self, textvariable=self.filename, 
                   foreground=COLORS.ok_active, relief=tk.RAISED)
        self.acc = ttk.Button(self, text='Run', command=lambda: self.display_file(parent))
#       create_exit_button(self,'discus',6,3,create_exit_button.donothing,(0,0))
        create_exit_button(self, 'discus', 6, 3, exit_command,(parent,0))

        self.caption.grid(row=0,column=0, columnspan=5, pady=(10,10))
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

class READ_FREE_FR(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__ ( self, parent )
        self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_read)
        self.grid(row=2,column=0,columnspan=8, sticky='W')
        #  Get Element symbols and characteristic wavelength from DISCUS
        nspcgr, self.spcgr, self.systems = get_spcgr()
        #
        self.para_a = tk.StringVar()
        self.para_b = tk.StringVar()
        self.para_c = tk.StringVar()
        self.para_alpha = tk.StringVar()
        self.para_beta  = tk.StringVar()
        self.para_gamma = tk.StringVar()
        self.spcgr_type = tk.IntVar()
        self.spcgr_name = tk.StringVar()
        self.spcgr_numb = tk.StringVar()
        #
        self.para_a.set('5.0')
        self.para_b.set('5.0')
        self.para_c.set('5.0')
        self.para_alpha.set('90.0')
        self.para_beta.set('90.0')
        self.para_gamma.set('90.0')
        self.spcgr_type.set(0)
        self.spcgr_name.set('P1')
        self.spcgr_numb.set('1')
        #
        self.caption=ttk.Label(self, text='Define an empty arbitrary space')
        self.label_a=ttk.Label(self, text='a')
        self.label_b=ttk.Label(self, text='b')
        self.label_c=ttk.Label(self, text='c')
        self.entry_a = ttk.Entry(self, textvariable=self.para_a, width=10,
                justify='right', foreground=COLORS.en_fore
                )
        self.entry_b = ttk.Entry(self, textvariable=self.para_a, width=10,
                justify='right', foreground=COLORS.en_fore
                )
        self.entry_c = ttk.Entry(self, textvariable=self.para_a, width=10,
                justify='right', foreground=COLORS.en_fore
                )
        self.label_alpha = ttk.Label(self, text='alpha')
        self.label_beta  = ttk.Label(self, text='beta')
        self.label_gamma = ttk.Label(self, text='gamma')
        self.entry_alpha = ttk.Entry(self, textvariable=self.para_alpha, width=10,
                justify='right', foreground=COLORS.en_fore
                )
        self.entry_beta  = ttk.Entry(self, textvariable=self.para_beta , width=10,
                justify='right', foreground=COLORS.en_fore
                )
        self.entry_gamma = ttk.Entry(self, textvariable=self.para_gamma, width=10,
                justify='right', foreground=COLORS.en_fore
                )
        self.R0 = tk.Radiobutton(self,text='Space group symbol',
                variable=self.spcgr_type, value=0,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front,
                command=lambda: self.setup_spcgr( 0)
                )
        self.R1 = tk.Radiobutton(self,text='Space group number',
                variable=self.spcgr_type, value=1,
                command=lambda: self.setup_spcgr( 1)
                )
        self.yScroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.lst_spcgr_name = tk.Listbox(self, height=2, width= 5,
                selectbackground=COLORS.en_back,
                selectforeground=COLORS.en_fore, selectmode=tk.SINGLE,
                yscrollcommand=self.yScroll.set
                )
        self.yScroll['command'] = self.lst_spcgr_name.yview
        self.lst_spcgr_name.configure(exportselection=False)
        for i in range(nspcgr):
            self.lst_spcgr_name.insert(i, self.spcgr[i])
        self.lst_spcgr_name.selection_set(1)
        self.lst_spcgr_name.yview_scroll(1, tk.UNITS)

        #self.entry_spcgr_name = ttk.Entry(self, textvariable=self.spcgr_name, width=10,
        #        justify='right', foreground=COLORS.en_fore
        #        )
        self.entry_spcgr_numb = ttk.Entry(self, textvariable=self.spcgr_numb, width=10,
                justify='right', foreground=COLORS.en_fore
                )
        self.label_choice = ttk.Label(self, text='Origin choice')
        self.choice = tk.Spinbox(self, from_=1, to=2, width=3,
                background=COLORS.en_back, foreground=COLORS.ok_front)
        #
        self.acc = ttk.Button(self, text='Run', command=lambda: self.define_free(parent))
        create_exit_button(self, 'discus', 6, 7, exit_command,(parent,0))
        #
        # Grid everything
        self.caption.grid(row=0, column=0, columnspan=5, pady=(10,10))
        self.label_a.grid(row=1, column=0, sticky='EW')
        self.label_b.grid(row=2, column=0, sticky='EW')
        self.label_c.grid(row=3, column=0, sticky='EW')
        self.entry_a.grid(row=1, column=1, sticky='EW')
        self.entry_b.grid(row=2, column=1, sticky='EW')
        self.entry_c.grid(row=3, column=1, sticky='EW')
        self.label_alpha.grid(row=1, column=2, sticky='EW')
        self.label_beta.grid(row=2, column=2, sticky='EW')
        self.label_gamma.grid(row=3, column=2, sticky='EW')
        self.entry_alpha.grid(row=1, column=3, sticky='EW')
        self.entry_beta.grid(row=2, column=3, sticky='EW')
        self.entry_gamma.grid(row=3, column=3, sticky='EW')
        self.R0.grid(row=5, column=0, columnspan=3, sticky=tk.W)
        self.R1.grid(row=6, column=0, columnspan=3, sticky=tk.W)
        self.lst_spcgr_name.grid(row=4, column=3, rowspan=2, sticky='EW')
        self.yScroll.grid(row=4, column=4, rowspan=3, sticky='W')
        self.entry_spcgr_numb.grid(row=6, column=3, sticky='EW')
        self.label_choice.grid(row=5, column=5, sticky='EW')
        self.choice.grid(row=5, column=6, sticky='EW')
        self.acc.grid(row=5, column=7)
        #
        self.setup_spcgr(self.spcgr_type.get())
        self.acc.configure(state='normal')

    def setup_spcgr(self, mode):
        if mode == 0:
            self.lst_spcgr_name.configure(state='normal', foreground=COLORS.en_fore)
            self.entry_spcgr_numb.configure(state='disabled', foreground=COLORS.dis_fore)
        else:
            self.lst_spcgr_name.configure(state='disabled', foreground=COLORS.dis_fore)
            self.entry_spcgr_numb.configure(state='normal', foreground=COLORS.en_fore)

    def define_free(self, parent):
        if self.spcgr_type.get() == 0:
            line = ('free' + ' ' + str(self.para_a.get())
                    + ', ' + str(self.para_b.get())
                    + ', ' + str(self.para_c.get())
                    + ', ' + str(self.para_alpha.get())
                    + ', ' + str(self.para_beta.get())
                    + ', ' + str(self.para_gamma.get())
                    + ', ' + 
                    str(self.spcgr[int(self.lst_spcgr_name.curselection()[0])])
                    )
        elif self.spcgr_type.get() == 1:
            line = ('free' + ' ' + str(self.para_a.get())
                    + ', ' + str(self.para_b.get())
                    + ', ' + str(self.para_c.get())
                    + ', ' + str(self.para_alpha.get())
                    + ', ' + str(self.para_beta.get())
                    + ', ' + str(self.para_gamma.get())
                    + ', ' + str(self.spcgr_numb.get())
                    )
        suite.discus_read_structure(line)
        parent.b_strumenu.menu.entryconfig(3,state='normal')
        parent.b_strumenu.menu.entryconfig(4,state='normal')
        parent.b_strumenu.menu.entryconfig(6,state='normal')
        parent.b_fourmenu.configure(state='normal')
        #
        suite_status.set(0,1)
        # Close menu
        self.destroy()


class READ_IMPORT_FR(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__ ( self, parent )
        self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_read)
        self.grid(row=2,column=0,columnspan=8, sticky='W')
        #
        self.filename = tk.StringVar()
        self.filename.set('Filename undefined')
        self.typestring = 'CIF files'
        self.typeext    = '*.cif *.CIF'
        #
        self.caption=ttk.Label(self, text='Import an external file format')
        #
        self.fileb = ttk.Button(self, text='Open',
                   command=lambda: file_open(self, self.typestring, self.typeext))
        self.label_fle = ttk.Label(self, textvariable=self.filename, 
                   foreground=COLORS.ok_active, relief=tk.RAISED)
        #
        self.yScroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.lst_external = tk.Listbox(self, height=2, width= 5,
                selectbackground=COLORS.en_back,
                selectforeground=COLORS.en_fore, selectmode=tk.SINGLE,
                yscrollcommand=self.yScroll.set
                )
        self.yScroll['command'] = self.lst_external.yview
        self.lst_external.configure(exportselection=False)
        self.lst_external.insert(0, 'CIF')
        self.lst_external.insert(1, 'SHELX')
        self.lst_external.insert(2, 'RMCprofile')
        self.lst_external.insert(3, 'CMAKER')
        self.lst_external.selection_set(0)
        self.lst_external.yview_scroll(0, tk.UNITS)
        #
        self.lst_external.bind('<ButtonRelease-1>', 
                lambda eff: self.convert_external(eff, self))
        #
        self.acc = ttk.Button(self, text='Run', command=lambda: self.do_import())
        create_exit_button(self, 'discus', 6, 7, exit_command,(parent,0))
        #
        # Grid everything
        self.caption.grid(row=0, column=0, columnspan=5, pady=(10,10))
        self.lst_external.grid(row=2, column=0, rowspan=2, sticky='EW')
        self.yScroll.grid(row=1, column=2, rowspan=2, sticky='W')
        self.fileb.grid(row=4, column=0)
        self.label_fle.grid(row=5, column=0, columnspan=3)
        self.acc.grid(row=5, column=7)
        #
        self.acc.configure(state='disabled')

    def convert_external(self, eff=None, event=0):
        if is_empty(self.lst_external.curselection()):
            self.typestring='CIF files'
            self.typeext='*.cif *.CIF'
        else:
            if int(self.lst_external.curselection()[0])==0:
                self.typestring='CIF files'
                self.typeext='*.cif *.CIF'
            elif int(self.lst_external.curselection()[0])==1:
                self.typestring='SHELX files'
                self.typeext='*.ins *.res *.INS *.RES'
            elif int(self.lst_external.curselection()[0])==2:
                self.typestring='RMCprofile files'
                self.typeext='*.cssr *.CSSR'
            elif int(self.lst_external.curselection()[0])==3:
                self.typestring='CMAKER files'
                self.typeext='*.txt *.TXT'

    def do_import(self):
        section_name = 'discus'
        line = 'continue'
        if is_empty(self.lst_external.curselection()):
            i = 0
        else:
            if self.filename.get() != 'Filename undefined':
                if int(self.lst_external.curselection()[0]) == 0:
                   line = 'import cif, ' + str( self.filename.get())
        suite.execute_command(section_name, line)
