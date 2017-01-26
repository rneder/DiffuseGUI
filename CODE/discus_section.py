import tkinter as tk
import numpy as np
import math as math
from tkinter import ttk
from tkinter import filedialog
from support import *
from exit_button import *
from macro_section import *
from loop_section import *
from conditional_section import *
from lib_discus_suite import *

def file_open(parent):
   parent.filename.set(filedialog.askopenfilename())
   if parent.filename.get() != 'Filename undefined' :
      parent.acc.configure(state='normal')

class READ_CELL_FR(tk.Frame):
   def __init__(self, parent):
      tk.Frame.__init__ ( self, parent )
#     self.configure(style= "Read.Discus.TFrame")
      self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_read)
      self.grid(row=2,column=0,columnspan=6)

      self.cell_type = tk.IntVar()
      self.cell_type.set(0)
      self.filename = tk.StringVar()
      self.filename.set('Filename undefined')
      self.caption=ttk.Label(self, text="Expand an asymmetric unit from file")
      self.fileb = ttk.Button(self, text="Open",
                   command=lambda: file_open(self))
#                  command=self.filename.set(filedialog.askopenfilename()))
      self.treat = ttk.Label(self, text="Treat atoms with\nequal names as:")
      self.label_fle = ttk.Label(self, textvariable=self.filename, relief=tk.RAISED)
      self.R1 = tk.Radiobutton(self,text="Equal types ",variable=self.cell_type,value=0,
                activeforeground="#F00",foreground="#00F")
      self.R2 = tk.Radiobutton(self,text="Sep. types",variable=self.cell_type,value=1,
                activeforeground="#F00",foreground="#00F")
      self.exp = ttk.Label(self, text="Expand to unit cells:")
      self.nx_l = ttk.Label(self, text="NX:")
      self.ny_l = ttk.Label(self, text="NY:")
      self.nz_l = ttk.Label(self, text="NZ:")
      self.nx = tk.Spinbox(self, from_=1, to=1000)
      self.ny = tk.Spinbox(self, from_=1, to=1000)
      self.nz = tk.Spinbox(self, from_=1, to=1000)
      self.acc = ttk.Button(self, text="Run", command=lambda: self.display_file(parent))
      create_exit_button(self,'discus',6,3)
  
 

      self.caption.grid(row=0,column=0,columnspan=5)
      self.fileb.grid(row=1,column=0)
      self.treat.grid(row=1,column=3)
      self.R1.grid(row=2,column=3,sticky=tk.W)
      self.R2.grid(row=3,column=3,sticky=tk.W)
      self.exp.grid(row=3,column=0,columnspan=2)
      self.nx_l.grid(row=4,column=0)
      self.ny_l.grid(row=5,column=0)
      self.nz_l.grid(row=6,column=0)
      self.nx.grid(row=4,column=1)
      self.ny.grid(row=5,column=1)
      self.nz.grid(row=6,column=1)
      self.acc.grid(row=6,column=2)
#     self.cancel.grid(row=6,column=3)
      self.label_fle.grid(row=2,column=0,columnspan=3)
      self.acc.configure(state='disabled')

#  def file_open(self):
#     self.filename.set(filedialog.askopenfilename())

   def display_file(self, parent):
      if self.cell_type.get() == 0:
         cmd = "cell"
      elif self.cell_type.get() == 1 :
         cmd = "lcell"
      else :
         cmd = "cell"
      line = (cmd + " " + str(self.filename.get()) + "," + str(self.nx.get()) +
                          "," + str(self.ny.get()) + "," + str(self.nz.get())   )
      print(line)
      suite.discus_read_structure(line)
      parent.b_strumenu.menu.entryconfig(3,state="normal")
      parent.b_strumenu.menu.entryconfig(4,state="normal")
      parent.b_strumenu.menu.entryconfig(6,state="normal")
      parent.b_fourmenu.configure(state='normal')
      # Close menu
      self.destroy()

class READ_STRU_FR(tk.Frame):
   def __init__(self, parent):
      tk.Frame.__init__ ( self, parent )
