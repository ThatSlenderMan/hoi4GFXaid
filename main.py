from tkinter import *
from tkinter import ttk

import pyperclip

normal = ""
shine = ""

def make_code():
    dds = dds_entry.get()
    filepath = filepath_input.get()
    prefix = custom_prefix_entry.get()
    global normal, shine
    normal = f'''SpriteType = {{
       name = "{prefix}{dds}"
       texturefile = "{filepath}{dds}.dds"
    }}'''
    shine = f'''spriteType = {{
        name = "{prefix}{dds}_shine"
        texturefile = "{filepath}{dds}.dds"
        animation = {{
            animationmaskfile = "{filepath}{dds}.dds"
            animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
            animationrotation = -90.0
            animationlooping = no
            animationtime = 0.75
            animationdelay = 0
            animationblendmode = "add"
            animationtype = "scrolling"
            animationrotationoffset = {{ x = 0.0 y = 0.0 }}
            animationtexturescale = {{ x = 1.0 y = 1.0 }}
        }}
        animation = {{
            animationmaskfile = "{filepath}{dds}.dds"
            animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
            animationrotation = 90.0
            animationlooping = no
            animationtime = 0.75
            animationdelay = 0
            animationblendmode = "add"
            animationtype = "scrolling"
            animationrotationoffset = {{ x = 0.0 y = 0.0 }}
            animationtexturescale = {{ x = 1.0 y = 1.0 }}
        }}
        legacy_lazy_load = no
    }}'''

    goals_normal_output.delete("1.0", END)
    goals_normal_output.insert('1.0', normal)
    goals_shine_output.delete("1.0", END)
    goals_shine_output.insert('1.0', shine)



def copy_normal():
    pyperclip.copy(normal)

def copy_shine():
    pyperclip.copy(shine)

root = Tk()
root.title("Slender's HOI4 GFX aid")
root.geometry("860x785")
theme = ttk.Style()
theme.theme_use('winnative')

frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=0, row=0, sticky=(N, W, E, S), padx=5, pady=5)
frame['borderwidth'] = 2
frame['relief'] = SUNKEN


dds_label = ttk.Label(frame, text=".dds Filename:")
dds_label.grid(column=1, row=0, sticky=(N, W, E, S))

dds = StringVar()
dds_entry = ttk.Entry(frame, textvariable=dds, width=50)
dds_entry.grid(column=2, row=0, sticky=(N, W, S), padx=5, pady=5)

dds_note = ttk.Label(frame, text="Note: do NOT enter '.dds' after the filename, the program takes care of that.")
dds_note.grid(column = 3, row = 0, sticky=(W), padx=5, pady=5)

filepath_label = ttk.Label(frame, text=".dds File Path:")
filepath_label.grid(column=1, row=1, sticky=(N, W, E, S))

filepath_input = StringVar()
filepath_entry = ttk.Entry(frame, textvariable=filepath_input, width=50)
filepath_entry.grid(column=2, row=1, sticky=(N, W, S), padx=5, pady=5)
filepath_input.set("gfx/interface/goals/")

filepath_note = ttk.Label(frame, text="Optional. Only edit if you further organise focus gfx within your /goals/ file.")
filepath_note.grid(column=3, row=1, sticky=(W, E), padx=5, pady=5)

do_stuff = ttk.Button(frame, text="Gimme the code", command=make_code, width=15)
do_stuff.grid(column=2, row=3, sticky=(N, W, S), padx=5, pady=5)

custom_prefix_label = ttk.Label(frame, text="Prefix:")
custom_prefix_label.grid(column=1, row=2, sticky=(N, W, E, S))

custom_prefix = StringVar()
custom_prefix_entry = ttk.Entry(frame, textvariable=custom_prefix, width=50)
custom_prefix_entry.grid(column=2, row=2, sticky=(N, W, S), padx=5, pady=5)
custom_prefix.set("GFX_goal_")

prefix_note = ttk.Label(frame, text="Will not work unless you end with an underscore '_'")
prefix_note.grid(column=3, row=2, sticky=(W, E), padx=5, pady=5)

goals_normal_label = ttk.Label(frame, text="goals.gfx:")
goals_normal_label.grid(column=1, row=4, sticky=(N, W, S))

goals_normal_output = Text(frame, width=91, height=4, state="normal")
goals_normal_output.grid(column=2, row=4, sticky=(N, W, S), columnspan=10, padx=5, pady=5)

goals_copy_button = ttk.Button(frame, text="Copy", command=copy_normal, width = 10)
goals_copy_button.grid(column=2, row=5, sticky=(N, W, S), columnspan=10, padx=5, pady=5)

goals_shine_label = ttk.Label(frame, text="goals_shine.gfx:")
goals_shine_label.grid(column=1, row=6, sticky=(N, W, S))

goals_shine_output = Text(frame, width=91, height=29, state="normal")
goals_shine_output.grid(column=2, row=6, sticky=(N, W, S), columnspan=10, padx=5, pady=5)

shine_copy_button = ttk.Button(frame, text="Copy", command=copy_shine, width = 10)
shine_copy_button.grid(column=2, row=7, sticky=(N, W, S), columnspan=10, padx=5, pady=5)

root.mainloop()
