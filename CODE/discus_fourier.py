import tkinter as tk
import math as math
from tkinter import ttk
from support import *
from exit_button import create_exit_button
from discus_convert import *
from discus_rad_menu import discus_rad_menu
from lib_discus_suite import *


class SINGLE_FOUR_FR(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__ ( self, parent )
        self.config(borderwidth=2, relief=tk.RAISED, background=COLORS.fr_read)
        self.grid(row=2, column=0, columnspan=8, sticky='EW')
#
#       Get Element symbols and characteristic wavelength from DISCUS
        nwave, self.symbols, self.wavelengths = get_wave()
#
#       Get Fourier settings from DISCUS
        corners, increment, radiation, bElement, wvle, ener, adp, ano, \
                percent, lot_type, lot_num, lot_dim, lot_per \
                = suite.discus_get_fourier()
        for i in range(4):
            for j in range(3):
                corners[i,j] = round_rbn(corners[i,j],5)
        wvle = round_rbn(wvle,5)
        ener = round_rbn(ener,5)
#
#       Determine if an element was given for its characteristic radiation
        Element = bElement.decode()
        ElementNumber = -1
        for i in range(nwave):
            if Element == self.symbols[i]:
                ElementNumber = i
                break

        self.ll_h = tk.StringVar()
        self.ll_k = tk.StringVar()
        self.ll_l = tk.StringVar()
        self.lr_h = tk.StringVar()
        self.lr_k = tk.StringVar()
        self.lr_l = tk.StringVar()
        self.ul_h = tk.StringVar()
        self.ul_k = tk.StringVar()
        self.ul_l = tk.StringVar()
        self.tl_h = tk.StringVar()
        self.tl_k = tk.StringVar()
        self.tl_l = tk.StringVar()
        self.ll_h.set(str(corners[0,0]))
        self.ll_k.set(str(corners[0,1]))
        self.ll_l.set(str(corners[0,2]))
        self.lr_h.set(str(corners[1,0]))
        self.lr_k.set(str(corners[1,1]))
        self.lr_l.set(str(corners[1,2]))
        self.ul_h.set(str(corners[2,0]))
        self.ul_k.set(str(corners[2,1]))
        self.ul_l.set(str(corners[2,2]))
        self.tl_h.set(str(corners[3,0]))
        self.tl_k.set(str(corners[3,1]))
        self.tl_l.set(str(corners[3,2]))
        self.caption=ttk.Label(self, text='Single crystal Fourier calculations')
        self.label_h = ttk.Label(self, text='H', anchor='center')
        self.label_k = ttk.Label(self, text='K', anchor='center')
        self.label_l = ttk.Label(self, text='L', anchor='center')
        self.label_ll = ttk.Label(self, text='Lower left')
        self.label_lr = ttk.Label(self, text='Lower right')
        self.label_ul = ttk.Label(self, text='Upper left')
        self.label_tl = ttk.Label(self, text='Top left')
        self.entry_ll_h = ttk.Entry(self, textvariable=self.ll_h, width=8, 
                justify='right', background=COLORS.en_back, foreground=COLORS.en_fore
                )
        self.entry_ll_k = ttk.Entry(self, textvariable=self.ll_k, width=8, 
                justify='right', background=COLORS.en_back, foreground=COLORS.en_fore
                )
        self.entry_ll_l = ttk.Entry(self, textvariable=self.ll_l, width=8, 
                justify='right', background=COLORS.en_back, foreground=COLORS.en_fore
                )
        self.entry_lr_h = ttk.Entry(self, textvariable=self.lr_h, width=8, 
                justify='right', background=COLORS.en_back, foreground=COLORS.en_fore
                )
        self.entry_lr_k = ttk.Entry(self, textvariable=self.lr_k, width=8, 
                justify='right', background=COLORS.en_back, foreground=COLORS.en_fore
                )
        self.entry_lr_l = ttk.Entry(self, textvariable=self.lr_l, width=8, 
                justify='right', background=COLORS.en_back, foreground=COLORS.en_fore
                )
        self.entry_ul_h = ttk.Entry(self, textvariable=self.ul_h, width=8, 
                justify='right', background=COLORS.en_back, foreground=COLORS.en_fore
                )
        self.entry_ul_k = ttk.Entry(self, textvariable=self.ul_k, width=8, 
                justify='right', background=COLORS.en_back, foreground=COLORS.en_fore
                )
        self.entry_ul_l = ttk.Entry(self, textvariable=self.ul_l, width=8, 
                justify='right', background=COLORS.en_back, foreground=COLORS.en_fore
                )
        self.entry_tl_h = ttk.Entry(self, textvariable=self.tl_h, width=8, 
                justify='right', background=COLORS.en_back, foreground=COLORS.en_fore
                )
        self.entry_tl_k = ttk.Entry(self, textvariable=self.tl_k, width=8, 
                justify='right', background=COLORS.en_back, foreground=COLORS.en_fore
                )
        self.entry_tl_l = ttk.Entry(self, textvariable=self.tl_l, width=8, 
                justify='right', background=COLORS.en_back, foreground=COLORS.en_fore
                )
        #
        self.label_np   = ttk.Label(self, text='Points along axis:')
        self.label_np_a = ttk.Label(self, text='Abscissa')
        self.label_np_o = ttk.Label(self, text='Ordinate')
        self.label_np_t = ttk.Label(self, text='Top axis')
        self.np_aa = tk.StringVar()
        self.np_oo = tk.StringVar()
        self.np_tt = tk.StringVar()
        self.np_aa.set(str(increment[0]))
        self.np_oo.set(str(increment[1]))
        self.np_tt.set(str(increment[2]))
        self.np_a = tk.Spinbox(self, from_=1, to=1001,width=8,
                justify='right', textvariable=self.np_aa,
                background=COLORS.en_back, foreground=COLORS.en_fore
                )
        self.np_o = tk.Spinbox(self, from_=1, to=1001,width=8,
                justify='right', textvariable=self.np_oo,
                background=COLORS.en_back, foreground=COLORS.en_fore
                )
        self.np_t = tk.Spinbox(self, from_=1, to=1001,width=8,
                justify='right', textvariable=self.np_tt,
                background=COLORS.en_back, foreground=COLORS.en_fore
                )
        #
        discus_rad_menu(self, nwave, radiation, wvle, ener, ElementNumber, adp, ano, 1, 4)
        #
        #
        self.Aver =tk.StringVar()
        self.Aver.set(percent)
        self.LabelAver =ttk.Label(self, \
                text='Subtract scattering by average structure sampled at')
        self.EntryAver  = ttk.Entry(self, textvariable=self.Aver, width=8,
                justify='right', background=COLORS.en_back, foreground=COLORS.en_fore)
        self.LabelAverPer =ttk.Label(self, text='%')
        #
        #
        self.lot_use = tk.IntVar()
        if lot_type == 0:
            self.lot_use.set(0)
        else :
            self.lot_use.set(1)
        self.label_lot = ttk.Label(self, text='Lots:')
        self.check_lot = ttk.Checkbutton(self, text='Use', variable=self.lot_use)
        self.check_lot.bind('<ButtonRelease-1>', self.lot_event)
        #
        self.label_lotshape =ttk.Label(self, text='Lot Shape:')
        self.lot_shape = tk.Listbox(self, height=2, width=10, selectbackground=COLORS.en_back,
                selectforeground=COLORS.en_fore, selectmode=tk.SINGLE
                )
        self.lot_shape.configure(exportselection=False)
        self.lot_shape.insert(1, 'Box'  )
        self.lot_shape.insert(2, 'Ellipsoid')
        if lot_type == 1 or lot_type==0 :
            self.lot_shape.selection_set(0)
        elif lot_type == 2:
            self.lot_shape.selection_set(1)
        #
        self.label_lotnum   =ttk.Label(self, text='Lot Number:')
        self.lotnn = tk.StringVar()
        self.lotnn.set(str(lot_num))
        self.lotn = tk.Spinbox(self, from_=1, to=1001, width=6, 
                justify='right', textvariable=self.lotnn,
                background=COLORS.en_back, foreground=COLORS.en_fore
                )
        #
        self.label_lotdimx =ttk.Label(self, text='Lot Size X:')
        self.label_lotdimy =ttk.Label(self, text='Lot Size Y:')
        self.label_lotdimz =ttk.Label(self, text='Lot Size Z:')
        self.lotxx = tk.StringVar()
        self.lotxx.set(str(lot_dim[0]))
        self.lotyy = tk.StringVar()
        self.lotyy.set(str(lot_dim[1]))
        self.lotzz = tk.StringVar()
        self.lotzz.set(str(lot_dim[2]))
        self.lotx = tk.Spinbox(self, from_=1, to=1001, width=6, 
                justify='right', textvariable=self.lotxx,
                background=COLORS.en_back, foreground=COLORS.en_fore
                )
        self.loty = tk.Spinbox(self, from_=1, to=1001, width=6, 
                justify='right', textvariable=self.lotyy,
                background=COLORS.en_back, foreground=COLORS.en_fore
                )
        self.lotz = tk.Spinbox(self, from_=1, to=1001, width=6, 
                justify='right', textvariable=self.lotzz,
                background=COLORS.en_back, foreground=COLORS.en_fore
                )
        #
        self.label_lot_per = ttk.Label(self, text='Lots:')
        self.lot_per = tk.IntVar()
        if lot_per == 0:
            self.lot_per.set(0)
        else :
            self.lot_per.set(1)
        self.check_lot_per = tk.Checkbutton(self, text='Periodic', variable=self.lot_per)
        self.lot_menu(self.lot_use.get())
        #
        #
        self.acc = ttk.Button(self, text='Run', 
                command=lambda: self.calc_fourier(parent, 
                corners, increment, radiation, wvle, ener, adp, ano, percent, 
                lot_type, lot_num, lot_dim, lot_per ))
        #
        #
        self.show= ttk.Button(self, text='Show', 
                command=lambda: self.show_fourier(parent, 
                corners, increment, radiation, wvle, ener, adp, ano, percent, 
                lot_type, lot_num, lot_dim, lot_per ))
        #
        #
        create_exit_button(self, 'discus', 11, 8, self.exit_command,
                (parent, corners, increment, radiation, wvle, ener, adp, ano,
                percent, lot_type, lot_num, lot_dim, lot_per )
                )
        #
        #
        self.CExplain = tk.Canvas(self, bg=COLORS.fr_read, height=200, width=400)
        self.CExplain.create_text( 20,  20, text='Calculates an arbitrary line, ', anchor=tk.W)
        self.CExplain.create_text( 20,  35, text='plane or voxel in reciprocal ', anchor=tk.W)
        self.CExplain.create_text( 20,  50, text='space. The corners are the ', anchor=tk.W)
        self.CExplain.create_text( 20,  65, text='lower left, lower right...', anchor=tk.W)
        self.CExplain.create_text( 20,  80, text='Points include the corners as ', anchor=tk.W)
        self.CExplain.create_text( 20,  95, text='shown in the schematic drawing.', anchor=tk.W)
        self.CExplain.create_line(400, 120, 600,160, width=4)
        self.CExplain.create_line(400, 120, 400, 20, width=4)
        self.CExplain.create_line(400, 120, 500, 60, width=4)
        self.CExplain.create_oval(400-5, 120-5, 400+5, 120+5, fill='black')
        self.CExplain.create_oval(467-5, 133-5, 467+5, 133+5, fill='black')
        self.CExplain.create_oval(533-5, 147-5, 533+5, 147+5, fill='black')
        self.CExplain.create_oval(600-5, 160-5, 600+5, 160+5, fill='black')
        self.CExplain.create_oval(400-5,  70-5, 400+5,  70+5, fill='black')
        self.CExplain.create_oval(400-5,  20-5, 400+5,  20+5, fill='black')
        self.CExplain.create_oval(500-5,  60-5, 500+5,  60+5, fill='black')
        self.CExplain.create_text(390, 120, text='Lower left', anchor=tk.E   )
        self.CExplain.create_text(600, 180, text='Lower right', anchor=tk.CENTER)
        self.CExplain.create_text(390,  20, text='Upper left', anchor=tk.E   )
        self.CExplain.create_text(510,  60, text='Top left', anchor=tk.W)
        self.CExplain.create_text(500, 160, text='Points along abscissa = 4', anchor=tk.E)
        self.CExplain.create_text(390,  70, text='Points along ordinate = 3', anchor=tk.E)
        #

##      # If an Element name was given, make this active
##      if ElementNumber > -1:
##          self.ele.configure(state='normal')
##          self.entry_wvle.configure(state='disabled')
##          self.entry_ener.configure(state='disabled')
##          self.rad_type.set(2)
##      else:
##          self.ele.configure(state='disabled')
##          self.entry_wvle.configure(state='normal')
##          self.entry_ener.configure(state='disabled')
##          self.rad_type.set(0)

        self.caption.grid(   row=0, column=0, columnspan=8, pady=(10, 10))
        self.label_h.grid(   row=1, column=1, sticky='EW')
        self.label_k.grid(   row=1, column=2, sticky='EW')
        self.label_l.grid(   row=1, column=3, sticky='EW')
        self.label_ll.grid(  row=2, column=0, sticky='EW')
        self.label_lr.grid(  row=3, column=0, sticky='EW')
        self.label_ul.grid(  row=4, column=0, sticky='EW')
        self.label_tl.grid(  row=5, column=0, sticky='EW')
        self.entry_ll_h.grid(row=2, column=1, sticky='EW')
        self.entry_ll_k.grid(row=2, column=2, sticky='EW')
        self.entry_ll_l.grid(row=2, column=3, sticky='EW')
        self.entry_lr_h.grid(row=3, column=1, sticky='EW')
        self.entry_lr_k.grid(row=3, column=2, sticky='EW')
        self.entry_lr_l.grid(row=3, column=3, sticky='EW')
        self.entry_ul_h.grid(row=4, column=1, sticky='EW')
        self.entry_ul_k.grid(row=4, column=2, sticky='EW')
        self.entry_ul_l.grid(row=4, column=3, sticky='EW')
        self.entry_tl_h.grid(row=5, column=1, sticky='EW')
        self.entry_tl_k.grid(row=5, column=2, sticky='EW')
        self.entry_tl_l.grid(row=5, column=3, sticky='EW')
        self.label_np.grid(  row=6, column=0, pady=(5, 0), columnspan=2, sticky='EW')
        self.label_np_a.grid(row=7, column=0, sticky='EW')
        self.label_np_o.grid(row=8, column=0, sticky='EW')
        self.label_np_t.grid(row=9, column=0, sticky='EW')
        self.np_a.grid(      row=7, column=1, columnspan=1, sticky='EW')
        self.np_o.grid(      row=8, column=1, columnspan=1, sticky='EW')
        self.np_t.grid(      row=9, column=1, columnspan=1, sticky='EW')
        #
        self.LabelAver.grid(     row=6,  column=3, columnspan=7, sticky='EW')
        self.EntryAver.grid(     row=6,  column=7, sticky='EW')
        self.LabelAverPer.grid(  row=6,  column=8, sticky='W')
        self.label_lot.grid(     row=7,  column=4, sticky='EW')
        self.check_lot.grid(     row=7,  column=5, sticky='EW')
        self.label_lotshape.grid(row= 9, column=3, sticky='EW')
        self.lot_shape.grid(     row= 9, column=4, rowspan=2, sticky='EW')
        self.label_lotnum.grid(  row=11, column=3, sticky='EW')
        self.lotn.grid(          row=11, column=4, sticky='EW')
        self.label_lotdimx.grid( row= 9, column=5, sticky='EW')
        self.label_lotdimy.grid( row=10, column=5, sticky='EW')
        self.label_lotdimz.grid( row=11, column=5, sticky='EW')
        self.lotx.grid(          row=9,  column=6, sticky='EW')
        self.loty.grid(          row=10, column=6, sticky='EW')
        self.lotz.grid(          row=11, column=6, sticky='EW')
        self.label_lot_per.grid( row=8,  column=4, sticky='EW')
        self.check_lot_per.grid( row=8,  column=5, sticky='EW')
        self.show.grid(          row=9,  column=8)
        self.acc.grid(           row=10, column=8)
        self.CExplain.grid(      row=12, column=0, columnspan=9, sticky='EW')
        #
        line = 'fourier'
        suite.suite_learn(line)

    def lot_event(self, event):
        # Inverts the current setting, apparently the Chekbutton bind 
        # Is executed BEFORE the button is inverted !?!?
        if self.lot_use.get()==1:
            choice = 0
        else:
            choice = 1
        self.lot_menu(choice)

    def lot_menu(self, choice):
        if choice ==1:
            self.label_lotshape.configure(foreground=COLORS.nor_fore)
            self.label_lotnum.configure(foreground=COLORS.nor_fore)
            self.label_lotdimx.configure(foreground=COLORS.nor_fore)
            self.label_lotdimy.configure(foreground=COLORS.nor_fore)
            self.label_lotdimz.configure(foreground=COLORS.nor_fore)
            self.label_lot_per.configure(foreground=COLORS.nor_fore)
            self.lot_shape.configure(state='normal')
            self.lotn.configure(state='normal')
            self.lotx.configure(state='normal')
            self.loty.configure(state='normal')
            self.lotz.configure(state='normal')
            self.check_lot_per.configure(state='normal')
        else:
            self.label_lotshape.configure(foreground=COLORS.dis_fore)
            self.label_lotnum.configure(foreground=COLORS.dis_fore)
            self.label_lotdimx.configure(foreground=COLORS.dis_fore)
            self.label_lotdimy.configure(foreground=COLORS.dis_fore)
            self.label_lotdimz.configure(foreground=COLORS.dis_fore)
            self.label_lot_per.configure(foreground=COLORS.dis_fore)
            self.lot_shape.configure(state='disabled')
            self.lotn.configure(state='disabled')
            self.lotx.configure(state='disabled')
            self.loty.configure(state='disabled')
            self.lotz.configure(state='disabled')
            self.check_lot_per.configure(state='disabled')


    def show_fourier(self, parent, \
                    corners, increment, radiation, wvle, ener, adp, ano,
                    percent, lot_type, lot_num, lot_dim, lot_per
                    ):

        self.send_fourier(corners, increment, radiation, wvle, ener, adp, ano,
                percent, lot_type, lot_num, lot_dim, lot_per 
                )
        line= ('show')
        suite.discus_calc_fourier(line)

    def calc_fourier(self, parent, 
                    corners, increment, radiation, wvle, ener, adp, ano, 
                    percent, lot_type, lot_num, lot_dim, lot_per 
                    ):

        self.send_fourier(corners, increment, radiation, wvle, ener, adp, ano, 
                percent, lot_type, lot_num, lot_dim, lot_per 
                )
        line= ('run')
        suite.discus_calc_fourier(line)
        line = 'exit'
        suite.discus_calc_fourier(line)
        parent.b_fourmenu.menu.entryconfig(6, state='normal')
        # Close menu
        self.destroy()

    def send_fourier(self, 
                    corners, increment, radiation, wvle, ener, adp, ano, percent, lot_type, \
                    lot_num, lot_dim, lot_per 
                    ):
        line = ('ll' + ' ' + str(self.entry_ll_h.get()) 
                     + ',' + str(self.entry_ll_k.get())
                     + ',' + str(self.entry_ll_l.get())
               )
        suite.discus_calc_fourier(line)
        line = ('lr' + ' ' + str(self.entry_lr_h.get()) 
                     + ',' + str(self.entry_lr_k.get())
                     + ',' + str(self.entry_lr_l.get())
               )
        suite.discus_calc_fourier(line)
        line = ('ul' + ' ' + str(self.entry_ul_h.get()) 
                     + ',' + str(self.entry_ul_k.get())
                     + ',' + str(self.entry_ul_l.get())
               )
        suite.discus_calc_fourier(line)
        line = ('na' + ' ' + str(self.np_a.get()))
        suite.discus_calc_fourier(line)
        line = ('no' + ' ' + str(self.np_o.get()))
        suite.discus_calc_fourier(line)
        line = ('nt' + ' ' + str(self.np_t.get()))
        suite.discus_calc_fourier(line)
#
        if is_empty(self.rad.curselection()):
           radiation = 0
        else:
           radiation = int(self.rad.curselection()[0])
        if radiation   == 0:
           line = 'xray'
        elif radiation   == 1:
           line = 'neutron'
        elif radiation   == 2:
           line = 'electron'
        else :
           line = 'xray'
        suite.discus_calc_fourier(line)
        if self.rad_type.get() == 0:
           line = ('wvle' + ' ' + str(self.entry_wvle.get()))
        elif self.rad_type.get() == 1:
           line = ('energy' + ' ' + str(self.entry_ener.get()))
        elif self.rad_type.get() == 2:
           line = ('wvle ' + str(self.symbols[int(self.ele.curselection()[0])]))
        suite.discus_calc_fourier(line)
        if self.adp.get() == 1:
           line = ('temp use')
        elif self.adp.get() == 0:
           line = ('temp ignore')
        suite.discus_calc_fourier(line)
        if self.ano.get() == 1:
           line = ('disp anom')
        elif self.ano.get() == 0:
           line = ('disp off')
        suite.discus_calc_fourier(line)
        line = 'set aver, ' + str(self.Aver.get())
        suite.discus_calc_fourier(line)
        if self.lot_use.get() == 0:
           line = 'lots OFF'
        else:
           if is_empty(self.lot_shape.curselection()):
              shape = 0
           else:
              shape = int(self.lot_shape.curselection()[0])
           if self.lot_per.get()== 1:
              period = 'yes'
           else:
              period = 'no'
           if shape==0:
              line = 'lots ' + 'box,' + str(self.lotx.get()) + ',' \
                                      + str(self.loty.get()) + ',' \
                                      + str(self.lotz.get()) + ',' \
                                      + str(self.lotn.get()) + ',' + period
           else:
              line = 'lots ' + 'box,' + str(self.lotx.get()) + ',' \
                                      + str(self.loty.get()) + ',' \
                                      + str(self.lotz.get()) + ',' \
                                      + str(self.lotn.get()) + ',' + period
        suite.discus_calc_fourier(line)

    def exit_command(self, parent, \
                    corners, increment, radiation, wvle, ener, adp, ano, \
                    percent, lot_type, lot_num, lot_dim, lot_per 
                    ):
        self.send_fourier(\
                corners, increment, radiation, wvle, ener, adp, ano, 
                percent, lot_type, lot_num, lot_dim, lot_per 
                )
        line = 'exit'
        suite.discus_calc_fourier(line)
#
