"""
   Support classes for DISCUS_SUITE GUI
   COLORS        : color_definitions
   command_gui   : Frame to enter a single command
   control_label : Branch control to an interactive session
   DO_NOTHING    : do-nothing button
   CreateToolTip : short help while hovering 
"""
#from tkinter import *
import tkinter as tk
from tkinter import ttk
from loop_defs import *
from lib_discus_suite import *
#
#  Useful constants
# 
class CONSTANTS:
   pi = 3.141592653589
   kev_lambda = 12.398420210
   planck = 6.62607004
   mass_e = 9.10938356
   mass_n = 1.67492747
   light  = 2.99792458
   charge = 1.60217656
#
#   COLOR DEFINITIONS
#
class COLORS:
   ok_front ="#0000FF"  # Blue
   ok_active="#FF0000"  # Red
   bg_active="#FAFAFA"  # light grey
   fr_back  ="#FFFFAA"  # light yellow
   fr_diffev="#CCFFFF"  # light blue
   fr_discus="#DDFFFF"  # light blue
   fr_kuplot="#EEFFFF"  # light blue
   fr_read  ="#FFFFEE"  # white'ish blue
#
#  Themes
#
def RBN_STYLES(parent):
   parent.style.configure("TButton",          foreground=  "#0000FF",
                                              background=  "#E0E0E0")
   parent.style.map("TButton",     foreground=[('active',  "#FF0000"), 
                                               ('disabled',"#909090")],
                                   background=[('active',  "#FAFAFA"), 
                                               ('disabled',"#D0D0D0")])
   parent.style.configure("Basic.TButton",    foreground=  "#0000AA",
                                              background=  "#E0E0E0")
#                         font=('bold'))
#
   parent.style.configure("TMenubutton",      foreground= "#0000FF",
                                              background= "#E0E0E0")
   parent.style.map("TMenubutton", foreground=[('active'," #FF0000"), 
                                               ('disabled',"#909090")],
                                   background=[('active',  "#FAFAFA"),
                                               ('disabled',"#D0D0D0")])
#
   parent.style.configure("TLabel",           foreground="#000000",
                                              background="#E0E0E0")
#  parent.style.map("TLabel",      foreground=[('active',"#00FF00")],
#                                  background=[('active',"#FAFAFA")])
   parent.style.configure("Control.TLabel",   foreground="#FF0000",
                                              background="#FAFAFA")
   parent.style.map("Control.TButton", foreground=[('active',"#00GG00")])
#
#  parent.style.configure("TFrame",           background="#C0FFFF")
#  parent.style.configure("Discus.TFrame",    background="#DDFFFF")
#  parent.style.configure("Discus.TFrame",    borderwidth=2, relief=tk.RAISED)
#  parent.style.configure("Read.Discus.TFrame",    background="#FFFFEE")
#  parent.style.configure("Read.Discus.TFrame",    borderwidth=2, relief=tk.RAISED)
#  parent.style.configure("Kuplot.TFrame",    background="#EEFFFF")
#  parent.style.configure("Kuplot.TFrame",    borderwidth=2, relief=tk.RAISED)
   parent.style.configure("TNotebook",        foreground=  "#0000FF",
                                              background=  "#E0E0E0")
   parent.style.map("TNotebook",   foreground=[('active',  "#FF0000"), 
                                               ('disabled',"#909090")],
                                   background=[('active',  "#FAFAFA"), 
                                               ('disabled',"#D0D0D0")])
   parent.style.configure("TNotebook.Tab",    foreground=  "#0000FF",
                                              background=  "#C0C0C0")
   parent.style.map("TNotebook.Tab",foreground=[('active',  "#FF0000"), 
                                                ('disabled',"#909090")],
                                    background=[('active',  "#FAFAFA"), 
                                                ('disabled',"#A0A0A0"), 
                                                ('selected',"#F0F0F0")])
def is_empty(any_structure):
   if any_structure:
      return False
   else:
      return True
#
#   COMMAND CLASS
#
class command_gui(tk.Frame):
   def __init__(self, parent, prog):
      tk.Frame.__init__ ( self, parent )
      if prog == 'suite':
         self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_back)
         self.grid(row=1,column=0,columnspan=6)
      elif prog == 'discus':
         self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_read)
         self.grid(row=2,column=0,columnspan=6)
      elif prog == 'kuplot':
         self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_read)
         self.grid(row=3,column=0,columnspan=6)

      self.section_name = prog
      self.label = ttk.Label(self, text="Enter "+prog+" command")
      self.cmd = tk.Entry(self, bg="#FFF")
      self.cmd.bind('<KeyRelease-Return>',self.send_cmd_return)
      self.acc = ttk.Button(self, text="Run", command=self.send_cmd)
