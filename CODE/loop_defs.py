import tkinter as tk
from tkinter import ttk
from lib_discus_suite import *
#
#   COLOR DEFINITIONS
#
class LOOP_DEFS:
   def __init__(self):
      self.lblock_read = False
      self.level       = 0

   def set_lblock_read(self,state):
      self.lblock_read  = state

   def set_level(self,new):
      self.level  = new

   def do_send_command(self, prog, line):
      if self.lblock_read:
         suite.gui_do_insert(prog, line)

LOOPS = LOOP_DEFS()

