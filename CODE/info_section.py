import tkinter as tk
from tkinter import ttk
from support import *

class InfoGUI(tk.Frame):

   def __init__(self,parent,pos_row, pos_col,span_row,span_col):
      tk.Frame.__init__ ( self, parent)
      self.config(borderwidth=2, relief=tk.RAISED,background='#DDDD00')
      self.grid(row=pos_row,column=pos_col,rowspan=span_row,columnspan=span_col)
      self.info_name = ttk.Label(self, text='Info Section')
      self.info_text = tk.Text()

      self.info_name.grid(row=0,column=0,sticky=tk.N)

   def insert(self,line):
      self.info.text.insert(END,line+'\n')

