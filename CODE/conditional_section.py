import tkinter as tk
from tkinter import ttk
from loop_defs import *
from support import *
#from info_section import *
from lib_discus_suite import *

class   if_gui(tk.Frame):
   def __init__(self, parent, prog, mode):
      tk.Frame.__init__ ( self, parent )
      if prog == 'suite':
         self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_read)
         self.grid(row=3,column=0,columnspan=6)
      elif prog == 'discus':
         self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_read)
         self.grid(row=2,column=0,columnspan=6)
      elif prog == 'kuplot':
         self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_read)
         self.grid(row=3,column=0,columnspan=6)
      elif prog == 'diffev':
         self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_read)
         self.grid(row=3,column=0,columnspan=6)

      self.counter = tk.StringVar()
      self.start   = tk.StringVar()
      self.finish    = tk.StringVar()
      self.increment = tk.StringVar()
      self.counter.set("")
      self.start.set("")
      self.finish.set("")
      self.increment.set("1")
      self.section_name = prog
      self.parent=parent

      if mode == "if_start" :
         self.if_start()
      if mode == "if_else" :
         self.if_elseif()
      if mode == "else" :
         self.if_else()
      if mode == "endif" :
         self.if_endif()

   def if_start(self):
      self.l_tit = ttk.Label(self,text = "If conditional")
      self.l_var = ttk.Label(self,text = "Condition")
      self.e_var   = tk.Entry(self, textvariable=self.counter,bg="#FFFFFF")
      self.run     = ttk.Button(self, text="Define Content", command=lambda:self.initiate())
      self.cancel  = ttk.Button(self, text="Exit", command=self.destroy)

#     create_exit_button(self, self.section_name, 4,5)

      self.l_tit.grid(row=0,column=0,columnspan=2)
      self.l_var.grid(row=1,column=0)
      self.e_var.grid(row=1,column=1)
      self.run.grid(row=2,column=2)
      self.cancel.grid(row=3,column=2)

   def if_elseif(self):
      self.l_tit = ttk.Label(self,text = "ElseIf conditional")
      self.l_var = ttk.Label(self,text = "Condition")
      self.e_var   = tk.Entry(self, textvariable=self.counter,bg="#FFFFFF")
      self.run     = ttk.Button(self, text="Define Content", command=lambda:self.ifif_elseif())
      self.cancel  = ttk.Button(self, text="Exit", command=self.destroy)

      self.l_tit.grid(row=0,column=0,columnspan=2)
      self.l_var.grid(row=1,column=0)
      self.e_var.grid(row=1,column=1)
      self.run.grid(row=2,column=2)
      self.cancel.grid(row=3,column=2)

   def if_else(self):
      self.l_tit = ttk.Label(self,text = "Else block")
      self.run     = ttk.Button(self, text="Define Content", command=lambda:self.ifif_else())
      self.cancel  = ttk.Button(self, text="Exit", command=self.destroy)

      self.l_tit.grid(row=0,column=0,columnspan=2)
      self.run.grid(row=1,column=2)
      self.cancel.grid(row=2,column=2)

   def if_endif(self):
      line="endif"
      suite.gui_do_insert(self.section_name,line)
      number = LOOPS.level-1
      LOOPS.set_level(number)
      if LOOPS.level < 0:
         LOOPS.set_lblock_read(False)
         self.parent.b_if.menu.entryconfig(1,state="disabled")
         self.parent.b_if.menu.entryconfig(2,state="disabled")
         self.parent.b_if.menu.entryconfig(3,state="disabled")
         LOOPS.set_level(0)

   def initiate(self):
      global suite_gui_lblock_read
      line = ("if (" + str(self.counter.get()) + ") then" )
      self.parent.b_if.menu.entryconfig(1,state="normal")
      self.parent.b_if.menu.entryconfig(2,state="normal")
      self.parent.b_if.menu.entryconfig(3,state="normal")
      #if isinstance(self.parent.b_loop,self.parent):
      #   self.parent.b_loop.menu.entryconfig(3,state='disabled')
      if LOOPS.level == 0 and LOOPS.lblock_read == False:
         suite.gui_do_init(self.section_name,line)
         number = LOOPS.level
      else:
         suite.gui_do_insert(self.section_name,line)
         number = LOOPS.level+1
         LOOPS.set_level(number) #LOOPS.level+1)
      LOOPS.set_lblock_read(True)
      self.destroy()
      #INFO.insert(line)

   def ifif_elseif(self):
      global suite_gui_lblock_read
      line = ("elseif (" + str(self.counter.get()) + ") then" )
      self.parent.b_if.menu.entryconfig(1,state="normal")
      self.parent.b_if.menu.entryconfig(2,state="normal")
      self.parent.b_if.menu.entryconfig(3,state="normal")
      suite.gui_do_insert(self.section_name,line)
      LOOPS.set_lblock_read(True)
      self.destroy()
      #INFO.insert(line)

   def ifif_else(self):
      global suite_gui_lblock_read
      line = ("else")
      self.parent.b_if.menu.entryconfig(1,state="normal")
      self.parent.b_if.menu.entryconfig(2,state="normal")
      self.parent.b_if.menu.entryconfig(3,state="normal")
      suite.gui_do_insert(self.section_name,line)
      LOOPS.set_lblock_read(True)
      self.destroy()
      #INFO.insert(line)

#
#  Build a If MenuButton
#
def create_if_menu(parent,prog,pos_row,pos_col):
#
      parent.b_if = ttk.Menubutton(parent, text="Conditionals") #, relief=tk.RAISED)

      parent.b_if.menu = tk.Menu(parent.b_if, tearoff=0)
      parent.b_if['menu'] = parent.b_if.menu
      parent.b_if.menu.add_command(label="If", 
                       command=lambda : if_gui(parent,prog,"if_start"),
                       activeforeground=COLORS.ok_active,
                       foreground=COLORS.ok_front)
      parent.b_if.menu.add_command(label="Else if",
                       command=lambda : if_gui(parent,prog,"if_else"),
                       activeforeground=COLORS.ok_active,
                       foreground=COLORS.ok_front)
      parent.b_if.menu.add_command(label="Else",
                       command=lambda : if_gui(parent,prog,"else"),
                       activeforeground=COLORS.ok_active,
                       foreground=COLORS.ok_front)
      parent.b_if.menu.add_command(label="Finish If",
                       command=lambda : if_gui(parent,prog,"endif"),
                       activeforeground=COLORS.ok_active,
                       foreground=COLORS.ok_front)
      parent.b_if.menu.entryconfig(0,state="normal")
      parent.b_if.menu.entryconfig(1,state="disabled")
      parent.b_if.menu.entryconfig(2,state="disabled")
      parent.b_if.menu.entryconfig(3,state="disabled")
      parent.b_if.grid(row=pos_row, column=pos_col, sticky=tk.W)
      parent.b_if_ttp = CreateToolTip(parent.b_if,\
      "Define conditions that control the execution of command "
      "blocks.")
