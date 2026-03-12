'''from tkinter import *
from tkinter import messagebox
def click():
    messagebox.showinfo("Ok")
win=Tk()
win.geometry('300x300')
win.title("CHeckbox")
'''
'''w=Label(win, text= 'Select', fg='Red', font='100')
w.pack()'''
'''B1=IntVar()
B2=IntVar()
B3=IntVar()
cb1=Checkbutton(win,text ='1',variable= B1, onvalue=1, offvalue=0, height=2, width=10)
cb2=Checkbutton(win,text ='2',variable= B2, onvalue=1, offvalue=0, height=2, width=10)
cb3=Checkbutton(win,text ='3',variable= B3, onvalue=1, offvalue=0, height=2, width=10)
cb1.pack()
cb2.pack()
cb3.pack()
win.mainloop()''''''
username=Label(win,text="User Name").place(x=30,y=50)
pw=Label(win,text="Password").place(x=30,y=90)
b=Button(win,text="Submit", activebackground='red', activeforeground='blue',command=click).place(x=30,y=120)
e1=Entry(win,width=20).place(x=100,y=50)
e2=Entry(win,width=20).place(x=100,y=90)
win.mainloop()

'''
import functools
def sum(x,y):
    return(x+y)
try:
    n=list(map(lambda x: int(x)**2, input().split(' ')))
    print('Squared numbers:',n)
    print('Sum of squares:', functools.reduce(sum, n))
except:
    print("ERROR, HOW COULD YOU?!")
