import tkinter as tk
from tkinter import filedialog

def file_open(parent):
    parent.filename.set(filedialog.askopenfilename())
    if parent.filename.get() != 'Filename undefined' :
        parent.label_fle.configure(foreground='#000000')
        parent.acc.configure(state='normal')

def file_new(parent):
    parent.filename.set(filedialog.asksaveasfilename())
    if parent.filename.get() != 'Filename undefined' :
        parent.label_fle.configure(foreground='#000000')
        parent.acc.configure(state='normal')
