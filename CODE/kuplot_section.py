import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from support import *
from exit_button import *
from macro_section import *
from loop_section import *
from conditional_section import *
from lib_discus_suite import *

class KUPLOT_LOAD_FR(tk.Frame):
   def __init__ (self, parent):
      tk.Frame.__init__ ( self, parent )
      self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_read)
      self.grid(row=3,column=0,columnspan=6, sticky='EW')

      self.filename = tk.StringVar()
      self.caption=ttk.Label(self, text="Load a data set")
      self.fileb = ttk.Button(self, text="File",
                   command=lambda: self.filename.set(filedialog.askopenfilename()))
      self.isfiletype = tk.StringVar()
      self.l_type=ttk.Label(self,text="Filetype: ", relief=tk.RAISED)
      self.ftype = ttk.Combobox(self, textvariable=self.isfiletype,
                   state='readonly')
      self.ftype['values'] = ('xy','ni')
      self.ftype.current(0)
      self.label_fle = ttk.Label(self, textvariable=self.filename, relief=tk.RAISED)
      self.acc = ttk.Button(self, text="Run", command=self.load_file)
      create_exit_button(self, 'kuplot', 3,3)

      self.caption.grid(row=0,column=0,columnspan=5)
      self.fileb.grid(row=1,column=0)
      self.label_fle.grid(row=1,column=1,columnspan=3)
      self.l_type.grid(row=2,column=0)
      self.ftype.grid(row=2,column=1)
      self.acc.grid(row=3,column=2)
#     self.cancel.grid(row=3,column=3)

#  def file_open(self):
#     self.filename.set(filedialog.askopenfilename())

   def load_file(self):
      if self.ftype.get() == "xy":
         line = "xy," + str(self.filename.get())
      elif self.ftype.get() == "ni":
         line = "ni," + str(self.filename.get())
      suite.kuplot_load(line)

class kuplot_gui(tk.Frame):
   def __init__(self, parent):
      tk.Frame.__init__ ( self, parent )
      self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_kuplot)
      self.grid(row=3,column=0,columnspan=6,sticky='EW')

      self.kuplot_name = ttk.Label(self, text="KUPLOT SECTION")
      self.b_session   = ttk.Button(self, text="Session", command=self.kuplot_session)
      self.b_filemenu  = ttk.Menubutton(self, text="File")
      self.b_reset = ttk.Button(self, text="Reset",
                     command=lambda: suite.execute_command("kuplot","reset"))
      self.b_plot  = ttk.Button(self, text="Plot", 
                     command=lambda: suite.execute_command("kuplot","plot"))
      create_command_button(self, "kuplot",1, 2)
      create_macro_menu(    self, "kuplot",1, 3)
      create_loop_menu(     self, 'kuplot',1, 4)
      create_if_menu(       self, 'kuplot',1, 5)
      self.b_help  = ttk.Button(self, text="Help", command=self.kuplot_help)
#     create_exit_button(self, 'kuplot', 1,7)
#
      self.b_filemenu.menu=tk.Menu(self.b_filemenu, tearoff=0 )
      self.b_filemenu['menu'] = self.b_filemenu.menu
      self.b_filemenu.menu.add_command( label="Load", 
                               command=lambda: KUPLOT_LOAD_FR(self),
                               activeforeground="#F00",foreground="#00F")

#
#  Place all elements
#
      self.kuplot_name.grid(row=0, column=0, columnspan=5,sticky=tk.N)
      self.b_session.grid(row=1, column=1, sticky=tk.W)
      self.b_filemenu.grid(row=1, column=0, sticky='EW')
#     Command Button at  (row=1, column=2, sticky=tk.W)
#     MacroButton at   (row=1, column=3, sticky=tk.W)
      self.b_help.grid(row=1, column=6, sticky=tk.W)
      self.b_reset.grid(row=2, column=0, sticky=tk.W)
      self.b_plot.grid(row=2, column=1, sticky=tk.W)
#     self.b_exit.grid(row=1, column=5,sticky=tk.W)

   def donothing(self):
      nthg = DO_NOTHING()

   def kuplot_session(self):
      turn_off(self.b_filemenu, self.b_command, self.b_macro, self.b_help,
               self.b_reset, self.b_plot)
      control_label(self,"interactive","kuplot",3)
      turn_on(self.b_filemenu, self.b_command, self.b_macro, self.b_help,
               self.b_reset, self.b_plot)

   def kuplot_help(self):
      turn_off(self.b_session,self.b_filemenu, self.b_command, self.b_macro,
               self.b_reset, self.b_plot)
      control_label(self,"help","kuplot",3)
      turn_on(self.b_session,self.b_filemenu, self.b_command, self.b_macro,
               self.b_reset, self.b_plot)

