from tkinter import *
import requests
import json

w = Tk()
w.title('student interface')
w.geometry('900x600')
fnt = ('Courier', 24)
url = "http://localhost:5000/api/addstudent"


def onclick():
    print('name: ' + n1.get())
    print('phnum: ' + p1.get())
    print('proglang: ' + g1.get())
    print('joindate: ' + j1.get())
    payload = json.dumps({
        "name": n1.get(),
        "phnum": p1.get(),
        "proglang": g1.get(),
        "joindate": j1.get()
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json())


n0 = Label(w, text='name -> ', font=fnt)
n0.grid(row=0, column=0)
n1 = Entry(w, width=20, font=fnt)
n1.grid(row=0, column=1)

p0 = Label(w, text='phone -> ', font=fnt)
p0.grid(row=1, column=0)
p1 = Entry(w, width=20, font=fnt)
p1.grid(row=1, column=1)

g0 = Label(w, text='proglang -> ', font=fnt)
g0.grid(row=2, column=0)
g1 = Entry(w, width=20, font=fnt)
g1.grid(row=2, column=1)

j0 = Label(w, text='joindate -> ', font=fnt)
j0.grid(row=3, column=0)
j1 = Entry(w, width=20, font=fnt)
j1.grid(row=3, column=1)

blank = Label(w, text=' ')
blank.grid(row=4, column=0)
sb = Button(w, text='submit', font=fnt, command=onclick)
sb.grid(row=5, column=1, sticky='e')

# event loop
w.mainloop()