#     self.configure(style= "Read.Discus.TFrame")
      self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_read)
      self.grid(row=2,column=0,columnspan=6)

      self.cell_type = tk.IntVar()
      self.cell_type.set(0)
      self.filename = tk.StringVar()
      self.filename.set('Filename undefined')
      self.caption=ttk.Label(self, text="Read an old structure from file")
      self.fileb = ttk.Button(self, text="Open",
                   command=lambda: file_open(self))
      self.label_fle = ttk.Label(self, textvariable=self.filename, relief=tk.RAISED)
      self.acc = ttk.Button(self, text="Run", command=lambda: self.display_file(parent))
      create_exit_button(self,'discus',6,3)

      self.caption.grid(row=0,column=0,columnspan=5)
      self.fileb.grid(row=1,column=0)
      self.label_fle.grid(row=2,column=0,columnspan=3)
      self.acc.grid(row=6,column=2)
      self.acc.configure(state='disabled')

#  def file_open(self):
#     self.filename.set(filedialog.askopenfilename())

   def display_file(self, parent):
      line = ('stru' + " " + str(self.filename.get()))
      suite.discus_read_structure(line)
      parent.b_strumenu.menu.entryconfig(3,state="normal")
      parent.b_strumenu.menu.entryconfig(4,state="normal")
      parent.b_strumenu.menu.entryconfig(6,state="normal")
      parent.b_fourmenu.configure(state='normal')

class SINGLE_FOUR_FR(tk.Frame):
   def __init__(self, parent):
      tk.Frame.__init__ ( self, parent )
#     self.configure(style= "Read.Discus.TFrame")
      self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_read)
      self.grid(row=2,column=0,columnspan=8)

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
      self.ll_h.set('0.0')
      self.ll_k.set('0.0')
      self.ll_l.set('0.0')
      self.lr_h.set('4.0')
      self.lr_k.set('0.0')
      self.lr_l.set('0.0')
      self.ul_h.set('0.0')
      self.ul_k.set('4.0')
      self.ul_l.set('0.0')
      self.tl_h.set('0.0')
      self.tl_k.set('0.0')
      self.tl_l.set('0.0')
      self.caption=ttk.Label(self, text="Single crystal Fourier calculations")
      self.label_h = ttk.Label(self,text='H')
      self.label_k = ttk.Label(self,text='K')
      self.label_l = ttk.Label(self,text='L')
      self.label_ll = ttk.Label(self,text='Lower left')
      self.label_lr = ttk.Label(self,text='Lower right')
      self.label_ul = ttk.Label(self,text='Upper left')
      self.label_tl = ttk.Label(self,text='Top left')
      self.entry_ll_h = ttk.Entry(self,textvariable=self.ll_h, width=8,justify='right')
      self.entry_ll_k = ttk.Entry(self,textvariable=self.ll_k, width=8,justify='right')
      self.entry_ll_l = ttk.Entry(self,textvariable=self.ll_l, width=8,justify='right')
      self.entry_lr_h = ttk.Entry(self,textvariable=self.lr_h, width=8,justify='right')
      self.entry_lr_k = ttk.Entry(self,textvariable=self.lr_k, width=8,justify='right')
      self.entry_lr_l = ttk.Entry(self,textvariable=self.lr_l, width=8,justify='right')
      self.entry_ul_h = ttk.Entry(self,textvariable=self.ul_h, width=8,justify='right')
      self.entry_ul_k = ttk.Entry(self,textvariable=self.ul_k, width=8,justify='right')
      self.entry_ul_l = ttk.Entry(self,textvariable=self.ul_l, width=8,justify='right')
      self.entry_tl_h = ttk.Entry(self,textvariable=self.tl_h, width=8,justify='right')
      self.entry_tl_k = ttk.Entry(self,textvariable=self.tl_k, width=8,justify='right')
      self.entry_tl_l = ttk.Entry(self,textvariable=self.tl_l, width=8,justify='right')
      self.label_np   = ttk.Label(self,text='Points along axis:')
      self.label_np_a = ttk.Label(self,text='Abscissa')
      self.label_np_o = ttk.Label(self,text='Ordinate')
      self.label_np_t = ttk.Label(self,text='Top axis')
      self.np_aa = tk.StringVar()
      self.np_aa.set('201')
      self.np_oo = tk.StringVar()
      self.np_oo.set('201')
      self.np_tt = tk.StringVar()
      self.np_tt.set('1')
      self.np_a = tk.Spinbox(self, from_=1, to=1001,textvariable=self.np_aa)
      self.np_o = tk.Spinbox(self, from_=1, to=1001,textvariable=self.np_oo)
      self.np_t = tk.Spinbox(self, from_=1, to=1001,textvariable=self.np_tt)
      self.label_rad = ttk.Label(self,text='Radiation')
      self.rad = tk.Listbox(self, height=3, width=10,selectbackground='#FFFFFF',
                 selectforeground='#0000FF',selectmode=tk.SINGLE)
      self.rad.configure(exportselection=False)
      self.rad.insert(1,'X-ray')
      self.rad.insert(2,'neutron')
      self.rad.insert(3,'electron')
      self.rad.selection_set(0)
      self.rad.bind('<ButtonRelease-1>',self.convert_event)
      self.rad_type = tk.IntVar()
      self.rad_type.set(0)
      self.label_wvl = ttk.Label(self,text='Wavelength')
      self.R1 = tk.Radiobutton(self,text="Wave length",variable=self.rad_type,value=0,
                activeforeground="#F00",foreground="#00F", justify='left',
                command=lambda: self.convert_setup( 1))
      self.R2 = tk.Radiobutton(self,text="Energy",variable=self.rad_type,value=1,
                activeforeground="#F00",foreground="#00F", justify='left',
                command=lambda: self.convert_setup(-1))
      self.wvle = tk.StringVar()
      self.wvle.set('0.70900')
      self.ener = tk.StringVar()
      self.ener.set(str(12.398424/float(self.wvle.get())))
      self.label_wvle_unit = tk.Label(self,text='Ang')
      self.label_ener_unit = tk.Label(self,text='keV')
      self.entry_wvle = ttk.Entry(self,textvariable=self.wvle, width=10, justify='right')
      self.entry_wvle.bind('<FocusOut>',self.convert_focus)
      self.entry_wvle.bind('<Leave>',self.convert_focus)
      self.entry_ener = ttk.Entry(self,textvariable=self.ener, width=10, justify='right')
      self.adp = tk.IntVar()
      self.adp.set(1)
      self.label_adp = ttk.Label(self,text='ADP')
      self.check_adp = ttk.Checkbutton(self,text='Use',variable=self.adp)
