import Calculations as calc
from tkinter import *
import utilities as u

def start_calc():
    u.results = []
    res = u.start_calc()
    up_price.config(state=NORMAL)
    down_price.config(state=NORMAL)
    result.delete(1.0,END)
    result.insert(1.0, res)

def next_step_up():
    string, res = u.next_step()
    if res:
        up_price.config(state= DISABLED)
        down_price.config(state= DISABLED)
    result.delete(1.0, END)
    result.insert(1.0, string)

def next_step_down():
    string, res = u.next_step(False)
    if res:
        up_price.config(state=DISABLED)
        down_price.config(state=DISABLED)
    result.delete(1.0, END)
    result.insert(1.0, string)

def step_back_func():
    string = u.step_back()
    if string == '':
        return
    up_price.config(state=NORMAL)
    down_price.config(state=NORMAL)
    result.delete(1.0, END)
    result.insert(1.0, string)

root = Tk('Options')

input_frame = LabelFrame(root, height = 300, width = 300)
input_frame.pack(side = 'left', fill = 'both')
labels = LabelFrame(input_frame)
labels.pack(side = 'left')
entries = LabelFrame(input_frame)
entries.pack(side = 'left')
res_frame = LabelFrame(root, height = 300, width = 300)
res_frame.pack(side = 'right', fill = 'both')
result = Text(res_frame)
result.pack(fill='both')
up_price = Button(res_frame, text='Цена на акцию поднялась', command=next_step_up)
up_price.pack()
down_price = Button(res_frame, text='Цена на акцию опустилась', command=next_step_down)
down_price.pack()
step_back = Button(res_frame, text='Сделать шаг назад', command=step_back_func)
step_back.pack()

for x in u.inputs_labels:
    l = Label(labels, text = x)
    l.pack()
    u.inputs_vars[x] = StringVar()
    e = Entry(entries, textvariable = u.inputs_vars[x])
    e.pack()

start_button = Button(input_frame, text = 'Начать решение', command=start_calc)
start_button.pack(side = 'right')

root.mainloop()


