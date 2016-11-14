from tkinter import *
from support import *
from lib_discus_suite import *
from discus_section import *
from kuplot_section import *
from macro_section import *

class MENU_BAR(Frame):
   def __init__(self,master):
      Frame.__init__(self,None)
      self.grid()
      self.__create_bar(master)
   def donothing(self):
      nthg = DO_NOTHING()

   def discus_sub(self):
      self.discus = discus_gui(self)

   def kuplot_sub(self):
      self.kuplot = kuplot_gui(self)

   def macro(self):
      self.macros = macro_gui(self,'suite')

   def command(self):
      self.cmds = command_gui(self,'suite')

   def suite_session(self):
      turn_off(self.b_section, self.b_command, self.b_macro, self.b_help)
      control_label(self,"interactive","suite",1)
      turn_on(self.b_section, self.b_command, self.b_macro, self.b_help)

   def suite_help(self):
      turn_off(self.b_session, self.b_section, self.b_command, self.b_macro)
      control_label(self,"help","suite",1)
      turn_on(self.b_session, self.b_section, self.b_command, self.b_macro)

   def __create_bar(self,master):
      self.b_session   = Button(self, text="Session", command=self.suite_session,
                         activeforeground=COLORS.ok_active,
                         foreground=COLORS.ok_front)
      self.b_section   = Menubutton(self, text="Sections", relief=RAISED,
                         activeforeground=COLORS.ok_active,
                         foreground=COLORS.ok_front)
      self.b_command   = Button(self, text="Commands", command=self.command,
                         activeforeground=COLORS.ok_active,
                         foreground=COLORS.ok_front)
      self.b_macro     = Button(self, text="Macros", command=self.macro,
                         activeforeground=COLORS.ok_active,
                         foreground=COLORS.ok_front)
      #question = PhotoImage(file="question.gif")
      self.b_help      = Button(self, text="Help", 
                         command=self.suite_help,
                         activeforeground=COLORS.ok_active,
                         foreground=COLORS.ok_front)
      self.b_exit      = Button(self, text="Exit", command=master.quit,
                         activeforeground=COLORS.ok_active,
                         foreground=COLORS.ok_front)

      self.b_section.menu = Menu(self.b_section, tearoff=0)
      self.b_section['menu'] = self.b_section.menu
      self.b_section.menu.add_command(label="DISCUS", command=self.discus_sub,
                         activeforeground=COLORS.ok_active,
                         foreground=COLORS.ok_front)
      self.b_section.menu.add_command(label="KUPLOT", command=self.kuplot_sub,
                         activeforeground=COLORS.ok_active,
                         foreground=COLORS.ok_front)
      self.b_section.menu.add_command(label="DIFFEV", command=self.donothing)

      # place items
      self.b_session.grid(row=0,column=0)
      self.b_section.grid(row=0,column=1)
      self.b_command.grid(row=0,column=2)
      self.b_macro.grid(row=0,column=3)
      self.b_help.grid(row=0,column=4)
      self.b_exit.grid(row=0,column=5)

      # Tooltips
      self.b_session_ttp = CreateToolTip(self.b_session, \
      "Start an interactive session. Type 'exit' to leave the "
      "interactive session and to return to the GUI") 
      self.b_help_ttp = CreateToolTip(self.b_help, \
      "Enter the help menu. Within the help menu you can obtain "
      "further info by typing any of the available word followed "
      "by a <RETURN> or <ENTER>." 
      "Return to the GUI with a empty line and <RETURN> of <ENTER> ")

class DISCUS_SUITE(Frame):

   def __init__(self, master):
      self.master = master
      master.title("DISCUS_SUITE")
      Frame.__init__ ( self, None )
      self.grid()
      self.__createWidgets(master)

   def __createWidgets (self,master ):
      self.menu_bar = MENU_BAR(master)

      self.menu_bar.grid(row=1,column=0)

suite.initialize_suite()
root = Tk()
root.minsize(width=400,height=500)
root.lift()
discus_suite_gui = DISCUS_SUITE(root)
root.mainloop()
