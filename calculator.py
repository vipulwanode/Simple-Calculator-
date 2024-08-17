from tkinter import *
def click(event):
    global scvalue
    text=event.widget.cget('text')
    print(text)
    if text=='=':
        if scvalue.get().isdigit():
            value=int(scvalue.get()) 
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update() 
    elif text=='C':
        scvalue.set('')
        screen.update() 
    else:
        scvalue.set(scvalue.get()+ text)
        screen.update() 
        
# GUI creation ...........
root=Tk()
root.geometry('644x900')
root.title(' Simple Calculator ')
root.resizable(False,False)
scvalue=StringVar()
scvalue.set('')
screen=Entry(root,textvar=scvalue,font='lucida 40 bold')
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

# button from 0 to 1 and button for operators..........

f=Frame(root,bg='black')
b=Button(f,text='7',padx=27,pady=12,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=10)
b.bind('<Button-1>',click)
b=Button(f,text='8',padx=27,pady=12,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=10)
b.bind('<Button-1>',click)
b=Button(f,text='9',padx=27,pady=12,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=10)
b.bind('<Button-1>',click)
b=Button(f,text='*',padx=27,pady=12,font='lucida 35 bold',bg='pink')
b.pack(side=LEFT,padx=18,pady=10)
b.bind('<Button-1>',click)
f.pack()


f=Frame(root,bg='black')
b=Button(f,text='4',padx=27,pady=12,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=10)
b.bind('<Button-1>',click)
b=Button(f,text='5',padx=27,pady=12,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=10)
b.bind('<Button-1>',click)
b=Button(f,text='6',padx=27,pady=12,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=10)
b.bind('<Button-1>',click)
b=Button(f,text='-',padx=27,pady=12,font='lucida 35 bold',bg='pink')
b.pack(side=LEFT,padx=18,pady=10)
b.bind('<Button-1>',click)
f.pack()


f=Frame(root,bg='black')
b=Button(f,text='1',padx=26,pady=12,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=10)
b.bind('<Button-1>',click)
b=Button(f,text='2',padx=26,pady=12,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=10)
b.bind('<Button-1>',click)
b=Button(f,text='3',padx=26,pady=12,font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=10)
b.bind('<Button-1>',click)
b=Button(f,text='+',padx=26,pady=12,font='lucida 35 bold' ,bg='pink')
b.pack(side=LEFT,padx=18,pady=10)
b.bind('<Button-1>',click)
f.pack()


f=Frame(root,bg='black')
b=Button(f,text='C',padx=27,pady=12,font='lucida 35 bold',bg='pink')
b.pack(side=LEFT,padx=18,pady=10)
b.bind('<Button-1>',click)
b=Button(f,text='0',padx=27,pady=12,font='lucida 35 bold',bg='pink')
b.pack(side=LEFT,padx=18,pady=10)
b.bind('<Button-1>',click)
b=Button(f,text='=',padx=27,pady=12,font='lucida 35 bold',bg='pink')
b.pack(side=LEFT,padx=18,pady=10)
b.bind('<Button-1>',click)
b=Button(f,text='/',padx=27,pady=12,font='lucida 35 bold',bg='pink')
b.pack(side=LEFT,padx=15,pady=10)
b.bind('<Button-1>',click)
f.pack()

root.mainloop()

