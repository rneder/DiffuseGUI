import tkinter as tk
from tkinter import ttk
from discus_convert import *

def discus_rad_menu(parent, nwave, radiation, wvle, ener, ElementNumber, 
                    adp, ano, pos_row, pos_col):
        
        parent.label_rad = ttk.Label(parent, text='Radiation:')
        parent.rad_type = tk.IntVar()
        parent.rad_type.set(0)
        parent.wvle = tk.StringVar()
        parent.wvle.set(str(wvle))
        parent.ener = tk.StringVar()
        parent.ener.set(str(ener))
        parent.rad = tk.Listbox(parent, height=3, width=10, 
                selectbackground=COLORS.en_back,
                selectforeground=COLORS.en_fore, selectmode=tk.SINGLE
                )
        parent.rad.configure(exportselection=False)
        parent.rad.insert(1, 'X-ray')
        parent.rad.insert(2, 'neutron')
        parent.rad.insert(3, 'electron')
        parent.rad.selection_set(radiation)
        #
        parent.label_wvl = ttk.Label(parent, text='Wavelength')
        parent.R0 = tk.Radiobutton(parent, text='Element    ',
                variable=parent.rad_type, value=2,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front, 
                justify='left',
                command=lambda: convert_setup(parent, 3)
                )
        parent.R1 = tk.Radiobutton(parent, text='Wave length',
                variable=parent.rad_type, value=0,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front, 
                justify='left',
                command=lambda: convert_setup(parent, 1)
                )
        parent.R2 = tk.Radiobutton(parent, text='Energy',
                variable=parent.rad_type, value=1,
                activeforeground=COLORS.ok_active, foreground=COLORS.ok_front, 
                justify='left',
                command=lambda: convert_setup(parent,-1)
                )
        #
        parent.yScroll = tk.Scrollbar(parent, orient=tk.VERTICAL)
        parent.ele = tk.Listbox(parent, height=1, width= 5,
                selectbackground=COLORS.en_back,
                selectforeground=COLORS.en_fore, selectmode=tk.SINGLE,
                yscrollcommand=parent.yScroll.set
                )
        parent.yScroll['command'] = parent.ele.yview
        parent.ele.configure(exportselection=False)
        for i in range(nwave):
            parent.ele.insert(i, parent.symbols[i])
        parent.ele.selection_set(20)
        parent.ele.yview_scroll(20, tk.UNITS)
        parent.label_wvle_unit = tk.Label(parent, text='Ang')
        if parent.rad_type.get() == 1:
            parent.label_ener_unit = tk.Label(parent,text='meV')
        else:
            parent.label_ener_unit = tk.Label(parent,text='keV')
        parent.entry_wvle = ttk.Entry(parent,textvariable=parent.wvle, 
                 width=10, justify='right', foreground=COLORS.en_fore
                 )
        parent.entry_ener = ttk.Entry(parent,textvariable=parent.ener, 
                 width=10, justify='right', foreground=COLORS.en_fore
                 )
        #
        # Bind events to Radiation related widgets
        #
        parent.rad.bind('<ButtonRelease-1>', lambda eff: convert_event(eff, parent, 1))
        parent.ele.bind('<ButtonRelease-1>', lambda eff: convert_element(eff, parent, 0))
        parent.entry_wvle.bind('<FocusOut>', lambda eff: convert_focus(eff, parent, 0))
        parent.entry_wvle.bind('<Leave>',    lambda eff: convert_focus(eff, parent, 0))
        parent.entry_ener.bind('<FocusOut>', lambda eff: convert_focus(eff, parent, 0))
        parent.entry_ener.bind('<Leave>',    lambda eff: convert_focus(eff, parent, 0))
        #
        # If an Element name was given, make this active
        if ElementNumber > -1:
            parent.ele.configure(state='normal')
            parent.entry_wvle.configure(state='disabled', foreground=COLORS.dis_fore)
            parent.entry_ener.configure(state='disabled', foreground=COLORS.dis_fore)
            parent.rad_type.set(2)
        else:
            parent.ele.configure(state='disabled')
            parent.entry_wvle.configure(state='normal', foreground=COLORS.en_fore)
            parent.entry_ener.configure(state='disabled', foreground=COLORS.dis_fore)
            parent.rad_type.set(0)
        #
        parent.adp = tk.IntVar()
        parent.adp.set(adp)
        parent.label_adp = ttk.Label(parent, text='ADP:')
        parent.check_adp = ttk.Checkbutton(parent, text='Use',variable=parent.adp)
        #
        parent.ano = tk.IntVar()
        parent.ano.set(ano)
        parent.label_ano = ttk.Label(parent, text='anomalous:')
        parent.check_ano = ttk.Checkbutton(parent, text='Use', variable=parent.ano)

        parent.label_rad.grid(      row=pos_row+0, column=pos_col+0, padx=(5,0), sticky='EW')
        parent.rad.grid(            row=pos_row+0, column=pos_col+1, rowspan=3, sticky='EW')
        parent.R0.grid(             row=pos_row+0, column=pos_col+2, sticky='EWNS')
        parent.R1.grid(             row=pos_row+1, column=pos_col+2, sticky='EW')
        parent.R2.grid(             row=pos_row+2, column=pos_col+2, sticky='EW')
        parent.ele.grid(            row=pos_row+0, column=pos_col+3, sticky='EWNS')
        parent.yScroll.grid(        row=pos_row+0, column=pos_col+4, sticky='W')
        parent.entry_wvle.grid(     row=pos_row+1, column=pos_col+3, sticky='EW')
        parent.label_wvle_unit.grid(row=pos_row+1, column=pos_col+4, sticky='W')
        parent.entry_ener.grid(     row=pos_row+2, column=pos_col+3, sticky='EW')
        parent.label_ener_unit.grid(row=pos_row+2, column=pos_col+4, sticky='W')
        #
        parent.label_adp.grid(      row=pos_row+3, column=pos_col+0, padx=(5,0), sticky='EW')
        parent.check_adp.grid(      row=pos_row+3, column=pos_col+1, sticky='EW')
        parent.label_ano.grid(      row=pos_row+4, column=pos_col+0, padx=(5,0), sticky='EW')
        parent.check_ano.grid(      row=pos_row+4, column=pos_col+1, sticky='EW')
