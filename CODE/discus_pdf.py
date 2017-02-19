import tkinter as tk
from tkinter import ttk
from support import *
from exit_button import create_exit_button
from file_stuff import file_new
from lib_discus_suite import *

class DISCUS_PDF_FR(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__ ( self, parent )
        self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_read)
        self.grid(row=2,column=0,columnspan=8, sticky='EW')
        #
        # Get PDF settings from DISCUS
        radiation, adp, r_max, r_step, lrho0, rho0, corr_lin, corr_quad, \
                period, exact, weight, finite, sphere, qmax, qbroad, qdamp \
                = suite.discus_get_pdf()
        #
        # Round input to 5 digits
        r_max     = round_rbn(r_max, 5)
        r_step    = round_rbn(r_step,5)
        rho0      = round_rbn(rho0  ,5)
        weight    = round_rbn(weight,5)
        sphere    = round_rbn(sphere,5)
        corr_lin  = round_rbn(corr_lin  ,5)
        corr_quad = round_rbn(corr_quad ,5)
        qmax      = round_rbn(qmax,  5)
        qbroad    = round_rbn(qbroad,8)
        qdamp     = round_rbn(qdamp, 8)
        #
        # Define variables
#       self.lim_min = tk.StringVar()  ' Reserved for later use
        self.lim_max   = tk.StringVar()
        self.lim_step  = tk.StringVar()
        self.rho0      = tk.StringVar()
        self.rho0_type = tk.IntVar()
        self.corr_lin  = tk.StringVar()
        self.corr_quad = tk.StringVar()
        self.corr_type = tk.IntVar()
        self.peri_type = tk.IntVar()
        self.exct_type = tk.IntVar()
        self.weight    = tk.StringVar()
        self.finite_type = tk.IntVar()
        self.sphere    = tk.StringVar()
        self.qmax      = tk.StringVar()
        self.qbroad    = tk.StringVar()
        self.qdamp     = tk.StringVar()
        self.filename = tk.StringVar()
        #
        self.lim_max.set(r_max)
        self.lim_step.set(r_step)
        self.rho0.set(rho0)
        self.rho0_type.set(lrho0)
        self.corr_lin.set(corr_lin)
        self.corr_quad.set(corr_quad)
        if corr_lin > 0.0:
            self.corr_type.set(0)
        elif corr_quad > 0.0:
            self.corr_type.set(1)
        else:
            self.corr_type.set(0)
        self.peri_type.set(period)
        self.exct_type.set(exact)
        self.weight.set(weight)
        self.finite_type.set(finite)
        self.sphere.set(sphere)
        self.qmax.set(qmax)
        self.qbroad.set(qbroad)
        self.qdamp.set(qdamp)
        self.filename.set('Filename undefined')
        #
        self.caption=ttk.Label(self, text='Pair Distribution Function calculations')

        self.label_limits = ttk.Label(self, text='PDF range:')
#       self.label_min    = ttk.Label(self, text='Min:')
        self.label_max    = ttk.Label(self, text='Max:')
        self.label_step   = ttk.Label(self, text='Step:')
