from pyvirtualdisplay import Display
from turtle import *
import tkinter as tk

display = Display(visible=0, size=(800, 600))
display.start()

# Your turtle code here
right(10)
forward(100)

display.stop()