import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from support import COLORS, control_label, turn_on, turn_off
from exit_button import create_exit_button
from macro_section import create_macro_menu
from command_lang import create_command_language
from lib_discus_suite import *

class KUPLOT_LOAD_FR(tk.Frame):
   def __init__ (self, parent):
      tk.Frame.__init__ ( self, parent )
      self.config(borderwidth=2, relief=tk.RAISED, background=COLORS.fr_read)
      self.grid(row=3,column=0,columnspan=6, sticky='EW')

      self.filename = tk.StringVar()
      self.caption=ttk.Label(self, text="Load a data set")
      self.fileb = ttk.Button(self, text="File",
              command=lambda: self.filename.set(filedialog.askopenfilename())
              )
      self.isfiletype = tk.StringVar()
      self.l_type=ttk.Label(self, text="Filetype: ", relief=tk.RAISED)
      self.ftype = ttk.Combobox(self, textvariable=self.isfiletype,
              state='readonly'
              )
      self.ftype['values'] = ('xy','ni')
      self.ftype.current(0)
      self.label_fle = ttk.Label(self, textvariable=self.filename, relief=tk.RAISED)
      self.acc = ttk.Button(self, text="Run", command=self.load_file)
      create_exit_button(self, 'kuplot', 3, 3, create_exit_button.donothing,(0,0))

      self.caption.grid(row=0, column=0, columnspan=5)
      self.fileb.grid(row=1, column=0)
      self.label_fle.grid(row=1, column=1, columnspan=3)
      self.l_type.grid(row=2, column=0)
      self.ftype.grid(row=2, column=1)
      self.acc.grid(row=3, column=2)
#     self.cancel.grid(row=3, column=3)


   def load_file(self):
      if self.ftype.get() == "xy":
         line = "xy," + str(self.filename.get())
      elif self.ftype.get() == "ni":
         line = "ni," + str(self.filename.get())
      suite.kuplot_load(line)

class kuplot_gui(tk.Frame):
   def __init__(self, parent, user):
      tk.Frame.__init__ ( self, parent )
      self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_kuplot)
      self.grid(row=3, column=0, columnspan=6, sticky='EW')

      self.kuplot_name = ttk.Label(self, text="KUPLOT SECTION")
      self.b_filemenu  = ttk.Menubutton(self, text="File")
      self.b_reset = ttk.Button(self, text="Reset",
              command=lambda: suite.execute_command("kuplot","reset")
              )
      self.b_plot  = ttk.Button(self, text="Plot", 
              command=lambda: suite.execute_command("kuplot","plot")
              )
      create_macro_menu(    self, "kuplot",1, 3)
      create_command_language(self, 'kuplot', 1,5)
      self.b_help  = ttk.Button(self, text="Help", command=lambda: self.kuplot_help(user))
#
      self.b_filemenu.menu=tk.Menu(self.b_filemenu, tearoff=0 )
      self.b_filemenu['menu'] = self.b_filemenu.menu
      self.b_filemenu.menu.add_command( label="Load", 
              command=lambda: KUPLOT_LOAD_FR(self),
              activeforeground=COLORS.ok_active, foreground=COLORS.ok_front)

#
#  Place all elements
#
      self.kuplot_name.grid(row=0, column=0, columnspan=5, sticky=tk.N)
      self.b_filemenu.grid(row=1, column=0, sticky='EW')
      self.b_help.grid(row=1, column=6, sticky=tk.W)
      self.b_reset.grid(row=2, column=0, sticky=tk.W)
      self.b_plot.grid(row=2, column=1, sticky=tk.W)

   def donothing(self):
      nthg = DO_NOTHING()


   def kuplot_help(self, user):
      turn_off(self.b_filemenu, self.b_cmd, self.b_macro,
               self.b_reset, self.b_plot)
      control_label(self,"help","kuplot",3)
      # Activate for current user type
      if user.get() == 0:
          turn_on(self.b_filemenu, self.b_macro,
                  self.b_reset, self.b_plot)
      else:
          turn_on(self.b_filemenu, self.b_cmd, self.b_macro,
                  self.b_reset, self.b_plot)

