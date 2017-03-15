import tkinter as tk
from tkinter import filedialog
from support import COLORS

def file_open(parent, typestring, typeext ):
#   typestring = 'DISCUS files'
#   type_ext   = '*.cell  *.stru'
    parent.filename.set(filedialog.askopenfilename(initialdir = '.', 
                        filetypes=((typestring  ,typeext ),('all files', '*.*')))
                       )
    if len(parent.filename.get()) == 0:
        parent.filename.set('Filename undefined')
    if parent.filename.get() != 'Filename undefined' :
        parent.label_fle.configure(foreground=COLORS.nor_fore)
        parent.acc.configure(state='normal')

def file_new(parent, typestring, typeext ):
    parent.filename.set(filedialog.asksaveasfilename(initialdir = '.',
                        filetypes=((typestring  ,typeext ),('all files', '*.*')))
                       )
    if len(parent.filename.get()) == 0:
        parent.filename.set('Filename undefined')
    if parent.filename.get() != 'Filename undefined' :
        parent.label_fle.configure(foreground=COLORS.nor_fore)
        parent.acc.configure(state='normal')
