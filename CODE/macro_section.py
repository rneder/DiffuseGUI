from tkinter import *
from tkinter import filedialog
from support import *
from lib_discus_suite import *

class macro_gui(Frame):
   def __init__(self, parent, prog):
      Frame.__init__ ( self, parent )
      if prog == 'suite':
         self.config(borderwidth=2, relief=RAISED,background=COLORS.fr_back)
         self.grid(row=1,column=0,columnspan=6)
      elif prog == 'discus':
         self.config(borderwidth=2, relief=RAISED,background=COLORS.fr_read)
         self.grid(row=2,column=0,columnspan=6)
      elif prog == 'kuplot':
         self.config(borderwidth=2, relief=RAISED,background=COLORS.fr_read)
         self.grid(row=3,column=0,columnspan=6)

      self.macrofilename = StringVar()
      self.macrofilename.set("Undefined")
      self.section_name = prog
      self.num_par = IntVar()
      self.num_par.set(0)
      self.num_par_old = IntVar()
      self.num_par_old.set(0)

      self.l_titl = Label(self, text="Macro Menu")
      self.b_open = Button(self, text="Open", command=self.file_open,
                    activeforeground=COLORS.ok_active,
                    foreground=COLORS.ok_front)
      self.l_file = Label(self, textvariable=self.macrofilename, relief=RAISED)
      self.run    = Button(self, text="Run",  command=self.macro_run,
                    activeforeground=COLORS.ok_active,
                    foreground=COLORS.ok_front)
      self.cancel = Button(self, text="Exit", command=self.destroy,
                    activeforeground=COLORS.ok_active,
                    foreground=COLORS.ok_front)

      self.l_titl.grid(row=0,column=0,columnspan=3, sticky=N)
      self.b_open.grid(row=1,column=0, sticky=W)
      self.l_file.grid(row=2,column=0,columnspan=3, sticky=W)
      self.run.grid(row=4,column=1, sticky=E)
      self.cancel.grid(row=4,column=2, sticky=E)

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

   def macro_run(self):
      line ="@" + str(self.macrofilename.get()) + " "
      if self.num_par.get() == 1 :
         line = line + str(self.entry_widgets[0].get())
      elif self.num_par.get() > 1 :
         for x in range(self.num_par.get()-1) :
            line = line + str(self.entry_widgets[x].get()) + ","
         line = line + str(self.entry_widgets[self.num_par.get()-1].get())
      suite.execute_macro(self.section_name, line)
      
   def create_entry_widget(self, x):
      new_widget = Entry(self) 
      new_widget.grid(row=5+x,column=1,columnspan=2)
      new_widget.insert(0,x+1)
      return new_widget
      
   def create_label_widget(self, x):
      new_label  = Label(self, text="Parameter " + str(x+1) + ":") 
      new_label.grid(row=5+x,column=0,)
      return new_label