#       self.entry_min = ttk.Entry(self,textvariable=self.lim_min, width=10, justify='right')
        self.entry_max = ttk.Entry(self,textvariable=self.lim_max, width=10, justify='right')
        self.entry_step= ttk.Entry(self,textvariable=self.lim_step,width=10, justify='right')
        self.label_rho0 = ttk.Label(self, text='Numb. density:')
        self.R1 = tk.Radiobutton(self,text='Automatic', variable=self.rho0_type,
                  value=1, activeforeground='#F00',foreground='#00F', justify='left',
                  command=lambda: self.setup_rho0( 1))
        self.R0 = tk.Radiobutton(self,text='Value    ', variable=self.rho0_type,
                  value=0, activeforeground='#F00',foreground='#00F', justify='left',
                  command=lambda: self.setup_rho0( 0))
        self.entry_rho0 = ttk.Entry(self,textvariable=self.rho0, width=10, justify='right')
        self.label_corr = ttk.Label(self, text='Corr. correct.:')
        self.C0 = tk.Radiobutton(self,text='linear', variable=self.corr_type,
                  value=0, activeforeground='#F00',foreground='#00F', justify='left',
                  command=lambda: self.setup_corr( 0))
        self.C1 = tk.Radiobutton(self,text='quadratic', variable=self.corr_type,
                  value=1, activeforeground='#F00',foreground='#00F', justify='left',
                  command=lambda: self.setup_corr( 1))
        self.entry_corr_lin  = ttk.Entry(self,textvariable=self.corr_lin , width=10, justify='right')
        self.entry_corr_quad = ttk.Entry(self,textvariable=self.corr_quad, width=10, justify='right')
        #
        self.label_peri = ttk.Label(self, text='Boundary cond.:')
        self.P1 = tk.Radiobutton(self,text='periodic', variable=self.peri_type,
                  value=1, activeforeground='#F00',foreground='#00F', justify='left',
                  command=lambda: self.setup_peri( 0))
        self.P0 = tk.Radiobutton(self,text='crystal', variable=self.peri_type,
                  value=0, activeforeground='#F00',foreground='#00F', justify='left',
                  command=lambda: self.setup_peri( 1))
#       self.E0 = tk.Radiobutton(self,text='linear', variable=self.corr_type,
#                 value=0, activeforeground='#F00',foreground='#00F', justify='left',
#                 command=lambda: self.setup_corr( 0))
#       self.E1 = tk.Radiobutton(self,text='quadratic', variable=self.corr_type,
#                 value=1, activeforeground='#F00',foreground='#00F', justify='left',
#                 command=lambda: self.setup_corr( 1))
        self.label_weight = ttk.Label(self, text='Scale factor:')
        self.entry_weight = ttk.Entry(self,textvariable=self.weight, width=10, justify='right')
        self.label_finite = ttk.Label(self, text='Finite size corr.:')
        self.F0 = tk.Radiobutton(self,text='infinite', variable=self.finite_type,
                  value=0, activeforeground='#F00',foreground='#00F', justify='left',
                  command=lambda: self.setup_finite( 0))
        self.F1 = tk.Radiobutton(self,text='sphere', variable=self.finite_type,
                  value=1, activeforeground='#F00',foreground='#00F', justify='left',
                  command=lambda: self.setup_finite( 1))
        self.entry_sphere = ttk.Entry(self,textvariable=self.sphere, width=10, justify='right')
        #
        self.fileb = ttk.Button(self, text='Save as', command=lambda: file_new(self))
        self.label_fle = ttk.Label(self, textvariable=self.filename,
                  relief=tk.RAISED, foreground='#FF0000'
                  )

        self.label_rad = ttk.Label(self,text='Radiation:')
        self.rad_type = tk.IntVar()
        self.rad_type.set(0)
        self.rad = tk.Listbox(self, height=3, width=10,selectbackground='#FFFFFF',
                   selectforeground='#0000FF',selectmode=tk.SINGLE)
        self.rad.configure(exportselection=False)
        self.rad.insert(1,'X-ray')
        self.rad.insert(2,'neutron')
        self.rad.insert(3,'electron')
        self.rad.selection_set(radiation)
        #
        #
        self.adp = tk.IntVar()
        self.adp.set(adp)
        self.label_adp = ttk.Label(self,text='ADP:')
        self.check_adp = ttk.Checkbutton(self,text='Use',variable=self.adp)
        #
        self.label_qmax = ttk.Label(self,text='Qmax:')
        self.entry_qmax = ttk.Entry(self,textvariable=self.qmax,width=10, justify='right')
        self.label_qbroad = ttk.Label(self,text='Qbroad:')
        self.entry_qbroad = ttk.Entry(self,textvariable=self.qbroad,width=10, justify='right')
        self.label_qdamp = ttk.Label(self,text='Qdamp:')
        self.entry_qdamp = ttk.Entry(self,textvariable=self.qdamp,width=10, justify='right')
        #
        self.show= ttk.Button(self, text='Show', command=lambda: self.show_pdf(parent))
        #
        self.acc = ttk.Button(self, text='Run', command=lambda: self.run_pdf(parent))
        create_exit_button(self,'discus',11,8,self.exit_command,(parent,0))
        #
        # Grid all elements that were not placed via functions
        self.caption.grid     (row=0, column=0, columnspan=9, sticky='NS', pady=(10,10))
        self.label_limits.grid(row=2, column=0, columnspan=1, sticky='EW')
