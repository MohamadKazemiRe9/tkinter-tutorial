import tkinter as tk

window = tk.Tk()

window.title("temp convertor")

def temp_convert():
    far = ent_temp.get()
    cel = (5/9) * (float(far) - 32)
    lbl_result["text"] = f"{round(cel,2)} \N{DEGREE CELSIUS}"

frm_entry = tk.Frame(master=window)
ent_temp = tk.Entry(master=frm_entry,width=10)
lbl_temp = tk.Label(master=frm_entry,text="\N{DEGREE FAHRENHEIT}")

ent_temp.grid(row=0,column=0)
lbl_temp.grid(row=0,column=1)

btn_convert = tk.Button(master=window,text="\N{RIGHTWARDS BLACK ARROW}",command=temp_convert)
lbl_result = tk.Label(master=window,text="\N{DEGREE CELSIUS}")

frm_entry.grid(row=0,column=0)
btn_convert.grid(row=0,column=1)
lbl_result.grid(row=0,column=2)

window.mainloop()