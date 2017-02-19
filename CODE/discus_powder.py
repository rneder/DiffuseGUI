import tkinter as tk
from tkinter import ttk
#import math as math
from support import *
from exit_button import create_exit_button
#from discus_convert import *
from discus_rad_menu import discus_rad_menu
from lib_discus_suite import *


class DISCUS_POWDER_FR(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__ ( self, parent )
        self.config(borderwidth=2, relief=tk.RAISED, background=COLORS.fr_read)
        self.grid(row=2, column=0, columnspan=8, sticky='EW')
        #
        #  Get Element symbols and characteristic wavelength from DISCUS
        nwave, self.symbols, self.wavelengths = get_wave()
        #
        #  Get Powder  settings from DISCUS
        mode, axis, radiation, bElement, wvle, \
                ener, adp, ano, theta, qvalues, dhkl, shkl,  \
                profile, profile_eta, profile_uvw, profile_asy, profile_width,  \
                profile_delta, preferred, pref_dp, pref_pt, pref_hkl, \
                lp, lp_ang, lp_fac \
                = suite.discus_get_powder()
        #
        # Round input to 5 digits
        for i in range(len(qvalues)):
           qvalues[i] = round_rbn(qvalues[i],5)
           theta  [i] = round_rbn(theta[i],5)
        wvle = round_rbn(wvle,5)
        ener = round_rbn(ener,5)
        profile_eta = round_rbn(profile_eta,5)
        for i in range(len(profile_uvw)):
           profile_uvw[i] = round_rbn(profile_uvw[i],5)
        for i in range(len(profile_asy)):
           profile_asy[i] = round_rbn(profile_asy[i],5)
        profile_width = round_rbn(profile_width,5)
        profile_delta = round_rbn(profile_delta,5)
        pref_dp = round_rbn(pref_dp,5)
        pref_pt = round_rbn(pref_pt,5)
        for i in range(len(pref_hkl)):
           pref_hkl[i] = round_rbn(pref_hkl[i],5)
        lp_ang = round_rbn(lp_ang,5)
        lp_fac = round_rbn(lp_fac,5)
        #
        #       Determine if an element was given for its characteristic radiation
        Element = bElement.decode()
        ElementNumber = -1
        for i in range(nwave):
            if Element == self.symbols[i]:
                ElementNumber = i
                break
        # Define variables
        self.calc_mode = tk.IntVar()
        self.calc_mode.set(0)
        self.calc_axis = tk.IntVar()
        self.calc_axis.set(0)
        self.lim_min = tk.StringVar()
        self.lim_max = tk.StringVar()
        self.lim_step = tk.StringVar()
        self.profile_eta = tk.StringVar()
        self.profile_u   = tk.StringVar()
        self.profile_v   = tk.StringVar()
        self.profile_w   = tk.StringVar()
        self.profile_width = tk.StringVar()
        self.pref_dp = tk.StringVar()
        self.pref_pt = tk.StringVar()
        self.pref_h  = tk.StringVar()
        self.pref_k  = tk.StringVar()
        self.pref_l  = tk.StringVar()
        self.lp_ang  = tk.StringVar()
        self.lp_fac  = tk.StringVar()
        if axis==0:
            self.lim_min.set(str(qvalues[0]))
            self.lim_max.set(str(qvalues[1]))
            self.lim_step.set(str(qvalues[2]))
        elif axis==1:
            self.lim_min.set(str(theta[0]))
            self.lim_max.set(str(theta[1]))
            self.lim_step.set(str(theta[2]))
        self.profile_eta.set(str(profile_eta))
        self.profile_u.set(str(profile_uvw[0]))
        self.profile_v.set(str(profile_uvw[1]))
        self.profile_w.set(str(profile_uvw[2]))
        self.profile_width.set(str(profile_width))
        #
        self.pref_dp.set(str(pref_dp))
        self.pref_pt.set(str(pref_pt))
        self.pref_h.set(str(pref_hkl[0]))
        self.pref_k.set(str(pref_hkl[1]))
        self.pref_l.set(str(pref_hkl[2]))
        #
        self.lp_ang.set(str(lp_ang))
        self.lp_fac.set(str(lp_fac))
        #
        self.caption=ttk.Label(self, text='Powder diffraction calculations')
        self.label_mode = ttk.Label(self, text='Powder mode:')
        self.mode = tk.Listbox(self, height=2, width=15, selectbackground=COLORS.en_back,
                selectforeground=COLORS.en_fore, selectmode=tk.SINGLE
                )
        self.mode.configure(exportselection=False)
        self.mode.insert(0,'Debye-Equation')
        self.mode.insert(1,'Rec. Spc. Integr.')
        self.mode.selection_set(mode)
        #
        self.label_axis = ttk.Label(self, text='Powder axis:')
        self.axis = tk.Listbox(self, height=2, width=15, selectbackground=COLORS.en_back,
                selectforeground=COLORS.en_fore, selectmode=tk.SINGLE
                )
        self.axis.configure(exportselection=False)
#       self.axis.insert(0,'d-star')
        self.axis.insert(0,'Q[A^-1]')
        self.axis.insert(1,'2-Theta')
        self.axis.selection_set(axis)
        self.label_limits = ttk.Label(self, text='Powder range:')
        self.label_min    = ttk.Label(self, text='Min:')
        self.label_max    = ttk.Label(self, text='Max:')
        self.label_step   = ttk.Label(self, text='Step:')
        self.entry_min = ttk.Entry(self,textvariable=self.lim_min, width=10,
                justify='right', background=COLORS.en_back, foreground=COLORS.en_fore
                )
        self.entry_max = ttk.Entry(self,textvariable=self.lim_max, width=10, 
                justify='right', background=COLORS.en_back, foreground=COLORS.en_fore
                )
        self.entry_step= ttk.Entry(self,textvariable=self.lim_step,width=10, 
                justify='right', background=COLORS.en_back, foreground=COLORS.en_fore
                )
        # Set values and label according to powder axis
        self.convert_axis(0,0,qvalues, theta)
        #
        self.label_prof = ttk.Label(self, text='Profile:')
        self.prof_yScroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.prof_func = tk.Listbox(self, height=2, width=15, 
                selectbackground=COLORS.en_back,
                selectforeground=COLORS.en_fore,selectmode=tk.SINGLE
                )
        self.prof_func.configure(exportselection=False)
        self.prof_func.insert(0,'None')
        self.prof_func.insert(1,'Gauss')
        self.prof_func.insert(2,'PseudoVoigt')
        self.prof_func.selection_set(profile)
        self.prof_func.yview_scroll(profile, tk.UNITS)
        self.prof_yScroll['command'] = self.prof_func.yview
        self.label_prof_eta = ttk.Label(self, text='Profile eta:')
        self.entry_prof_eta = ttk.Entry(self,textvariable=self.profile_eta, 
                width=10, justify='right', background=COLORS.en_back, 
                foreground=COLORS.en_fore
                )
        self.label_prof_uvw = ttk.Label(self, text='Profile uvw:')
        self.entry_prof_u   = ttk.Entry(self,textvariable=self.profile_u, 
                width=10, justify='right', background=COLORS.en_back, 
                foreground=COLORS.en_fore
                )
        self.entry_prof_v   = ttk.Entry(self,textvariable=self.profile_v, 
                width=10, justify='right', background=COLORS.en_back, 
                foreground=COLORS.en_fore
                )
        self.entry_prof_w   = ttk.Entry(self,textvariable=self.profile_w, 
                width=10, justify='right', background=COLORS.en_back, 
                foreground=COLORS.en_fore)
        self.label_prof_width = ttk.Label(self, text='Profile width:'
                )
        self.entry_prof_width = ttk.Entry(self,textvariable=self.profile_width, 
                width=10, justify='right', background=COLORS.en_back, 
                foreground=COLORS.en_fore)
        self.label_prof_units = ttk.Label(self, text='* FWHM'
                )
        #
        self.label_pref = ttk.Label(self, text='Preferred:')
        self.pref_yScroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.pref_func = tk.Listbox(self, height=2, width=15,
                selectbackground=COLORS.en_back,
                selectforeground=COLORS.en_fore,selectmode=tk.SINGLE
                )
        self.pref_func.configure(exportselection=False)
        self.pref_func.insert(0,'None')
        self.pref_func.insert(1,'Rietveld')
        self.pref_func.insert(2,'March')
        self.pref_func.selection_set(preferred)
        self.pref_func.yview_scroll(preferred, tk.UNITS)
        self.pref_yScroll['command'] = self.pref_func.yview
        self.label_pref_dp = ttk.Label(self, text='Pref. Damp:')
        self.entry_pref_dp = ttk.Entry(self, textvariable=self.pref_dp, 
                width=10, justify='right', background=COLORS.en_back, 
                foreground=COLORS.en_fore
                )
        self.label_pref_pt = ttk.Label(self, text='Pref. Frac:')
        self.entry_pref_pt = ttk.Entry(self, textvariable=self.pref_pt, 
                width=10, justify='right', background=COLORS.en_back, 
                foreground=COLORS.en_fore
                )
        self.label_pref_hkl= ttk.Label(self, text='Pref. HKL :')
        self.entry_pref_h  = ttk.Entry(self, textvariable=self.pref_h, 
                width=10, justify='right', background=COLORS.en_back, 
                foreground=COLORS.en_fore
                )
        self.entry_pref_k  = ttk.Entry(self, textvariable=self.pref_k, 
                width=10, justify='right', background=COLORS.en_back, 
                foreground=COLORS.en_fore
                )
        self.entry_pref_l  = ttk.Entry(self, textvariable=self.pref_l, 
                width=10, justify='right', background=COLORS.en_back, 
                foreground=COLORS.en_fore
                )
        #
        self.label_lp = ttk.Label(self, text='LP Corr.:')
        self.lp_yScroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.lp_func = tk.Listbox(self, height=2, width=15,
                selectbackground=COLORS.en_back,
                selectforeground=COLORS.en_fore, selectmode=tk.SINGLE
                )
        self.lp_func.configure(exportselection=False)
        self.lp_func.insert(0, 'None')
        self.lp_func.insert(1, 'Bragg-Br.')
        self.lp_func.insert(2, 'Neutron')
        self.lp_func.insert(3, 'Synchrotron')
        self.lp_func.selection_set(lp)
        self.lp_func.yview_scroll(lp, tk.UNITS)
        self.lp_yScroll['command'] = self.lp_func.yview
        self.label_lp_ang = ttk.Label(self, text='Mono.Theta')
        self.entry_lp_ang = ttk.Entry(self, textvariable=self.lp_ang, width=10, 
                justify='right', background=COLORS.en_back, 
                foreground=COLORS.en_fore
                )
        self.label_lp_fac = ttk.Label(self, text='Fraction:')
        self.entry_lp_fac = ttk.Entry(self, textvariable=self.lp_fac, width=10, 
                justify='right', background=COLORS.en_back, 
                foreground=COLORS.en_fore
                )
        #
        discus_rad_menu(self, nwave, radiation, wvle, ener, ElementNumber, 
                adp, ano, 1, 4
                )
        #
        # Do bindings to powder axis
        self.axis.bind('<ButtonRelease-1>', 
                lambda eff: self.convert_axis(eff, 1, qvalues, theta))
        self.prof_func.bind('<ButtonRelease-1>', 
                lambda eff: self.convert_profile(eff, 1, profile_uvw, profile_delta))
        self.pref_func.bind('<ButtonRelease-1>', 
                lambda eff: self.convert_pref(eff, 1, pref_dp, pref_pt, pref_hkl))
        self.lp_func.bind('<ButtonRelease-1>', 
                lambda eff: self.convert_lp(eff, 1, lp_ang, lp_fac))
        #
        self.convert_profile(0,0,profile_uvw, profile_delta)
        self.convert_pref(0,0,pref_dp, pref_pt, pref_hkl)
        self.convert_lp(0,0,lp_ang, lp_fac)
        #
        self.acc = ttk.Button(self, text='Run', command=lambda: self.run_powder(parent))
        #
        #
        self.show= ttk.Button(self, text='Show', command=lambda: self.show_powder(parent))
        #
        #
        create_exit_button(self,'discus',11,8,self.exit_command,(parent,0))
        #
        # Grid all elements that were not placed via functions
        self.caption.grid     (    row=0, column=0, columnspan=8, sticky='NS', pady=(10,10))
        self.label_mode.grid  (    row=1, column=0, columnspan=1, sticky='EW')
        self.mode.grid        (    row=1, column=1, columnspan=2, sticky='W')
        self.label_axis.grid  (    row=3, column=0, columnspan=1, sticky='EW')
        self.axis.grid        (    row=3, column=1, columnspan=2, sticky='W')
        self.label_limits.grid(    row=5, column=0, columnspan=1, sticky='EW')
        self.label_min.grid   (    row=4, column=1, columnspan=1, sticky='EW')
        self.label_max.grid   (    row=4, column=2, columnspan=1, sticky='EW')
        self.label_step.grid  (    row=4, column=3, columnspan=1, sticky='EW')
        self.entry_min.grid   (    row=5, column=1, columnspan=1, sticky='EW')
        self.entry_max.grid   (    row=5, column=2, columnspan=1, sticky='EW')
        self.entry_step.grid  (    row=5, column=3, columnspan=1, sticky='EW')
        self.label_prof.grid  (    row=6, column=0, columnspan=1, sticky='EW')
        self.prof_func.grid   (    row=6, column=1, columnspan=1, sticky='EW')
        self.prof_yScroll.grid(    row=6, column=2, columnspan=1, sticky='W')
        self.label_prof_eta.grid(  row=7, column=0, columnspan=1, sticky='EW')
        self.entry_prof_eta.grid(  row=7, column=1, columnspan=1, sticky='EW')
        self.label_prof_uvw.grid(  row=8, column=0, columnspan=1, sticky='EW')
        self.entry_prof_u.grid(    row=8, column=1, columnspan=1, sticky='EW')
        self.entry_prof_v.grid(    row=8, column=2, columnspan=1, sticky='EW')
        self.entry_prof_w.grid(    row=8, column=3, columnspan=1, sticky='EW')
        self.label_prof_width.grid(row=9, column=0, columnspan=1, sticky='EW')
        self.entry_prof_width.grid(row=9, column=1, columnspan=1, sticky='EW')
        self.label_prof_units.grid(row=9, column=2, columnspan=1, sticky='EW')
        self.show.grid(            row=9, column=8, columnspan=1, sticky='EW')
        self.acc.grid(             row=10, column=8, columnspan=1, sticky='EW')
        self.label_pref.grid(      row=10, column=0, columnspan=1, sticky='EW')
        self.pref_func.grid   (    row=10, column=1, columnspan=1, sticky='EW')
        self.pref_yScroll.grid(    row=10, column=2, columnspan=1, sticky='W')
        self.label_pref_dp.grid(   row=11, column=0, columnspan=1, sticky='EW')
        self.entry_pref_dp.grid(   row=11, column=1, columnspan=1, sticky='EW')
        self.label_pref_pt.grid(   row=12, column=0, columnspan=1, sticky='EW')
        self.entry_pref_pt.grid(   row=12, column=1, columnspan=1, sticky='EW')
        self.label_pref_hkl.grid(  row=13, column=0, columnspan=1, sticky='EW')
        self.entry_pref_h.grid(    row=13, column=1, columnspan=1, sticky='EW')
        self.entry_pref_k.grid(    row=13, column=2, columnspan=1, sticky='EW')
        self.entry_pref_l.grid(    row=13, column=3, columnspan=1, sticky='EW')
        self.label_lp.grid(        row=6, column=4, columnspan=1, sticky='EW')
        self.lp_func.grid   (      row=6, column=5, columnspan=1, sticky='EW',padx=(5,0))
        self.lp_yScroll.grid(      row=6, column=6, columnspan=1, sticky='W')
        self.label_lp_ang.grid(    row=7, column=4, columnspan=1, sticky='EW',padx=(5,0))
        self.entry_lp_ang.grid(    row=7, column=5, columnspan=1, sticky='EW')
        self.label_lp_fac.grid(    row=8, column=4, columnspan=1, sticky='EW',padx=(5,0))
        self.entry_lp_fac.grid(    row=8, column=5, columnspan=1, sticky='EW')
        #
        line = 'powder'
        suite.suite_learn(line)
        #

    def run_powder(self, parent):
        dummy = 0
        self.send_powder(parent, dummy)
        line = 'run'
        suite.discus_calc_powder(line)
        line = 'exit'
        suite.discus_calc_powder(line)
        parent.b_fourmenu.menu.entryconfig(6,state='normal')
        # Close menu
        self.destroy()
        #
    def show_powder(self, parent):
        dummy = 0
        self.send_powder(parent, dummy)
        line = 'show'
        suite.discus_calc_powder(line)
        #
    def send_powder(self, parent, dummy):
        #
        if is_empty(self.rad.curselection()):
           line = 'xray'
        else:
           if int(self.rad.curselection()[0])==0:
               line = 'xray'
           elif int(self.rad.curselection()[0])==1:
               line = 'neutron'
           elif int(self.rad.curselection()[0])==2:
               line = 'electron'
           else :
               line = 'xray'
        suite.discus_calc_powder(line)
        #
        if is_empty(self.mode.curselection()):
            line = 'set calc, debye'
        else:
            if int(self.mode.curselection()[0])==0:
                line = 'set calc, debye'
            elif int(self.mode.curselection()[0])==1:
                line = 'set calc, complete'
            else:
                line = 'set calc, debye'
        suite.discus_calc_powder(line)
        #
        if is_empty(self.axis.curselection()):
           calc_axis = 0
        else:
           calc_axis = int(self.axis.curselection()[0])
        if calc_axis   == 0:
           line = 'set axis, q'
           suite.discus_calc_powder(line)
           line = 'set qmin, ' + str(self.entry_min.get())
           suite.discus_calc_powder(line)
           line = 'set qmax, ' + str(self.entry_max.get())
           suite.discus_calc_powder(line)
           line = 'set dq, ' + str(self.entry_step.get())
           suite.discus_calc_powder(line)
        if calc_axis   == 1:
           line = 'set axis, tth'
           suite.discus_calc_powder(line)
           line = 'set tthmin, ' + str(self.entry_min.get())
           suite.discus_calc_powder(line)
           line = 'set tthmax, ' + str(self.entry_max.get())
           suite.discus_calc_powder(line)
           line = 'set dtth, ' + str(self.entry_step.get())
           suite.discus_calc_powder(line)
        elif calc_axis   == 2:
           line = 'set axis, dstar'
           suite.discus_calc_powder(line)
        #
        if self.rad_type.get() == 0:
           line = ('set wvle, ' + str(self.entry_wvle.get()))
        elif self.rad_type.get() == 1:
           line = ('set energy, ' + str(self.entry_ener.get()))
        elif self.rad_type.get() == 2:
           line = ('set wvle, ' + str(self.symbols[int(self.ele.curselection()[0])]))
        suite.discus_calc_powder(line)
        #
        if self.adp.get() == 1:
           line = ('set temp, use')
        elif self.adp.get() == 0:
           line = ('set temp, ignore')
        suite.discus_calc_powder(line)
        #
        if self.ano.get() == 1:
           line = ('set disp, anom')
        elif self.ano.get() == 0:
           line = ('set disp, off')
        suite.discus_calc_powder(line)
        #
        # Profile info
        #
        if is_empty(self.prof_func.curselection()):
            line = 'set profile, none'
            suite.discus_calc_powder(line)
        else:
            if int(self.prof_func.curselection()[0])==0:
                line = 'set profile, off'
                suite.discus_calc_powder(line)
            elif int(self.prof_func.curselection()[0])==1:
                line = 'set profile, gauss'
                suite.discus_calc_powder(line)
            elif int(self.prof_func.curselection()[0])==2:
                line = 'set profile, pseudo'
                suite.discus_calc_powder(line)
                line = 'set profile, eta, ' + str(self.entry_prof_eta.get())
                suite.discus_calc_powder(line)
                line = 'set profile, uvw, ' + str(self.entry_prof_u.get()) \
                                   + ','    + str(self.entry_prof_v.get()) \
                                   + ','    + str(self.entry_prof_w.get())
                suite.discus_calc_powder(line)
                line = 'set profile, width, ' + str(self.entry_prof_width.get())
                suite.discus_calc_powder(line)
        #
        # Preferred info
        #
        if is_empty(self.pref_func.curselection()):
            line = 'set preferred, none'
            suite.discus_calc_powder(line)
        else:
            if int(self.pref_func.curselection()[0])==0:
                line = 'set preferred, off'
                suite.discus_calc_powder(line)
            else:
                if int(self.pref_func.curselection()[0])==1:
                    line = 'set preferred, rietveld'
                    suite.discus_calc_powder(line)
                elif int(self.pref_func.curselection()[0])==2:
                    line = 'set preferred, march'
                    suite.discus_calc_powder(line)
                line = 'set preferred, damping, ' + str(self.entry_pref_dp.get())
                suite.discus_calc_powder(line)
                line = 'set preferred, portion, ' + str(self.entry_pref_pt.get())
                suite.discus_calc_powder(line)
                line = 'set preferred, hkl, ' + str(self.entry_pref_h.get()) \
                                     + ','    + str(self.entry_pref_k.get()) \
                                     + ','    + str(self.entry_pref_l.get())
                suite.discus_calc_powder(line)
        #
        # Lorenz-Polarization Correction
        #
        if is_empty(self.lp_func.curselection()):
            line = 'set lp, none'
            suite.discus_calc_powder(line)
        elif int(self.lp_func.curselection()[0])==0:
            line = 'set lp, off'
            suite.discus_calc_powder(line)
        elif int(self.lp_func.curselection()[0])==1:
            line = 'set lp, bragg, ' + str(self.entry_lp_ang.get())
            suite.discus_calc_powder(line)
        elif int(self.lp_func.curselection()[0])==2:
            line = 'set lp, neutron'
            suite.discus_calc_powder(line)
        elif int(self.lp_func.curselection()[0])==3:
            line = 'set lp, sync, ' + str(self.entry_lp_fac.get()) \
                             + ','  + str(self.entry_lp_ang.get())
            suite.discus_calc_powder(line)
#       line = 'show'
#       suite.discus_calc_powder(line)
        #
    def exit_command(self, parent,i):
        i=1
        self.send_powder(parent,i)
        line = 'exit'
        suite.discus_calc_powder(line)
     
        
    def convert_axis(self, eff=None, event=0, qvalues=['0.5', '5.0', '0.01'],
                     theta=['5.0', '120.0', '0.01']):
        #
        # Change of powder axis 
        # Handle if no selection was given
        if is_empty(self.axis.curselection()):
            self.lim_min.set(str(qvalues[0]))
            self.lim_max.set(str(qvalues[1]))
            self.lim_step.set(str(qvalues[2]))
            self.label_min['text'] = 'Q-min:'
            self.label_max['text'] = 'Q-max:'   
            self.label_step['text'] = 'Q-step:'
        else:
            if int(self.axis.curselection()[0]) == 0:
                self.lim_min.set(str(qvalues[0]))
                self.lim_max.set(str(qvalues[1]))
                self.lim_step.set(str(qvalues[2]))
                self.label_min['text'] = 'Q-min:'
                self.label_max['text'] = 'Q-max:'
                self.label_step['text'] = 'Q-step:'
            elif int(self.axis.curselection()[0]) == 1:
                self.lim_min.set(str(theta[0]))
                self.lim_max.set(str(theta[1]))
                self.lim_step.set(str(theta[2]))
                self.label_min['text'] = '2Theta-min:'
                self.label_max['text'] = '2Theta-max:'
                self.label_step['text'] = '2Theta-step:'
    def convert_profile(self, eff=None, event=0, uvw=['0.01', '0.01', '0.01'], delta='0.5'):    
        #
        # Change of profile function
        # Handle if no selection was given
        if is_empty(self.prof_func.curselection()):
            self.label_prof_eta.configure(foreground=COLORS.dis_fore)
            self.label_prof_uvw.configure(foreground=COLORS.dis_fore)
            self.label_prof_width.configure(foreground=COLORS.dis_fore)
            self.label_prof_units.configure(foreground=COLORS.dis_fore)
            self.entry_prof_eta.configure(state='disabled', foreground=COLORS.dis_fore)
            self.entry_prof_u.configure(state='disabled', foreground=COLORS.dis_fore)
            self.entry_prof_v.configure(state='disabled', foreground=COLORS.dis_fore)
            self.entry_prof_w.configure(state='disabled', foreground=COLORS.dis_fore)
            self.entry_prof_width.configure(state='disabled', foreground=COLORS.dis_fore)
        else:
            if int(self.prof_func.curselection()[0]) == 0:
                self.label_prof_eta.configure(foreground=COLORS.dis_fore)
                self.label_prof_uvw.configure(foreground=COLORS.dis_fore)
                self.label_prof_width.configure(foreground=COLORS.dis_fore)
                self.label_prof_units.configure(foreground=COLORS.dis_fore)
                self.entry_prof_eta.configure(state='disabled', foreground=COLORS.dis_fore)
                self.entry_prof_u.configure(state='disabled', foreground=COLORS.dis_fore)
                self.entry_prof_v.configure(state='disabled', foreground=COLORS.dis_fore)
                self.entry_prof_w.configure(state='disabled', foreground=COLORS.dis_fore)
                self.entry_prof_width.configure(state='disabled', foreground=COLORS.dis_fore)
            elif int(self.prof_func.curselection()[0]) == 1:
                self.label_prof_eta.configure(foreground=COLORS.dis_fore)
                self.label_prof_uvw.configure(foreground=COLORS.nor_fore)
                self.label_prof_width.configure(foreground=COLORS.nor_fore)
                self.label_prof_units.configure(foreground=COLORS.nor_fore)
                self.entry_prof_eta.configure(state='disabled', foreground=COLORS.dis_fore)
                self.entry_prof_u.configure(state='disabled', foreground=COLORS.dis_fore)
                self.entry_prof_v.configure(state='disabled', foreground=COLORS.dis_fore)
                self.entry_prof_w.configure(state='normal', foreground=COLORS.en_fore)
                self.entry_prof_width.configure(state='normal', foreground=COLORS.en_fore)
                self.label_prof_uvw['text'] = 'Profile sigma:'
            elif int(self.prof_func.curselection()[0]) == 2:
                self.label_prof_eta.configure(foreground=COLORS.nor_fore)
                self.label_prof_uvw.configure(foreground=COLORS.nor_fore)
                self.label_prof_width.configure(foreground=COLORS.nor_fore)
                self.label_prof_units.configure(foreground=COLORS.nor_fore)
                self.entry_prof_eta.configure(state='normal', foreground=COLORS.en_fore)
                self.entry_prof_u.configure(state='normal', foreground=COLORS.en_fore)
                self.entry_prof_v.configure(state='normal', foreground=COLORS.en_fore)
                self.entry_prof_w.configure(state='normal', foreground=COLORS.en_fore)
                self.entry_prof_width.configure(state='normal', foreground=COLORS.en_fore)
                self.label_prof_uvw['text'] = 'Profile uvw:'
    def convert_pref(self, eff=None, event=0, dp=0, pt=0, hkl=['0.00','0.00', '1.00']):    
        #
        # Change of preferred orientation model
        # Handle if no selection was given
        if is_empty(self.pref_func.curselection()):
            self.label_pref_dp.configure(foreground=COLORS.dis_fore)
            self.label_pref_pt.configure(foreground=COLORS.dis_fore)
            self.label_pref_hkl.configure(foreground=COLORS.dis_fore)
            self.entry_pref_dp.configure(state='disabled', foreground=COLORS.dis_fore)
            self.entry_pref_pt.configure(state='disabled', foreground=COLORS.dis_fore)
            self.entry_pref_h.configure(state='disabled', foreground=COLORS.dis_fore)
            self.entry_pref_k.configure(state='disabled', foreground=COLORS.dis_fore)
            self.entry_pref_l.configure(state='disabled', foreground=COLORS.dis_fore)
        else:
            if int(self.pref_func.curselection()[0]) == 0:
                self.label_pref_dp.configure(foreground=COLORS.dis_fore)
                self.label_pref_pt.configure(foreground=COLORS.dis_fore)
                self.label_pref_hkl.configure(foreground=COLORS.dis_fore)
                self.entry_pref_dp.configure(state='disabled', foreground=COLORS.dis_fore)
                self.entry_pref_pt.configure(state='disabled', foreground=COLORS.dis_fore)
                self.entry_pref_h.configure(state='disabled', foreground=COLORS.dis_fore)
                self.entry_pref_k.configure(state='disabled', foreground=COLORS.dis_fore)
                self.entry_pref_l.configure(state='disabled', foreground=COLORS.dis_fore)
            elif (int(self.pref_func.curselection()[0]) == 1 or
                  int(self.pref_func.curselection()[0]) == 2
                 ):
                #
                self.label_pref_dp.configure(foreground=COLORS.nor_fore)
                self.label_pref_pt.configure(foreground=COLORS.nor_fore)
                self.label_pref_hkl.configure(foreground=COLORS.nor_fore)
                self.entry_pref_dp.configure(state='normal', foreground=COLORS.en_fore)
                self.entry_pref_pt.configure(state='normal', foreground=COLORS.en_fore)
                self.entry_pref_h.configure(state='normal', foreground=COLORS.en_fore)
                self.entry_pref_k.configure(state='normal', foreground=COLORS.en_fore)
                self.entry_pref_l.configure(state='normal', foreground=COLORS.en_fore)
    def convert_lp(self, eff=None, event=0, ang=0, fac=0):    
        #
        # Change of LP correction model
        # Handle if no selection was given
        if is_empty(self.lp_func.curselection()):
            self.label_lp_ang.configure(foreground=COLORS.dis_fore)
            self.label_lp_fac.configure(foreground=COLORS.dis_fore)
            self.entry_lp_ang.configure(state='disabled', foreground=COLORS.dis_fore)
            self.entry_lp_fac.configure(state='disabled', foreground=COLORS.dis_fore)
        else:
            if int(self.lp_func.curselection()[0]) == 0:
                self.label_lp_ang.configure(foreground=COLORS.dis_fore)
                self.label_lp_fac.configure(foreground=COLORS.dis_fore)
                self.entry_lp_ang.configure(state='disabled', foreground=COLORS.dis_fore)
                self.entry_lp_fac.configure(state='disabled', foreground=COLORS.dis_fore)
            elif int(self.lp_func.curselection()[0]) == 1:
                self.label_lp_ang.configure(foreground=COLORS.nor_fore)
                self.label_lp_fac.configure(foreground=COLORS.dis_fore)
                self.entry_lp_ang.configure(state='normal', foreground=COLORS.en_fore)
                self.entry_lp_fac.configure(state='disabled', foreground=COLORS.dis_fore)
            elif int(self.lp_func.curselection()[0]) == 2:
                self.label_lp_ang.configure(foreground=COLORS.dis_fore)
                self.label_lp_fac.configure(foreground=COLORS.dis_fore)
                self.entry_lp_ang.configure(state='disabled', foreground=COLORS.dis_fore)
                self.entry_lp_fac.configure(state='disabled', foreground=COLORS.dis_fore)
            elif int(self.lp_func.curselection()[0]) == 3:
                self.label_lp_ang.configure(foreground=COLORS.nor_fore)
                self.label_lp_fac.configure(foreground=COLORS.nor_fore)
                self.entry_lp_ang.configure(state='normal', foreground=COLORS.en_fore)
                self.entry_lp_fac.configure(state='normal', foreground=COLORS.en_fore)