#       self.label_min.grid   (row=1, column=1, columnspan=1, sticky='EW')
        self.label_max.grid   (row=1, column=1, columnspan=1, sticky='EW')
        self.label_step.grid  (row=1, column=2, columnspan=1, sticky='EW')
#       self.entry_min.grid   (row=1, column=1, columnspan=1, sticky='EW')
        self.entry_max.grid   (row=2, column=1, columnspan=1, sticky='EW')
        self.entry_step.grid  (row=2, column=2, columnspan=1, sticky='EW')
        self.label_rho0.grid  (row=3, column=0, columnspan=1, sticky='EW',pady=(5,0))
        self.R1.grid          (row=3, column=1, columnspan=1, sticky='EW',pady=(5,0))
        self.R0.grid          (row=4, column=1, columnspan=1, sticky='EW')
        self.entry_rho0.grid  (row=4, column=2, columnspan=1, sticky='EW')
        self.label_corr.grid  (row=5, column=0, columnspan=1, sticky='EW')
        self.C0.grid          (row=5, column=1, columnspan=1, sticky='EW',pady=(5,0))
        self.C1.grid          (row=6, column=1, columnspan=1, sticky='EW')
        self.entry_corr_lin.grid (row=5, column=2, columnspan=1, sticky='EW',pady=(5,0))
        self.entry_corr_quad.grid(row=6, column=2, columnspan=1, sticky='EW')
        self.label_peri.grid  (row=7, column=0, columnspan=1, sticky='EW',pady=(5,0))
        self.P1.grid          (row=7, column=1, columnspan=1, sticky='EW',pady=(5,0))
        self.P0.grid          (row=8, column=1, columnspan=1, sticky='EW')
        self.label_weight.grid(row=9, column=0, columnspan=1, sticky='EW',pady=(5,0))
        self.entry_weight.grid(row=9, column=1, columnspan=1, sticky='EW',pady=(5,0))
        self.label_finite.grid(row=10, column=0, columnspan=1, sticky='EW',pady=(5,0))
        self.F0.grid          (row=10, column=1, columnspan=1, sticky='EW',pady=(5,0))
        self.F1.grid          (row=11, column=1, columnspan=1, sticky='EW')
        self.entry_sphere.grid(row=11, column=2, columnspan=1, sticky='EW')
        self.label_rad.grid(   row=1, column=5, padx=(5,0), sticky='EW')
        self.rad.grid(         row=1, column=6, rowspan=3, sticky='EW')
        self.label_adp.grid(   row=4, column=5, padx=(5,0), sticky='EW')
        self.check_adp.grid(   row=4, column=6, sticky='EW')
        self.label_qmax.grid(  row=5, column=5, padx=(5,0), sticky='EW')
        self.entry_qmax.grid(  row=5, column=6, sticky='EW')
        self.label_qbroad.grid(row=6, column=5, padx=(5,0), sticky='EW')
        self.entry_qbroad.grid(row=6, column=6, sticky='EW')
        self.label_qdamp.grid( row=7, column=5, padx=(5,0), sticky='EW')
        self.entry_qdamp.grid( row=7, column=6, sticky='EW')
        self.fileb.grid(       row=12, column=0)
        self.label_fle.grid(   row=12, column=1, columnspan=5, padx=(10,20), sticky='W')
        #
        self.show.grid(row=9, column=8, columnspan=1, sticky='EW')
        self.acc.grid(row=10, column=8, columnspan=1, sticky='EW')
        #
        line = 'powder'
        suite.suite_learn(line)
        #
        self.setup_rho0(self.rho0_type.get())
        self.setup_corr(self.corr_type.get())
        self.setup_finite(self.finite_type.get())
        #
        self.acc.configure(state='disabled')

    def setup_rho0(self, mode):
        if mode == 1:
            self.entry_rho0.configure(state='disabled')
        else:
            self.entry_rho0.configure(state='normal')

    def setup_finite(self, mode):
        if mode == 0:
            self.entry_sphere.configure(state='disabled')
        else:
            self.entry_sphere.configure(state='normal')


    def setup_corr(self, mode):
        if mode == 0:
            self.entry_corr_lin.configure(state='normal')
            self.entry_corr_quad.configure(state='disabled')
        else:
            self.entry_corr_lin.configure(state='disabled')
            self.entry_corr_quad.configure(state='normal')

    def setup_peri(self, mode):
        i = 0
