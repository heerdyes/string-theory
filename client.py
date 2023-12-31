from tkinter import *

w = Tk()
w.title('student interface')
w.geometry('900x600')

# event handlers
def onquery():
  inp = t.get()
  t.delete(0, END)
  o.configure(text=inp)


# font tuple
f0 = ('OCRA', 14)

# label
l = Label(w, text='message:', font=f0)
l.grid(column=0, row=0)
# text input
t = Entry(w, width=16, font=f0)
t.grid(column=1, row=0)
# buttons
b = Button(w, text='query', font=f0, command=onquery)
b.grid(column=0, row=1)
# display label
o = Label(w, text='', font=f0)
o.grid(column=0, row=2)

# focus on the entry field
t.focus()

# event loop
w.mainloop()