#     self.check_adp.invoke()
      self.ano = tk.IntVar()
      self.ano.set(0)
      self.label_ano = ttk.Label(self,text='anomalous')
      self.check_ano = ttk.Checkbutton(self,text='Use',variable=self.ano)
      self.acc = ttk.Button(self, text="Run", command=lambda: self.calc_fourier(parent))
      create_exit_button(self,'discus',9,7)

      self.caption.grid(row=0,column=0,pady=(5,5),columnspan=8)
      self.label_h.grid(row=1,column=1,sticky='EW')
      self.label_k.grid(row=1,column=2,sticky='EW')
      self.label_l.grid(row=1,column=3,sticky='EW')
      self.label_ll.grid(row=2,column=0,sticky='EW')
      self.label_lr.grid(row=3,column=0,sticky='EW')
      self.label_ul.grid(row=4,column=0,sticky='EW')
      self.label_tl.grid(row=5,column=0,sticky='EW')
      self.entry_ll_h.grid(row=2,column=1,sticky='EW')
      self.entry_ll_k.grid(row=2,column=2,sticky='EW')
      self.entry_ll_l.grid(row=2,column=3,sticky='EW')
      self.entry_lr_h.grid(row=3,column=1,sticky='EW')
      self.entry_lr_k.grid(row=3,column=2,sticky='EW')
      self.entry_lr_l.grid(row=3,column=3,sticky='EW')
      self.entry_ul_h.grid(row=4,column=1,sticky='EW')
      self.entry_ul_k.grid(row=4,column=2,sticky='EW')
      self.entry_ul_l.grid(row=4,column=3,sticky='EW')
      self.entry_tl_h.grid(row=5,column=1,sticky='EW')
      self.entry_tl_k.grid(row=5,column=2,sticky='EW')
      self.entry_tl_l.grid(row=5,column=3,sticky='EW')
      self.label_np.grid(row=6,column=0,pady=(5,0),columnspan=2,sticky='EW')
      self.label_np_a.grid(row=7,column=0,sticky='EW')
      self.label_np_o.grid(row=8,column=0,sticky='EW')
      self.label_np_t.grid(row=9,column=0,sticky='EW')
      self.np_a.grid(row=7,column=1,columnspan=3,sticky='EW')
      self.np_o.grid(row=8,column=1,columnspan=3,sticky='EW')
      self.np_t.grid(row=9,column=1,columnspan=3,sticky='EW')
      self.label_rad.grid(row=2,column=4,padx=(5,0),sticky='EW')
      self.rad.grid(row=1,column=5,rowspan=3,sticky='EW')
      self.R1.grid(row=2,column=6,sticky='EW')
      self.R2.grid(row=3,column=6,sticky='EW')
      self.entry_wvle.grid(row=2,column=7,sticky='EW')
      self.label_wvle_unit.grid(row=2,column=8,sticky='W')
      self.entry_ener.grid(row=3,column=7,sticky='EW')
      self.label_ener_unit.grid(row=3,column=8,sticky='W')
      self.label_adp.grid(row=4,column=4,padx=(5,0),sticky='EW')
      self.check_adp.grid(row=4,column=5,sticky='EW')
      self.label_ano.grid(row=5,column=4,padx=(5,0),sticky='EW')
      self.check_ano.grid(row=5,column=5,sticky='EW')
      self.acc.grid(row=9,column=6)
      self.entry_ener.configure(state='disabled')

   def convert_event(self, event):
      # Change of radiation (X-ray, neutron, electron)
      if is_empty(self.rad.curselection()):
         radiation = 0
      else:
         radiation = int(self.rad.curselection()[0])
      # calculate wavelength if Radiobutton is in state Energy
      calc_wvle = self.rad_type.get() == 1
      print(calc_wvle)
      print('RADIATION ',radiation)
      print('Event     ', event)
      self.convert(calc_wvle)
      if radiation == 1:
         self.label_ener_unit['text']='meV'
      else:
         self.label_ener_unit['text']='keV'

   def convert_focus(self, event):
      # calculate wavelength if Radiobutton is in state Energy
      calc_wvle = self.rad_type.get() == 1
      self.convert(calc_wvle)
      

   def convert_setup(self, mode):
      if mode == 0:
         # Change of radiation (X-ray, neutron, electron)
         # calculate wavelength if Radiobutton is in state Energy
         calc_wvle = self.rad_type.get() == 1
      elif mode == 1:
         # Change of energy ==> wavelength Radiobutton
         calc_wvle = True
         self.entry_wvle.configure(state='normal')
         self.entry_ener.configure(state='disabled')
      elif mode ==-1:
         # Change of wavelength ==> energy Radiobutton
         calc_wvle = False
         self.entry_wvle.configure(state='disabled')
         self.entry_ener.configure(state='normal')
      elif mode == 2:
         # wavelength value was entered calc energy
         calc_wvle = False
      elif mode == -2:
         # energy value was entered calc wavelength
         calc_wvle = True
      self.convert(calc_wvle)

   def convert(self, calc_wvle):
      if is_empty(self.rad.curselection()):
         radiation = 0
      else:
         radiation = int(self.rad.curselection()[0])
      print('Radiation  type ', radiation)
      if calc_wvle:
         # Calculate wavelength from current energy
         energy = float(self.ener.get())
         if radiation == 0:
            # X-rays
            wvle = (CONSTANTS.planck*CONSTANTS.light/CONSTANTS.charge ) / energy
         elif radiation == 1:
            # neutrons
            wvle = CONSTANTS.planck/math.sqrt(2.*CONSTANTS.mass_n*CONSTANTS.charge*energy/10.)
         elif radiation == 2:
            # electrons
            wvle = CONSTANTS.planck/math.sqrt(2.*CONSTANTS.mass_e*CONSTANTS.charge*energy*10) / \
                   math.sqrt(1.+(CONSTANTS.charge*energy)/(2*CONSTANTS.mass_e*CONSTANTS.light**2*10))
         self.wvle.set(str(wvle))
      else:
         # Calculate energy from current wavelength
         wvle = float(self.wvle.get())
         if radiation == 0:
            # X-rays
            energy = (CONSTANTS.planck*CONSTANTS.light/CONSTANTS.charge ) / wvle
         elif radiation == 1:
            # neutrons
            energy = CONSTANTS.planck**2/(2.*CONSTANTS.mass_n*CONSTANTS.charge*wvle**2/10.)
         elif radiation == 2:
            # electrons
            energy = -10.*CONSTANTS.mass_e*CONSTANTS.light**2/CONSTANTS.charge +  \
                    math.sqrt( 100.*CONSTANTS.mass_e**2*CONSTANTS.light**4/CONSTANTS.charge**2 + \
                    ((CONSTANTS.planck*CONSTANTS.light)/(CONSTANTS.charge*wvle))**2)
         self.ener.set(str(energy))

   def calc_fourier(self, parent):
      self.send_fourier()
      # Close menu
      self.destroy()

   def send_fourier(self):
      line = ('ll' + " " + str(self.entry_ll_h.get()) 
                   + "," + str(self.entry_ll_k.get())
                   + "," + str(self.entry_ll_l.get())
             )
      print(line)
      suite.discus_calc_fourier(line)
      line = ('lr' + " " + str(self.entry_lr_h.get()) 
                   + "," + str(self.entry_lr_k.get())
                   + "," + str(self.entry_lr_l.get())
             )
      print(line)
      suite.discus_calc_fourier(line)
      line = ('ul' + " " + str(self.entry_ul_h.get()) 
                   + "," + str(self.entry_ul_k.get())
                   + "," + str(self.entry_ul_l.get())
             )
      print(line)
      suite.discus_calc_fourier(line)
      line = ('na' + " " + str(self.np_a.get()))
      suite.discus_calc_fourier(line)
      line = ('no' + " " + str(self.np_o.get()))
      suite.discus_calc_fourier(line)
      line = ('nt' + " " + str(self.np_t.get()))
      suite.discus_calc_fourier(line)
