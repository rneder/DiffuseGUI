import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from support import *
from exit_button import *
from macro_section import *
from loop_section import *
from conditional_section import *
from lib_discus_suite import *

class diffev_gui(tk.Frame):
   def __init__(self, parent):
      tk.Frame.__init__ ( self, parent)
      self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_diffev)
#      self.configure(style= "Discus.TFrame")
      self.grid(row=4,column=0,columnspan=6)

      self.diffev_name = ttk.Label(self, text="DIFFEV SECTION")
      self.b_session   = ttk.Button(self, text="Session", command=self.diffev_session)
      create_command_button(self, 'diffev',1, 2)
      create_macro_menu(    self, 'diffev',1, 3)
      create_loop_menu(     self, 'diffev',1, 4)
      create_if_menu(       self, 'diffev',1, 5)
      self.b_help  = ttk.Button(self, text="Help", command=self.diffev_help)
#     create_exit_button(self,'diffev', 1,7)
#
#  Place all elements
#
      self.diffev_name.grid(row=0, column=0, columnspan=5,sticky=tk.N)
      self.b_session.grid(row=1, column=0, sticky=tk.W)
#     Command button at  (row=1, column=2, sticky=tk.W)
#     MacroButton at   (row=1, column=3, sticky=tk.W)
#     Loop Button at   (row=1, column=4, sticky=tk.W)
#     If   Button at   (row=1, column=5, sticky=tk.W)
      self.b_help.grid(row=1, column=6, sticky=tk.W)
#     self.b_exit.grid(row=1, column=7,sticky=tk.W)

   def donothing(self):
      nthg = DO_NOTHING()

   def diffev_session(self):
      turn_off(self.b_command, self.b_macro, self.b_help,self.b_exit)
      control_label(self, "interactive", "diffev", 2)
      turn_on(self.b_command, self.b_macro, self.b_help,self.b_exit)

   def diffev_help(self):
      turn_off(self.b_session, self.b_command, self.b_macro,self.b_exit)
      control_label(self, "help", "diffev", 2)
      turn_on(self.b_session, self.b_command, self.b_macro,self.b_exit)

