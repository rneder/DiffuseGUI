import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from loop_defs import *
from support import *
from lib_discus_suite import *

class macro_gui(tk.Frame):
   def __init__(self, parent, prog, mode):
      tk.Frame.__init__ ( self, parent )
      if prog == 'suite':
         self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_back)
         self.grid(row=1,column=0,columnspan=4)
      elif prog == 'discus':
         self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_read)
         self.grid(row=2,column=0,columnspan=6)
      elif prog == 'kuplot':
         self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_read)
         self.grid(row=3,column=0,columnspan=6)

      self.macrofilename = tk.StringVar()
      self.macrofilename.set("Undefined")
      self.section_name = prog
      self.num_par = tk.IntVar()
      self.num_par.set(0)
      self.num_par_old = tk.IntVar()
      self.num_par_old.set(0)
      self.parent=parent

      if mode == "run" :
         self.menu_run()
      elif mode == "learn":
         self.menu_learn()
      elif mode == "lend":
         self.menu_lend()

   def menu_run(self):
      self.l_titl = ttk.Label(self, text="Macro Run Menu")
      self.b_open = ttk.Button(self, text="Open", command=self.file_open)
      self.l_file = ttk.Label(self, textvariable=self.macrofilename, relief=tk.RAISED)
      self.run    = ttk.Button(self, text="Run",  command=self.macro_run)
      self.cancel = ttk.Button(self, text="Exit", command=self.destroy)

      self.l_titl.grid(row=0,column=0,columnspan=3, sticky=tk.N)
      self.b_open.grid(row=1,column=0, sticky=tk.W)
      self.l_file.grid(row=2,column=0,columnspan=3, sticky=tk.W)
      self.run.grid(row=4,column=1, sticky=tk.E)
      self.cancel.grid(row=4,column=2, sticky=tk.E)

   def menu_learn(self):
      self.l_titl = ttk.Label(self, text="Macro Learn Menu")
      self.b_open = ttk.Button(self, text="Save As", command=self.file_save)
      self.l_file = ttk.Label(self, textvariable=self.macrofilename, relief=tk.RAISED)
      self.run    = ttk.Button(self, text="OK",  command=self.macro_learn)
      self.cancel = ttk.Button(self, text="Exit", command=self.destroy)

      self.l_titl.grid(row=0,column=0,columnspan=3, sticky=tk.N)
      self.b_open.grid(row=1,column=0, sticky=tk.W)
      self.l_file.grid(row=2,column=0,columnspan=3, sticky=tk.W)
      self.run.grid(row=4,column=1, sticky=tk.E)
      self.cancel.grid(row=4,column=2, sticky=tk.E)

   def file_open(self):
      self.macrofilename.set(filedialog.askopenfilename())
      line = str(self.macrofilename.get())
      number = suite.test_macro_param(line)
      self.num_par.set(number)
      if self.num_par.get() < self.num_par_old.get() :
         for x in range(self.num_par_old.get()) :
            self.entry_widgets[x].grid_forget()
            self.label_widgets[x].grid_forget()
      self.entry_widgets = [self.create_entry_widget(x) for x in range(self.num_par.get())]
      self.label_widgets = [self.create_label_widget(x) for x in range(self.num_par.get())]
      self.num_par_old.set(self.num_par.get())

   def file_save(self):
      self.macrofilename.set(filedialog.asksaveasfilename())

   def macro_run(self):
      line ="@" + str(self.macrofilename.get()) + " "
      if self.num_par.get() == 1 :
         line = line + str(self.entry_widgets[0].get())
      elif self.num_par.get() > 1 :
         for x in range(self.num_par.get()-1) :
            line = line + str(self.entry_widgets[x].get()) + ","
         line = line + str(self.entry_widgets[self.num_par.get()-1].get())
      
      if LOOPS.lblock_read:
         LOOPS.do_send_command(self.section_name, line)
      else:
         suite.execute_macro(self.section_name, line)

   def macro_learn(self):
      line ="learn " + str(self.macrofilename.get()) + " "
      suite.execute_command(self.section_name, line)
      self.parent.b_macro.menu.entryconfig(1,state="disabled")
      self.parent.b_macro.menu.entryconfig(2,state="normal")

   def  menu_lend(self):
      line ="lend "
      suite.execute_command(self.section_name, line)
      self.parent.b_macro.menu.entryconfig(1,state="normal")
      self.parent.b_macro.menu.entryconfig(2,state="disabled")
      
   def create_entry_widget(self, x):
      new_widget = tk.Entry(self) 
      new_widget.grid(row=5+x,column=1,columnspan=2)
      new_widget.insert(0,x+1)
      return new_widget
      
   def create_label_widget(self, x):
      new_label  = ttk.Label(self, text="Parameter " + str(x+1) + ":") 
      new_label.grid(row=5+x,column=0,)
      return new_label
#
#  Build a macro MenuButton
#
def create_macro_menu(parent,prog,pos_row,pos_col):
#
      parent.b_macro = ttk.Menubutton(parent, text="Macros") #, relief=tk.RAISED)

      parent.b_macro.menu = tk.Menu(parent.b_macro, tearoff=0)
      parent.b_macro['menu'] = parent.b_macro.menu
      parent.b_macro.menu.add_command(label="Run", 
                       command=lambda : macro_gui(parent,prog,"run"),
                       activeforeground=COLORS.ok_active,
                       foreground=COLORS.ok_front)
      parent.b_macro.menu.add_command(label="Learn",
                       command=lambda : macro_gui(parent,prog,"learn"),
                       activeforeground=COLORS.ok_active,
                       foreground=COLORS.ok_front)
      parent.b_macro.menu.add_command(label="Finish Learn",
                       command=lambda : macro_gui(parent,prog,"lend"),
                       activeforeground=COLORS.ok_active,
                       foreground=COLORS.ok_front)
      parent.b_macro.menu.entryconfig(1,state="normal")
      parent.b_macro.menu.entryconfig(2,state="disabled")
      parent.b_macro.grid(row=pos_row, column=pos_col, sticky=tk.W)
      parent.b_macro_ttp = CreateToolTip(parent.b_macro,\
      "Load and execute a macro at the current DISCUS_SUITE section. "
      "A macro is a prerecorded list of DISCUS_SUITE commands, that "
      "optionally may take parameters. "
      "You can also start to record a macro within this menu")
