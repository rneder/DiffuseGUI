from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from support import *
from macro_section import *
from lib_discus_suite import *

class KUPLOT_LOAD_FR(Frame):
   def __init__ (self, parent):
      Frame.__init__ ( self, parent )
      self.config(borderwidth=2, relief=RAISED,background=COLORS.fr_read)
      self.grid(row=3,column=0,columnspan=6)

      self.filename = StringVar()
      self.caption=Label(self, text="Load a data set")
      self.fileb = Button(self, text="File",command=self.file_open,
                   activeforeground=COLORS.ok_active,foreground=COLORS.ok_front)
      self.isfiletype = StringVar()
      self.l_type=Label(self,text="Filetype: ", relief=RAISED)
      self.ftype = ttk.Combobox(self, textvariable=self.isfiletype,
                   state='readonly')
      self.ftype['values'] = ('xy','ni')
      self.ftype.current(0)
      self.label_fle = Label(self, textvariable=self.filename, relief=RAISED)
      self.acc = Button(self, text="Run", command=self.load_file,
                    activeforeground="#F00",foreground="#00F")
      self.cancel = Button(self, text="Exit", command=self.destroy,
                    activeforeground="#F00",foreground="#00F")

      self.caption.grid(row=0,column=0,columnspan=5)
      self.fileb.grid(row=1,column=0)
      self.label_fle.grid(row=1,column=1,columnspan=3)
      self.l_type.grid(row=2,column=0)
      self.ftype.grid(row=2,column=1)
      self.acc.grid(row=3,column=2)
      self.cancel.grid(row=3,column=3)

   def file_open(self):
      self.filename.set(filedialog.askopenfilename())

   def load_file(self):
      if self.ftype.get() == "xy":
         line = "xy," + str(self.filename.get())
      elif self.ftype.get() == "ni":
         line = "ni," + str(self.filename.get())
      suite.kuplot_load(line)

class kuplot_gui(Frame):
   def __init__(self, parent):
      Frame.__init__ ( self, parent )
      self.config(borderwidth=2, relief=RAISED,background=COLORS.fr_kuplot)
      self.grid(row=3,column=0,columnspan=6)

      self.kuplot_name = Label(self, text="KUPLOT SECTION")
      self.b_session   = Button(self, text="Session", command=self.kuplot_session,
                         activeforeground="#F00",fg="#00F")
      self.b_filemenu  = Menubutton(self, text="File", relief=RAISED,
                             activeforeground="#F00",fg="#00F")
      self.b_reset = Button(self, text="Reset", command=self.kuplot_reset,
                            activeforeground="#F00",fg="#00F")
      self.b_plot  = Button(self, text="Plot", command=self.kuplot_plot,
                            activeforeground="#F00",fg="#00F")
      self.b_command   = Button(self, text="Commands", command=self.command,
                         activeforeground=COLORS.ok_active,
                         foreground=COLORS.ok_front)
      self.b_macro = Button(self, text="Macro", command=self.macro,
                            activeforeground="#F00",fg="#00F")
      self.b_help  = Button(self, text="Help", command=self.kuplot_help,
                            activeforeground="#F00",fg="#00F")
      self.b_exit  = Button(self, text="Exit", command=self.destroy,
                     activeforeground="#F00",fg="#00F")
#
      self.b_filemenu.menu=Menu(self.b_filemenu, tearoff=0 )
      self.b_filemenu['menu'] = self.b_filemenu.menu
      self.b_filemenu.menu.add_command( label="Load", command=self.load_file,
                               activeforeground="#F00",foreground="#00F")
#
#  Place all elements
#
      self.kuplot_name.grid(row=0, column=0, columnspan=5,sticky=N)
      self.b_session.grid(row=1, column=0, sticky=W)
      self.b_filemenu.grid(row=1, column=1, sticky=W)
      self.b_command.grid(row=1, column=2, sticky=W)
      self.b_macro.grid(row=1, column=3, sticky=W)
      self.b_help.grid(row=1, column=4, sticky=W)
      self.b_reset.grid(row=2, column=0, sticky=W)
      self.b_plot.grid(row=2, column=1, sticky=W)
      self.b_exit.grid(row=2, column=4,sticky=W)

   def command(self):
      self.cmds = command_gui(self,'kuplot')

   def macro(self):
      self.macros = macro_gui(self,'kuplot')

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

   def load_file(self):
      self.load_files = KUPLOT_LOAD_FR(self)

   def kuplot_reset(self):
      line="reset"
      prog="kuplot"
      suite.execute_command(prog,line)

   def kuplot_plot(self):
      line="plot"
      prog="kuplot"
      suite.execute_command(prog,line)

   def kuplot_plot(self):
      line="plot"
      prog="kuplot"
      suite.execute_command(prog,line)