#       if mode == 0:
#           self.entry_corr_lin.configure(state='normal')
#           self.entry_corr_quad.configure(state='disabled')
#       else:
#           self.entry_corr_lin.configure(state='disabled')
#           self.entry_corr_quad.configure(state='normal')

    def run_pdf(self, parent):
        dummy = 0
        self.send_pdf(parent, dummy)
        line = 'calc'
        suite.discus_calc_pdf(line)
        line = 'exit'
        suite.discus_calc_pdf(line)
        if self.filename.get() != 'undefined':
            line = 'save pdf, ' + str(self.filename.get())
            suite.discus_calc_pdf(line)
        self.destroy()
        #

    def show_pdf(self, parent):
        dummy = 0
        self.send_pdf(parent, dummy)
        line = 'show'
        suite.discus_calc_pdf(line)
        #

    def send_pdf(self, parent, dummy):
        #
        line = 'ides all'
        suite.discus_calc_pdf(line)
        line = 'jdes all'
        suite.discus_calc_pdf(line)
        line = 'isel all'
        suite.discus_calc_pdf(line)
        line = 'jsel all'
        suite.discus_calc_pdf(line)
        #
        line = 'set range, ' + str(self.lim_max.get()) + ', ' \
                             + str(self.lim_step.get())
        suite.discus_calc_pdf(line)
        #
        if self.rho0_type.get() == 1:
            line = 'set dens, auto'
        else:
            line = 'set dens, ' + str(self.rho0.get())
        suite.discus_calc_pdf(line)
        #
        line = 'set corrlin, ' + str(self.corr_lin.get())
        suite.discus_calc_pdf(line)
        line = 'set corrquad, ' + str(self.corr_quad.get())
        suite.discus_calc_pdf(line)
        #
        if self.peri_type.get() == 0:
           line = 'set boundary, crystal, exact'
        else:
           line = 'set boundary, period, 3D'
        suite.discus_calc_pdf(line)
        #
        line = 'set weight, ' + str(self.weight.get())
        suite.discus_calc_pdf(line)
        #
        if self.finite_type.get() == 0:
            line = 'set finite, period'
        elif self.finite_type.get() == 1:
            line = 'set finite, sphere,' + str(self.sphere.get())
        suite.discus_calc_pdf(line)
        #
        if is_empty(self.rad.curselection()):
           line = 'set rad, xray'
        else:
           if int(self.rad.curselection()[0])==0:
               line = 'set rad, xray'
           elif int(self.rad.curselection()[0])==1:
               line = 'set rad, neutron'
           elif int(self.rad.curselection()[0])==2:
               line = 'set rad, electron'
           else :
               line = 'set rad, xray'
        suite.discus_calc_pdf(line)
        #
        if self.adp.get() == 1:
           line = ('set therm, gauss')
        elif self.adp.get() == 0:
           line = ('set therm, off')
        suite.discus_calc_pdf(line)
        #
        line = 'set qmax, '  + str(self.qmax.get())
        suite.discus_calc_pdf(line)
        #
        line = 'set qbroad, '  + str(self.qbroad.get())
        suite.discus_calc_pdf(line)
        #
        line = 'set qdamp, '  + str(self.qdamp.get())
        suite.discus_calc_pdf(line)

    def exit_command(self, parent,i):
        i=1
        self.send_pdf(parent,i)
        line = 'exit'
        suite.discus_calc_pdf(line)