#
      print(' Radiation ', self.rad.curselection())
      if is_empty(self.rad.curselection()):
         radiation = 0
      else:
         radiation = int(self.rad.curselection()[0])
      if radiation   == 0:
         line = "xray"
      elif radiation   == 1:
         line = "neutron"
      elif radiation   == 2:
         line = "electron"
      else :
         line = "xray"
      suite.discus_calc_fourier(line)
      print('RADIATION_TYPE ', str(self.rad_type.get()))
      if self.rad_type.get() == 0:
         line = ('wvle' + " " + str(self.entry_wvle.get()))
      elif self.rad_type.get() == 1:
         line = ('energy' + " " + str(self.entry_wvle.get()))
      suite.discus_calc_fourier(line)
      print('ADP      _TYPE ', str(self.adp.get()))
      if self.adp.get() == 1:
         line = ('temp use')
      elif self.adp.get() == 0:
         line = ('temp ignore')
      suite.discus_calc_fourier(line)
      print('ANO      _TYPE ', str(self.ano.get()))
      if self.ano.get() == 1:
         line = ('disp anom')
      elif self.ano.get() == 0:
         line = ('disp off')
      suite.discus_calc_fourier(line)
#
      line= ('show')
      suite.discus_calc_fourier(line)
      line= ('run')
      suite.discus_calc_fourier(line)

