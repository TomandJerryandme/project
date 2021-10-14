# !/usr/bin
# python GUI 编程

# https://www.runoob.com/python/python-gui-tkinter.html     菜鸟教程
# https://www.cnblogs.com/Kobe10/p/5773821.html     博客
import tkinter as tk
import os
from tkinter import messagebox

wiondow = tk.Tk()
text_input = tk.Text(wiondow, height=10, width=100)
text_input.insert(tk.END, 'This is Text')
wiondow.title("title")
text_input.pack()
# wiondow.wm_attributes("-alpha", 1.0)
# wiondow.wm_attributes("-topmost", True)
wiondow.mainloop()