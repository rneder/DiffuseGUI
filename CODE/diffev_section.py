from tkinter import *
from tkinter import filedialog
from color_definitions import *
from do_nothing import *
from macro_section import *
from lib_discus_suite import *

class READ_CELL_FR(Frame):
   def __init__(self, parent):
      Frame.__init__ ( self, parent )
      self.config(borderwidth=2, relief=RAISED,background=COLORS.fr_read)
      self.grid(row=2,column=0,columnspan=6)

      self.cell_type = IntVar()
      self.cell_type.set(0)
      self.filename = StringVar()
      self.filename.set(' ')
      self.caption=Label(self, text="Read a unit cell file")
      self.fileb = Button(self, text="Open",command=self.file_open,
                     activeforeground=COLORS.ok_active,foreground=COLORS.ok_front)
      self.treat = Label(self, text="Treat atoms with\nequal names as:")
      self.label_fle = Label(self, textvariable=self.filename, relief=RAISED)
      self.R1 = Radiobutton(self,text="Equal types ",variable=self.cell_type,value=0,
                       activeforeground="#F00",foreground="#00F")
      self.R2 = Radiobutton(self,text="Sep. types",variable=self.cell_type,value=1,
                       activeforeground="#F00",foreground="#00F")
      self.exp = Label(self, text="Expand to unit cells:")
      self.nx_l = Label(self, text="NX:")
      self.ny_l = Label(self, text="NY:")
      self.nz_l = Label(self, text="NZ:")
      self.nx = Spinbox(self, from_=1, to=1000)
      self.ny = Spinbox(self, from_=1, to=1000)
      self.nz = Spinbox(self, from_=1, to=1000)
      self.acc = Button(self, text="Run", command=self.display_file,
                      activeforeground="#F00",foreground="#00F")
      self.cancel = Button(self, text="Exit", command=self.destroy,
                      activeforeground="#F00",foreground="#00F")
  
 

      self.caption.grid(row=0,column=0,columnspan=5)
      self.fileb.grid(row=1,column=0)
      self.treat.grid(row=1,column=3)
      self.R1.grid(row=2,column=3,sticky=W)
      self.R2.grid(row=3,column=3,sticky=W)
      self.exp.grid(row=3,column=0,columnspan=2)
      self.nx_l.grid(row=4,column=0)
      self.ny_l.grid(row=5,column=0)
      self.nz_l.grid(row=6,column=0)
      self.nx.grid(row=4,column=1)
      self.ny.grid(row=5,column=1)
      self.nz.grid(row=6,column=1)
      self.acc.grid(row=6,column=2)
      self.cancel.grid(row=6,column=3)
      self.label_fle.grid(row=2,column=0,columnspan=3)

   def file_open(self):
      self.filename.set(filedialog.askopenfilename())

   def display_file(self):
      if self.cell_type.get() == 0:
         cmd = "cell"
      elif self.cell_type.get() == 1 :
         cmd = "lcell"
      else :
         cmd = "cell"
      line = (cmd + " " + str(self.filename.get()) + "," + str(self.nx.get()) +
                          "," + str(self.ny.get()) + "," + str(self.nz.get())   )
      suite.py_read_structure(line)

class discus_gui(Frame):
   def __init__(self, parent):
      Frame.__init__ ( self, parent )
      self.config(borderwidth=2, relief=RAISED,background=COLORS.fr_discus)
      self.grid(row=2,column=0,columnspan=6)

      self.discus_name = Label(self, text="DISCUS SECTION")
      self.b_session   = Button(self, text="Session", command=self.discus_session,
                         activeforeground="#F00",fg="#00F")
      self.b_strumenu  = Menubutton(self, text="Structure", relief=RAISED,
                             activeforeground="#F00",fg="#00F")
      self.b_macro = Button(self, text="Macro", command=self.macro,
                            activeforeground="#F00",fg="#00F")
      self.b_help  = Button(self, text="Help", command=self.discus_help,
                            activeforeground="#F00",fg="#00F")
      self.b_exit  = Button(self, text="Exit", command=self.destroy,
                     activeforeground="#F00",fg="#00F")
#
      self.b_strumenu.menu=Menu(self.b_strumenu, tearoff=0 )
      self.b_strumenu['menu'] = self.b_strumenu.menu
      self.b_strumenu.menu.add_command( label="Read cell", command=self.read_cell,
                               activeforeground="#F00",foreground="#00F")
      self.b_strumenu.menu.add_command(label="Read stru", command=self.donothing)
      self.b_strumenu.menu.add_command(label="Read free", command=self.donothing)
      self.b_strumenu.menu.add_command(label="Save ", command=self.donothing)
      self.b_strumenu.menu.add_command(label="Plot ", command=self.donothing)
      self.b_strumenu.menu.add_command(label="Import", command=self.donothing)
      self.b_strumenu.menu.add_command(label="Export", command=self.donothing)
#
#  Place all elements
#
      self.discus_name.grid(row=0, column=0, columnspan=5,sticky=N)
      self.b_session.grid(row=1, column=0, sticky=W)
      self.b_strumenu.grid(row=1, column=1, sticky=W)
      self.b_macro.grid(row=1, column=2, sticky=W)
      self.b_help.grid(row=1, column=3, sticky=W)
      self.b_exit.grid(row=1, column=4,sticky=W)

   def macro(self):
      self.macros = macro_gui(self,'discus')
   def donothing(self):
      nthg = DO_NOTHING()

   def discus_session(self):
      self.b_strumenu.config(state="disabled")
      self.b_strumenu.update()
      self.b_macro.config(state="disabled")
      self.b_macro.update()
      self.b_help.config(state="disabled")
      self.b_help.update()
      #
      suite.interactive('discus')
      #
      self.b_strumenu.config(state="normal")
      self.b_strumenu.update()
      self.b_macro.config(state="normal")
      self.b_macro.update()
      self.b_help.config(state="normal")
      self.b_help.update()

   def discus_help(self):
      self.b_session.config(state="disabled")
      self.b_session.update()
      self.b_strumenu.config(state="disabled")
      self.b_strumenu.update()
      self.b_macro.config(state="disabled")
      self.b_macro.update()
      #
      suite.execute_help('discus')
      #
      self.b_session.config(state="normal")
      self.b_session.update()
      self.b_strumenu.config(state="normal")
      self.b_strumenu.update()
      self.b_macro.config(state="normal")
      self.b_macro.update()

   def read_cell(self):
      self.read_cells = READ_CELL_FR(self)
