import tkinter as tk
from tkinter import ttk
from loop_defs import *
from support import *
#from info_section import *
from lib_discus_suite import *

class loop_gui(tk.Frame):
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

      if mode == "classic" :
         self.do_classic()
      if mode == "enddo" :
         self.do_enddo()

   def do_classic(self):
      self.l_tit = ttk.Label(self,text = "Do Loop")
      self.l_var = ttk.Label(self,text = "Loop counter")
      self.l_start=ttk.Label(self,text = "Start value ")
      self.l_finish = ttk.Label(self,text = "End value   ")
      self.l_inc = ttk.Label(self,text = "Increment   ")
      self.e_var   = tk.Entry(self, textvariable=self.counter,bg="#FFFFFF")
      self.e_start = tk.Entry(self, textvariable=self.start,bg="#FFFFFF")
      self.e_finish= tk.Entry(self, textvariable=self.finish,bg="#FFFFFF")
      self.e_inc   = tk.Entry(self, textvariable=self.increment,bg="#FFFFFF")
      self.run     = ttk.Button(self, text="Define Content", command=lambda:self.initiate())
      self.cancel  = ttk.Button(self, text="Exit", command=self.destroy)

#     create_exit_button(self, self.section_name, 4,5)

      self.l_tit.grid(row=0,column=0,columnspan=2)
      self.l_var.grid(row=1,column=0)
      self.l_start.grid(row=2,column=0)
      self.l_finish.grid(row=3,column=0)
      self.l_inc.grid(row=4,column=0)
      self.e_var.grid(row=1,column=1)
      self.e_start.grid(row=2,column=1)
      self.e_finish.grid(row=3,column=1)
      self.e_inc.grid(row=4,column=1)
      self.run.grid(row=3,column=5)
      self.cancel.grid(row=4,column=5)

   def initiate(self):
      global suite_gui_lblock_read
      line = ("do " + str(self.counter.get()) + "=" + str(self.start.get()) + "," 
                    + str(self.finish.get()) + "," + str(self.increment.get()))
      self.parent.b_loop.menu.entryconfig(3,state="normal")
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

   def do_enddo(self):
      line="enddo"
      suite.gui_do_insert(self.section_name,line)
      number = LOOPS.level-1
      LOOPS.set_level(number)
      if LOOPS.level < 0:
         LOOPS.set_lblock_read(False)
         self.parent.b_loop.menu.entryconfig(3,state="disabled")
         LOOPS.set_level(0)

#
#  Build a loop MenuButton
#
def create_loop_menu(parent,prog,pos_row,pos_col):
#
      parent.b_loop = ttk.Menubutton(parent, text="Loops") #, relief=tk.RAISED)

      parent.b_loop.menu = tk.Menu(parent.b_loop, tearoff=0)
      parent.b_loop['menu'] = parent.b_loop.menu
      parent.b_loop.menu.add_command(label="Do", 
                       command=lambda : loop_gui(parent,prog,"classic"),
                       activeforeground=COLORS.ok_active,
                       foreground=COLORS.ok_front)
      parent.b_loop.menu.add_command(label="Do While",
                       command=lambda : loop_gui(parent,prog,"while"),
                       activeforeground=COLORS.ok_active,
                       foreground=COLORS.ok_front)
      parent.b_loop.menu.add_command(label="Do ... Until",
                       command=lambda : loop_gui(parent,prog,"until"),
                       activeforeground=COLORS.ok_active,
                       foreground=COLORS.ok_front)
      parent.b_loop.menu.add_command(label="Finish Loop",
                       command=lambda : loop_gui(parent,prog,"enddo"),
                       activeforeground=COLORS.ok_active,
                       foreground=COLORS.ok_front)
      parent.b_loop.menu.entryconfig(1,state="normal")
      parent.b_loop.menu.entryconfig(3,state="disabled")
      parent.b_loop.grid(row=pos_row, column=pos_col, sticky=tk.W)
      parent.b_loop_ttp = CreateToolTip(parent.b_loop,\
      "Allows to repeat a set of commands/instructions")
