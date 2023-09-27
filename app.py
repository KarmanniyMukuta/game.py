from tkinter import*
from random import randint
number=randint(1, 10)

def click():
    
    global count 
    count+=1
    label2['text'] = f'Спроби: {count}'
    
    
    a=int(entry.get())
    if a<number:
        lable1.config(text="Більше")
    elif a>number:
        lable1.config(text="Менше")
    else:
        lable1.config(text="Вгадано")
        
count = 0
        

win=Tk()
win.title("Вгадай число by Mukuta K.")
win['bg'] = '#303030'
win.geometry("300x100")
lable1=Label (win, text="Введыть число від 1 до 10:")
lable1.pack()
entry=Entry(win, width=10)
entry.pack()
btn=Button(win, text="Вгадати", command=click)
btn.pack()

label2 = Label(win, text=f'Спроби: {count}', bg='red')
label2.pack()
win.mainloop()