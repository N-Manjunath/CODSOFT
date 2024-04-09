import tkinter
from tkinter import *
import random
root=tkinter.Tk()
root.geometry('350x350')
tasks=[]
def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert('end',task)
def clear_listbox():
    lb_tasks.delete(0,  'end')
def add_task():
    task=txt_input.get()
    if task!='':
        tasks.append(task)
        update_listbox()
    else:
        lbl_display['text']=' please enter any task'
def del_task():
    global tasks
    tasks=[]
    update_listbox()
def del_one_task():
    task=lb_tasks.get('active')
    if task in tasks:
        tasks.remove(task)
    update_listbox()
def choose_random():
    task=random.choice(tasks)
    msg1='random task is : %s'%task
    lbl_display['text']=msg1
def no_of_tasks():
    tasks_count=len(tasks)
    msg2='number of taks : %s'%tasks_count
    lbl_display['text']=msg2
def ascend():
        tasks.sort()
        update_listbox ()
def descend():
    tasks.sort()
    tasks.reverse()
    update_listbox()

lbl_title=tkinter.Label(root,text='To-Do-List',font='arial 20 bold')
lbl_title.grid(row=0,column=0)
lbl_display=tkinter.Label(root,text='')
lbl_display.grid(row=1,column=0)
lbl_display=tkinter.Label(root,text='Display Bar',bg='white')
lbl_display.grid(row=0,column=1)
txt_input=tkinter.Entry(root,width=15)
txt_input.grid(row=1,column=1)
btn_add=tkinter.Button(root,text="Add task",fg='green',bg='white',command=add_task)
btn_add.grid(row=2,column=0)
btn_del=tkinter.Button(root,text="Delete all",fg='red',bg='white',command=del_task)
btn_del.grid(row=3,column=0)
btn_del_one=tkinter.Button(root,text='Delete one',fg='red',bg='white',command=del_one_task)
btn_del_one.grid(row=4,column=0)
btn_random_choose=tkinter.Button(root,text='choose_random',fg='orange',bg='white',command=choose_random)
btn_random_choose.grid(row=5,column=0)
btn_no_of_tasks=tkinter.Button(root,text='tasks count',fg='orange',bg='white',command=no_of_tasks)
btn_no_of_tasks.grid(row=6,column=0)
btn_Ascend=tkinter.Button(root,text='Ascend order',fg='blue',bg='white',command=ascend)
btn_Ascend.grid(row=7,column=0)
btn_Descend=tkinter.Button(root,text='Descend order',fg='blue',bg='white',command=descend)
btn_Descend.grid(row=8,column=0)
btn_exit=tkinter.Button(root,text='exit',fg='red',bg='white',command=exit)
btn_exit.grid(row=9,column=0)
lb_tasks=tkinter.Listbox(root)
lb_tasks.grid(row=1,column=1,rowspan=8)
root.mainloop()