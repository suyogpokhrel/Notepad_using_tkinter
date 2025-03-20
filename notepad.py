import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser,filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Notepad Editor')


#################### main menu ########################
main_menu = tk.Menu()

# file
file = tk.Menu(main_menu, tearoff=False)



edit = tk.Menu(main_menu, tearoff=False)
view = tk.Menu(main_menu, tearoff=False)
color_theme = tk.Menu(main_menu, tearoff=False)

# cascading
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)

# ----------------&&&& End main menu &&&&&--------------------


#################### Toolbar ########################
# ----------------&&&& End Toolbar &&&&&--------------------


#################### text editor ########################
# ----------------&&&& End text editor &&&&&--------------------


#################### main status bar ########################
# ----------------&&&& End main status bar &&&&&--------------------


#################### main menu functionality ########################
# ----------------&&&& End main menu functionality &&&&&--------------------

main_application.config(menu=main_menu)
main_application.mainloop()

