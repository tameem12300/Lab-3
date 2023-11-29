import tkinter as tk
from PIL import Image, ImageTk
import random

def close():
    window.destroy()

symb_dict={
    -17:"A",
    -16:"B",
    -15:"C",
    -14:"D",
    -13:"E",
    -12:"F",
    -11:"G",
    -10:"H",
    -9:"I",
    -8:"J",
    -7:"K",
    -6:"L",
    -5:"M",
    -4:"N",
    -3:"P",
    -2:"Q",
    -1:"R",
    0:"S",
    1:"T",
    2:"U",
    3:"V",
    4:"W",
    5:"X",
    6:"Y",
    7:"Z",
    8:"0",
    9:"1",
    10:"2",
    11:"3",
    12:"4",
    13:"5",
    14:"6",
    15:"7",
    16:"8",
    17:"9",
    18:"O"

}

def block_gen():
    
    a = random.randint(-17,18)
    b = random.randint(-17,18)
    c = random.randint(-17,18)
    d = random.randint(-17,18)
    sum = a+b+d+c    

    if sum<18 and sum>-17:
        return symb_dict.get(a) + symb_dict.get(b) + symb_dict.get(c) + symb_dict.get(d)
    else: return block_gen()

def key_gen():
    return block_gen() + "-" + block_gen() + "-" + block_gen() 

print(key_gen())
window = tk.Tk() 

def update_label():
   lbl_result.config(text=key_gen())
       
window.geometry('800x600')
bg_img = ImageTk.PhotoImage(file='FIFA.jpg')

lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window)
frame.place(relx=0.3, rely=0.3, anchor='n')

lbl_roots = tk.Label(frame, text='Result:')
lbl_roots.grid(column=1, row=2)
lbl_result = tk.Label(frame, text=key_gen(), font=('Arial', 10))
lbl_result.grid(column=2, row=2)

btn_exit = tk.Button(frame, text='enter', command=close)
btn_exit.grid(column=2, row=4, padx=10, pady=15)

btn_new = tk.Button(frame,text="new", command=update_label)
btn_new.grid(column=1, row=4, padx=10, pady=15)


window.mainloop()





