from tkinter import *

window = Tk()

window.title("Counter")

def increase():
    current_value = int(lbl_counter["text"])
    lbl_counter["text"] = str(current_value + 1)

def decrease():
    current_value = int(lbl_counter["text"])
    lbl_counter["text"] = str(current_value - 1)

window.rowconfigure(0,minsize=100,weight=1)
window.columnconfigure([0,1,2],minsize=50,weight=1)

btn_decrease = Button(master=window,text="-" , command=decrease)
btn_decrease.grid(row=0,column=0,sticky="nsew")

lbl_counter = Label(master=window,text="0")
lbl_counter.grid(row=0,column=1)

btn_increse = Button(master=window,text="+",command=increase)
btn_increse.grid(row=0,column=2,sticky="nsew")

window.mainloop()