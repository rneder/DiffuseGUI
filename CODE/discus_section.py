import tkinter as tk
from tkinter import ttk
from support import COLORS, control_label, is_empty, turn_off, turn_on, CreateToolTip
from exit_button import create_exit_button
from macro_section import create_macro_menu
from command_lang import create_command_language
from discus_read import READ_CELL_FR, READ_STRU_FR
from discus_output import DISCUS_OUTPUT_FR
from discus_fourier import SINGLE_FOUR_FR
from discus_powder import DISCUS_POWDER_FR
from suite_status import suite_status
#
class discus_gui(tk.Frame):
    def __init__(self, parent, user):
       tk.Frame.__init__ ( self, parent)
       self.config(borderwidth=2, relief=tk.RAISED,background=COLORS.fr_discus)
#       self.configure(style= 'Discus.TFrame')
       self.grid(row=2,column=0,columnspan=7,sticky='EW')

       self.discus_name = ttk.Label(self, text='DISCUS SECTION')
#
       self.b_strumenu  = ttk.Menubutton(self, text='Build a basic\nStructure',
                          style='Basic.TButton')
       self.b_fourmenu  = ttk.Menubutton(self, text='Calculate PDF / \nFourier / Powder',
                          style='Basic.TButton')
       create_macro_menu(    self, 'discus',1, 4)
       create_command_language(self, 'discus', 1,6)
       self.b_help  = ttk.Button(self, text='Help', command=lambda: self.discus_help(user))
 #
       self.b_strumenu.menu=tk.Menu(self.b_strumenu, tearoff=0 )
       self.b_strumenu['menu'] = self.b_strumenu.menu
       self.b_strumenu.menu.add_command( label='Expand asymmetric unit',
                                command=lambda: READ_CELL_FR(self),
                                activeforeground='#F00',foreground='#00F')
       self.b_strumenu.menu.add_command(label='Read old structure', 
                                command=lambda: READ_STRU_FR(self),
                                activeforeground='#F00',foreground='#00F')
       self.b_strumenu.menu.add_command(label='Define empty free space', command=self.donothing)
       self.b_strumenu.menu.add_command(label='Save ', command=self.donothing)
       self.b_strumenu.menu.add_command(label='Plot ', command=self.donothing)
       self.b_strumenu.menu.add_command(label='Import', command=self.donothing)
       self.b_strumenu.menu.add_command(label='Export', command=self.donothing)
#
       self.b_strumenu.menu.entryconfig(3,state='disabled')
       self.b_strumenu.menu.entryconfig(4,state='disabled')
       self.b_strumenu.menu.entryconfig(6,state='disabled')
#
       self.b_fourmenu.menu=tk.Menu(self.b_fourmenu, tearoff=0 )
       self.b_fourmenu['menu'] = self.b_fourmenu.menu
       self.b_fourmenu.menu.add_command( label='Calculate Fourier',
                                command=lambda: SINGLE_FOUR_FR(self),
                                activeforeground='#F00',foreground='#00F')
       self.b_fourmenu.menu.add_command( label='Zone Axis Pattern',
                                command=lambda: SINGLE_FOUR_FR(self),
                                activeforeground='#F00',foreground='#00F')
       self.b_fourmenu.menu.add_separator()
       self.b_fourmenu.menu.add_command( label='Powder Pattern',
                                command=lambda: DISCUS_POWDER_FR(self),
                                activeforeground='#F00',foreground='#00F')
       self.b_fourmenu.menu.add_command( label='PDF',
                                command=lambda: SINGLE_FOUR_FR(self),
                                activeforeground='#F00',foreground='#00F')
       self.b_fourmenu.menu.add_separator()
       self.b_fourmenu.menu.add_command( label='Save Pattern',
                                command=lambda: DISCUS_OUTPUT_FR(self),
                                activeforeground='#F00',foreground='#00F')
       self.b_fourmenu.menu.entryconfig(1,state='disabled')
       self.b_fourmenu.menu.entryconfig(3,state='disabled')
       self.b_fourmenu.menu.entryconfig(3,state='normal')
       self.b_fourmenu.menu.entryconfig(4,state='disabled')
       self.b_fourmenu.menu.entryconfig(6,state='disabled')
       self.b_fourmenu.menu.entryconfig(6,state='normal')
#      self.b_fourmenu.configure(state='disabled')

#
#  Place all elements
#
       self.discus_name.grid(row=0, column=1, columnspan=5,sticky=tk.N)
       self.b_strumenu.grid(row=1, column=0, sticky=tk.W)
       self.b_fourmenu.grid(row=1, column=1, sticky=tk.W)
       self.b_help.grid(row=1, column=7, sticky='EWNS')
#
#  ToolTips
#
#      self.b_session_ttp = CreateToolTip(self.b_session,\
#      'Start an interactive DISCUS session. Type 'exit' to leave the '
#      'interactive session and to return to the GUI')
       self.b_strumenu_ttp = CreateToolTip(self.b_strumenu,\
       'The basic and typically the first step within DISCUS. ' 
       'Read a structure from a file, build a unit cell by expanding '
       'the content of an asymmetric unit, import external formats. '
       'Includes the menu to save a structure')
       self.b_fourmenu_ttp = CreateToolTip(self.b_fourmenu,\
       'Calculate a diffraction pattern or a PairDistributionFunction. '
       ' Active, once a structure has been build')
       self.b_help_ttp = CreateToolTip(self.b_help, \
       'Enter the help menu. Within the help menu you can obtain '
       'further info by typing any of the available words followed '
       'by a <RETURN> or <ENTER>.' 
       'Return to the GUI with an empty line and <RETURN> or <ENTER> ')
       #
       # Set proper status
       #
#      suite_status.change(1)
       self.b_strumenu.bind('<ButtonRelease-1>', lambda eff: suite_status.change(eff, -1))
       self.b_fourmenu.bind('<ButtonRelease-1>', lambda eff: suite_status.change(eff, -1))
       self.b_macro.bind('<ButtonRelease-1>', lambda eff: suite_status.change(eff, -1))
       self.b_cmd.bind('<ButtonRelease-1>', lambda eff: suite_status.change(eff, -1))
       self.b_help.bind('<ButtonRelease-1>', lambda eff: suite_status.change(eff, -1))
 
    def donothing(self):
        nthg = DO_NOTHING()


    def discus_help(self, user):
        # Remember old states 
        fourmenu_state = self.b_fourmenu.state()
        # Temporarily turn off
        turn_off(self.b_strumenu, self.b_fourmenu, self.b_cmd, self.b_macro)
        control_label(self, 'help', 'discus', 2)
        # Activate for current user type
        if user.get() == 0: 
            turn_on(self.b_strumenu, self.b_macro)
        else:
            turn_on(self.b_strumenu, self.b_cmd, self.b_macro)
        # For all users return menus to previous state if active
        if is_empty(fourmenu_state):
            turn_on(self.b_fourmenu)
  