#                     activeforeground="#F00",foreground="#00F")
      self.exit = ttk.Button(self, text="Exit", command=self.destroy)
#                     activeforeground="#F00",foreground="#00F")


      self.label.grid(row=0,column=0)
      self.cmd.grid(row=1,column=0,columnspan=3)
      self.acc.grid(row=2,column=1)
      self.exit.grid(row=2,column=2)

   def send_cmd(self):
          line = self.cmd.get()
          length = len(line)
          if LOOPS.lblock_read:
             suite.gui_do_insert(self.section_name,line)
          else:
             suite.execute_command(self.section_name,line)
          self.cmd.delete(0,last=length)

   def send_cmd_return(self,event):
          line = self.cmd.get()
          length = len(line)
          if LOOPS.lblock_read:
             suite.gui_do_insert(self.section_name,line)
          else:
             suite.execute_command(self.section_name,line)
          self.cmd.delete(0,last=length)

def create_command_button(parent, prog, pos_row, pos_col):
   parent.b_command   = ttk.Button(parent, text="Commands", 
                      command=lambda: command_gui(parent,prog)) 
#                     activeforeground=COLORS.ok_active,
#                     foreground=COLORS.ok_front)
   parent.b_command.grid(row=pos_row,column=pos_col)
   parent.b_command_tt = CreateToolTip(parent.b_command, \
   "Open a window to type individual commands")
#
#   CONTOL CLASS
#
def control_label(parent,task,prog,row_number):
      #
      if task == "interactive" :
         infotext="Control in interactive window; type exit to return to GUI"
      elif task == "help" :
         infotext="Control in interactive window; hit ENTER key to return to GUI"
      parent.l_control=ttk.Label(parent,
            text=infotext,
            style="Control.TLabel")
      parent.l_control.grid(row=row_number,column=0, columnspan=6, sticky=tk.W)
      parent.update()
      #
      if task == "interactive" :
         suite.interactive(prog)
      elif task == "help" :
         suite.execute_help(prog)
      #
      parent.l_control.destroy()
      parent.update()
#
#    CLASS donothing
#
class DO_NOTHING(tk.Frame):
   def __init__(self):
      tk.Frame.__init__(self,None)
      self.grid()
      self.button = ttk.Button(self, text= "Do nothing botton; click to close",
                    command=self.destroy)
      self.button.grid(row=0,column=0)
#
#    def grey_out
#
def turn_off(*pargs):
    for widget in pargs:
       widget.config(state="disabled")
       widget.update()
def turn_on(*pargs):
    for widget in pargs:
       widget.config(state="normal")
       widget.update()

###def create_exit_button(parent, pos_row, pos_col):
###   parent.b_exit = ttk.Button(parent, text="Exit", 
###                   command=lambda: parent.destroy())
####                     activeforeground=COLORS.ok_active,
####                     foreground=COLORS.ok_front)
###   parent.b_exit.grid(row=pos_row,column=pos_col)
#
#    CLASS tooltip
#
""" tk_ToolTip_class101.py
gives a Tkinter widget a tooltip as the mouse is above the widget
tested with Python27 and Python34  by  vegaseat  09sep2014
www.daniweb.com/programming/software-development/code/484591/a-tooltip-class-for-tkinter

Modified to include a delay time by Victor Zaccardo, 25mar16
"""

#try:
#    # for Python2
#    import Tkinter as tk
#except ImportError:
#    # for Python3
#    import tkinter as tk

class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 300     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 55
        y += self.widget.winfo_rooty() + 40
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background="#ffffAA", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()

# testing ...
#if __name__ == '__main__':
#    root = Tk()
#    btn1 = Button(root, text="button 1")
#    btn1.pack(padx=10, pady=5)
#    button1_ttp = CreateToolTip(btn1, \
#   'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, '
#   'consectetur, adipisci velit. Neque porro quisquam est qui dolorem ipsum '
#   'quia dolor sit amet, consectetur, adipisci velit. Neque porro quisquam '
#   'est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit.')
#
#    btn2 = Button(root, text="button 2")
#    btn2.pack(padx=10, pady=5)
#    button2_ttp = CreateToolTip(btn2, \
#    "First thing's first, I'm the realest. Drop this and let the whole world "
#    "feel it. And I'm still in the Murda Bizness. I could hold you down, like "
#    "I'm givin' lessons in  physics. You should want a bad Vic like this.")
#    root.mainloop()
#
