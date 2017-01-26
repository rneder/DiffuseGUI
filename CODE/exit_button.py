import tkinter as tk
from tkinter import ttk
from loop_defs import *

class create_exit_button(ttk.Button):
   def __init__(self,parent, prog, pos_row, pos_col):
      self.parent=parent
      parent.b_exit = ttk.Button(parent, text="Exit", 
                      command=self.run_exit)
#                     activeforeground=COLORS.ok_active,
#                     foreground=COLORS.ok_front)
      parent.b_exit.grid(row=pos_row,column=pos_col)
      self.prog = prog

   def run_exit(self):
      LOOPS.do_send_command(self.prog, "exit")
      self.parent.destroy()
