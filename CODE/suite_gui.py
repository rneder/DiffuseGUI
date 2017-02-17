import tkinter as tk
from tkinter import ttk
from support import *
from   info_section import *
from discus_section import discus_gui
from kuplot_section import kuplot_gui
from diffev_section import diffev_gui
from exit_button import create_exit_button
from macro_section import create_macro_menu
from command_lang import create_command_language
from suite_status import suite_status

def deactivate(parent):
    parent.b_macro.menu.entryconfig(1, state='disabled')
    parent.b_cmd.config(state='disabled')

def activate(parent):
    parent.b_macro.menu.entryconfig(1, state='normal')
    parent.b_cmd.config(state='normal')

def deactivate_all(parent):
    deactivate(parent.menu_baar)
    deactivate(parent.note_buch.gui_discus)
    deactivate(parent.note_buch.gui_discus)
    deactivate(parent.note_buch.gui_kuplot)
    deactivate(parent.note_buch.gui_diffev)

def activate_all(parent):
    activate(parent.menu_baar)
    activate(parent.note_buch.gui_discus)
    activate(parent.note_buch.gui_kuplot)
    activate(parent.note_buch.gui_diffev)

class MENU_BAR(tk.Frame):
    def __init__(self,master, user):
        tk.Frame.__init__(self,None, background='#FFFFFF')
        self.config(borderwidth=2, relief=tk.RAISED)
        self.grid()
        self.__create_bar(master, user)
    def donothing(self):
        nthg = DO_NOTHING()

    def discus_sub(self):
        LOOPS.do_send_command('suite', 'discus')
        self.discus = discus_gui(self)

    def kuplot_sub(self):
        LOOPS.do_send_command('suite', 'kuplot')
        self.kuplot = kuplot_gui(self)

    def diffev_sub(self):
        LOOPS.do_send_command('suite', 'diffev')
        self.diffev = diffev_gui(self)

    def suite_help(self, user):
        turn_off(self.b_macro, self.b_cmd, self.b_exit)
        control_label(self,'help','suite',1)
        # Activate for current user type
        if user.get() == 0:
           turn_on(self.b_macro, self.b_exit)
        else:
           turn_on(self.b_macro, self.b_cmd, self.b_exit)

    def __create_bar(self,master, user):
        create_command_language(self, 'suite', 0,5)
        create_macro_menu(    self, 'suite',0, 3)
        self.b_help      = ttk.Button(self, text='Help', 
                           command=lambda: self.suite_help(user))
        self.b_exit      = ttk.Button(self, text='Exit', command=master.quit)

        # place items
        self.b_help.grid(row=0, column=6, sticky='EWNS')
        self.b_exit.grid(row=0, column=7, sticky='EWNS')

        # Tooltips
#       self.b_session_ttp = CreateToolTip(self.b_session, \
#       'Start an interactive session. Type "exit" to leave the '
#       'interactive session and to return to the GUI') 
        self.b_help_ttp = CreateToolTip(self.b_help, \
        'Enter the help menu. Within the help menu you can obtain '
        'further info by typing any of the available words followed '
        'by a <RETURN> or <ENTER>.' 
        'Return to the GUI with an empty line and <RETURN> or <ENTER> ')
        self.b_exit_tt = CreateToolTip(self.b_exit, \
        'Terminate the DISCUS_SUITE. Make sure that you have saved '
        'any important structure, as the DISCUS_SUITE will not '
        'ask to confirm an EXIT')

        #InfoFrame
        #self.Info = INFO(self)

class NOTE_BOOK(tk.Frame):
    def __init__(self, master, user, row_pos, col_pos, row_span, col_span):
        self.master = master
        tk.Frame.__init__ ( self, None, background='#DDDDDD')
        self.config(borderwidth=4, relief=tk.RAISED)
        self.grid(row=row_pos, column=col_pos, rowspan=row_span,
                  columnspan=col_span, sticky='EW')
        self.__createWidgets(master, user)
    def __createWidgets(self, master, user):
        self.nb = ttk.Notebook(self)
        #
        # create a child frame for each page
        #
        self.discus = tk.Frame(bg=COLORS.fr_discus)
        self.kuplot = tk.Frame(bg=COLORS.fr_kuplot)
        self.diffev = tk.Frame(bg=COLORS.fr_diffev)
        #
        self.gui_discus = discus_gui(self.discus, user)
        self.gui_kuplot = kuplot_gui(self.kuplot, user)
        self.gui_diffev = diffev_gui(self.diffev, user)
        #
        # create the pages, text goes on the tabs
        #
        self.nb.add(self.discus, text='DISCUS \nStructure Builder')
        self.nb.add(self.kuplot, text='KUPLOT \nGraphics')
        self.nb.add(self.diffev, text='DIFFEV \nRefinement')
        #
        # grid everything
        #
        self.nb.grid(row=0, column=0, sticky='EW')
        #
        # tool tips
        #
        self.gui_discus_ttp = CreateToolTip(self.nb, \
        'The three tabs give access to the main tasks of the '
        'DISCUS_SUITE: \nDISCUS the structure building and modifying tool '
        '\nKUPLOT the graphics part with access to data set manipulations '
        'and R-value calculations \nDIFFEV a generic evolutionary '
        'refinement tool.')
        #
        self.nb.bind('<<NotebookTabChanged>>',lambda eff : suite_status.nbc(eff, self))
        suite_status(0)

class DISCUS_SUITE(tk.Frame):

    def __init__(self, master):
        self.master = master
        master.title('DISCUS_SUITE')
        tk.Frame.__init__ ( self, None, background='#FFFFFF' )
        self.grid()
        self.style=ttk.Style()
        RbnStyles = RBN_STYLES(self)
        self.__createWidgets(self)

    def __createWidgets (self,master ):
        self.user = tk.IntVar()
        self.user.set(0)
        self.menu_baar= MENU_BAR(master, self.user)
        self.note_buch= NOTE_BOOK(master, self.user, 2, 0, 1, 2)
        #
        self.R1 =tk.Radiobutton(self, text='Basic Mode', variable=self.user,
                                value=0,command=lambda: deactivate_all(self),
                                activeforeground='#F00', foreground='#00F')
        self.R2 =tk.Radiobutton(self, text='Advanced Mode', variable=self.user,
                                value=1,command=lambda: activate_all(self),
                                activeforeground='#FF0000',
                                foreground='#0000FF')

        self.R1.grid(row=0, column=0, stick='W', padx=(0,20))
        self.R2.grid(row=1, column=0, stick='W', padx=(0,20))
        self.menu_baar.grid(row=0, column=1)
        deactivate_all(self)
        self.R1_ttp = CreateToolTip(self.R1, \
        'In the basic mode you have access to the menu driven tasks.')
        self.R2_ttp = CreateToolTip(self.R2, \
        'In the Advanced mode you have full access to all commands, '
        'a detailed knowledge of the command language is needed')

def main():
    suite.initialize_suite()
    root = tk.Tk()
    root.minsize(width=800, height=600)
    root.configure(bg='white')
    root.lift()
    discus_suite_gui = DISCUS_SUITE(root)
    suite_status(0)
    a=suite_status(0)
    root.mainloop()
#
if __name__=='__main__': main()