class discus_gui(tk.Frame):
   def __init__(self, parent, user):
      tk.Frame.__init__ ( self, parent)
      self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_discus)
#      self.configure(style= "Discus.TFrame")
      self.grid(row=2,column=0,columnspan=7,sticky='EW')

      self.discus_name = ttk.Label(self, text="DISCUS SECTION")
#
      self.b_strumenu  = ttk.Menubutton(self, text="Build a basic\nStructure",
                         style='Basic.TButton')
      self.b_fourmenu  = ttk.Menubutton(self, text="Calculate PDF / \nFourier / Powder",
                         style='Basic.TButton')
      self.b_session   = ttk.Button(self, text="Interactive\nSession", command=self.discus_session)
      create_command_button(self, 'discus',1, 3)
      create_macro_menu(    self, 'discus',1, 4)
      create_loop_menu(     self, 'discus',1, 5)
      create_if_menu(       self, 'discus',1, 6)
      self.b_help  = ttk.Button(self, text="Help", command=lambda: self.discus_help(user))
#     create_exit_button(self,'discus',1,7)
#
      self.b_strumenu.menu=tk.Menu(self.b_strumenu, tearoff=0 )
      self.b_strumenu['menu'] = self.b_strumenu.menu
      self.b_strumenu.menu.add_command( label='Expand asymmetric unit',
                               command=lambda: READ_CELL_FR(self),
                               activeforeground="#F00",foreground="#00F")
      self.b_strumenu.menu.add_command(label="Read old structure", 
                               command=lambda: READ_STRU_FR(self),
                               activeforeground="#F00",foreground="#00F")
      self.b_strumenu.menu.add_command(label="Define empty free space", command=self.donothing)
      self.b_strumenu.menu.add_command(label="Save ", command=self.donothing)
      self.b_strumenu.menu.add_command(label="Plot ", command=self.donothing)
      self.b_strumenu.menu.add_command(label="Import", command=self.donothing)
      self.b_strumenu.menu.add_command(label="Export", command=self.donothing)
#
      self.b_strumenu.menu.entryconfig(3,state="disabled")
      self.b_strumenu.menu.entryconfig(4,state="disabled")
      self.b_strumenu.menu.entryconfig(6,state="disabled")
