import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser,filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Notepad Editor')


#################### main menu ########################
main_menu = tk.Menu()

# ----------------- file -------------------------------
# file icons
new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')

file = tk.Menu(main_menu, tearoff=False)


# -------------------- edit -----------------------------
# edit icons
copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')

edit = tk.Menu(main_menu, tearoff=False)


# --------------------- view ------------------------------
# view icons
tool_bar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons2/status_bar.png')

view = tk.Menu(main_menu, tearoff=False)


# ---------------------- color theme -----------------------
# color theme icons
light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')

color_theme = tk.Menu(main_menu, tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Default' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red ' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' : ('#ededed', '#6b9dc2'),
}


# cascading
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)

# ----------------&&&& End main menu &&&&&--------------------


#################### Toolbar ########################

tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

# font box 
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx=5)

# size box 


# ----------------&&&& End Toolbar &&&&&--------------------


#################### text editor ########################
# ----------------&&&& End text editor &&&&&--------------------


#################### main status bar ########################
# ----------------&&&& End main status bar &&&&&--------------------


#################### main menu functionality ########################

# file commands
file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N')
file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O')
file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S')
file.add_command(label='Save As', image=save_as_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S')
file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q')

# edit commands
edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+C')
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl+V')
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X')
edit.add_command(label='Clear All', image=clear_all_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+X')
edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F')

# view check button
view.add_checkbutton(label='Tool Bar', image=tool_bar_icon, compound=tk.LEFT)
view.add_checkbutton(label='Status Bar', image=status_bar_icon, compound=tk.LEFT)

# color theme
count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT)
    count+=1


# ----------------&&&& End main menu functionality &&&&&--------------------

main_application.config(menu=main_menu)
main_application.mainloop()

