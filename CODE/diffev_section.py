import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from support import COLORS, control_label, turn_on, turn_off
#from exit_button import *
from macro_section import create_macro_menu
#from loop_section import *
#from conditional_section import *
from command_lang import create_command_language
from lib_discus_suite import *

class diffev_gui(tk.Frame):
   def __init__(self, parent, user):
      tk.Frame.__init__ ( self, parent)
      self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_diffev)
      self.grid(row=4,column=0,columnspan=6)

      self.diffev_name = ttk.Label(self, text="DIFFEV SECTION")
      create_macro_menu(    self, 'diffev',1, 3)
      create_command_language(self, 'diffev', 1,5)
      self.b_help  = ttk.Button(self, text="Help", command=lambda: self.diffev_help(user))
#
#  Place all elements
#
      self.diffev_name.grid(row=0, column=0, columnspan=5,sticky=tk.N)
      self.b_help.grid(row=1, column=6, sticky=tk.W)

   def donothing(self):
      nthg = DO_NOTHING()


   def diffev_help(self, user):
      turn_off(self.b_cmd, self.b_macro)
      control_label(self, "help", "diffev", 2)
      # Activate for current user type
      if user.get() == 0:
         turn_on(self.b_cmd, self.b_macro)
      else:
         turn_on(self.b_cmd, self.b_macro)