#
      self.b_fourmenu.menu=tk.Menu(self.b_fourmenu, tearoff=0 )
      self.b_fourmenu['menu'] = self.b_fourmenu.menu
      self.b_fourmenu.menu.add_command( label='Calculate Fourier',
                               command=lambda: SINGLE_FOUR_FR(self),
                               activeforeground="#F00",foreground="#00F")
      self.b_fourmenu.menu.add_command( label='Zone Axis Pattern',
                               command=lambda: SINGLE_FOUR_FR(self),
                               activeforeground="#F00",foreground="#00F")
      self.b_fourmenu.menu.add_separator()
      self.b_fourmenu.menu.add_command( label='Powder Pattern',
                               command=lambda: SINGLE_FOUR_FR(self),
                               activeforeground="#F00",foreground="#00F")
      self.b_fourmenu.menu.add_command( label='PDF',
                               command=lambda: SINGLE_FOUR_FR(self),
                               activeforeground="#F00",foreground="#00F")
      self.b_fourmenu.menu.add_separator()
      self.b_fourmenu.menu.add_command( label='Save Pattern',
                               command=lambda: SINGLE_FOUR_FR(self),
                               activeforeground="#F00",foreground="#00F")
      self.b_fourmenu.menu.entryconfig(1,state="disabled")
      self.b_fourmenu.menu.entryconfig(3,state="disabled")
      self.b_fourmenu.menu.entryconfig(4,state="disabled")
      self.b_fourmenu.menu.entryconfig(6,state="disabled")
      self.b_fourmenu.configure(state='disabled')

#
#  Place all elements
#
      self.discus_name.grid(row=0, column=1, columnspan=5,sticky=tk.N)
      self.b_strumenu.grid(row=1, column=0, sticky=tk.W)
      self.b_fourmenu.grid(row=1, column=1, sticky=tk.W)
      self.b_session.grid(row=1, column=2, sticky=tk.W)
#     Command button at  (row=1, column=3, sticky=tk.W)
#     MacroButton at   (row=1, column=4, sticky=tk.W)
#     Loop Button at   (row=1, column=5 sticky=tk.W)
#     If   Button at   (row=1, column=6 sticky=tk.W)
      self.b_help.grid(row=1, column=7, sticky=tk.W)
#     self.b_exit.grid(row=1, column=9,sticky=tk.W)
#
#  ToolTips
#
      self.b_session_ttp = CreateToolTip(self.b_session,\
      "Start an interactive DISCUS session. Type 'exit' to leave the "
      "interactive session and to return to the GUI")
      self.b_strumenu_ttp = CreateToolTip(self.b_strumenu,\
      "The basic and typically the first step within DISCUS. " 
      "Read a structure from a file, build a unit cell by expanding "
      "the content of an asymmetric unit, import external formats. "
      "Includes the menu to save a structure")
      self.b_fourmenu_ttp = CreateToolTip(self.b_fourmenu,\
      "Calculate a diffraction pattern or a PairDistributionFunction. "
      " Active, once a structure has been build")
      self.b_help_ttp = CreateToolTip(self.b_help, \
      "Enter the help menu. Within the help menu you can obtain "
      "further info by typing any of the available words followed "
      "by a <RETURN> or <ENTER>." 
      "Return to the GUI with an empty line and <RETURN> or <ENTER> ")

   def donothing(self):
      nthg = DO_NOTHING()

   def discus_session(self):
      # Remember old states 
      fourmenu_state = self.b_fourmenu.state()
      # Temporarily turn off
      turn_off(self.b_strumenu, self.b_command, self.b_macro, self.b_loop, self.b_if, self.b_help)
      control_label(self, "interactive", "discus", 2)
      turn_on(self.b_strumenu, self.b_command, self.b_macro, self.b_loop, self.b_if, self.b_help)
      # For all users return menus to previous state if active
      if is_empty(fourmenu_state):
          turn_on(self.b_fourmenu)

   def discus_help(self, user):
      # Remember old states 
      fourmenu_state = self.b_fourmenu.state()
      # Temporarily turn off
      turn_off(self.b_session,self.b_strumenu, self.b_fourmenu, self.b_command, 
               self.b_loop, self.b_if, self.b_macro)
      control_label(self, "help", "discus", 2)
      # Activate for current user type
      if user.get() == 0: 
         turn_on(self.b_strumenu, self.b_macro)
      else:
         turn_on(self.b_session,self.b_strumenu, self.b_command, 
         self.b_macro, self.b_loop, self.b_if)
      # For all users return menus to previous state if active
      if is_empty(fourmenu_state):
          turn_on(self.b_fourmenu)

