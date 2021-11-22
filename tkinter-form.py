import tkinter as tk
from tkinter import StringVar , OptionMenu


window = tk.Tk()
window.title("مشخصات کاربر")

lbl_title = tk.Label(text="فرم زیر را پر کنید" ,bg="#3211af",fg="#fff",font=(None,20,"bold"),pady=10)
lbl_title.pack(fill=tk.X)

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()


lbl_first_name = tk.Label(master=frm_form, text=":نام")
ent_first_name = tk.Entry(master=frm_form, width=50)

lbl_first_name.grid(row=0, column=1, sticky="w")
ent_first_name.grid(row=0, column=0)

lbl_last_name = tk.Label(master=frm_form, text=":نام خوانوادگی")
ent_last_name = tk.Entry(master=frm_form, width=50)

lbl_last_name.grid(row=1, column=1, sticky="w")
ent_last_name.grid(row=1, column=0)

lbl_postl_code = tk.Label(master=frm_form, text=":کد پستی")
ent_postl_code = tk.Entry(master=frm_form, width=50)

lbl_postl_code.grid(row=2, column=1, sticky="w")
ent_postl_code.grid(row=2, column=0)

lbl_address = tk.Label(frm_form,text=":آدرس")
ent_address = tk.Text(frm_form,width=37,height=4)

lbl_address.grid(row=3,column=1,sticky="w")
ent_address.grid(row=3,column=0)


options = [
    "اصفهان",
    "تهران",
    "اهواز",
    "کرمان",
    "یزد",
    "تبریز",
    "مشهد"
]
  
clicked = StringVar()
  
clicked.set( "شهر محل سکونت" )
  
drop = OptionMenu( window , clicked , *options )
drop.pack()

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

btn_clear = tk.Button(master=frm_buttons, text="Clear")
btn_clear.pack(side=tk.RIGHT, ipadx=10)

window.mainloop()