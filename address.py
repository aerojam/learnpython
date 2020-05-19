import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Address Entry Form')
window.minsize(400, 260)

frm_address = tk.Frame(master=window)
frm_address.columnconfigure(0, weight=0)
frm_address.columnconfigure(1, weight=1)

lbl_first_name = tk.Label(master=frm_address, text='First Name:')
ent_first_name = tk.Entry(master=frm_address)
lbl_first_name.grid(column=0, row=0, sticky='w', padx=5, pady=3)
ent_first_name.grid(column=1, row=0, sticky='we', padx=5, pady=3)

lbl_last_name = tk.Label(master=frm_address, text='Last Name:')
ent_last_name = tk.Entry(master=frm_address)
lbl_last_name.grid(column=0, row=1, sticky='w', padx=5, pady=3)
ent_last_name.grid(column=1, row=1, sticky='we', padx=5, pady=3)

lbl_address1 = tk.Label(master=frm_address, text='Address Line 1:')
ent_address1 = tk.Entry(master=frm_address)
lbl_address1.grid(column=0, row=2, sticky='w', padx=5, pady=3)
ent_address1.grid(column=1, row=2, sticky='we', padx=5, pady=3)

lbl_address2 = tk.Label(master=frm_address, text='Address Line 2:')
ent_address2 = tk.Entry(master=frm_address)
lbl_address2.grid(column=0, row=3, sticky='w', padx=5, pady=3)
ent_address2.grid(column=1, row=3, sticky='we', padx=5, pady=3)

lbl_city = tk.Label(master=frm_address, text='City:')
ent_city = tk.Entry(master=frm_address)
lbl_city.grid(column=0, row=4, sticky='w', padx=5, pady=3)
ent_city.grid(column=1, row=4, sticky='we', padx=5, pady=3)

lbl_state = tk.Label(master=frm_address, text='State/Province:')
ent_state = tk.Entry(master=frm_address)
lbl_state.grid(column=0, row=5, sticky='w', padx=5, pady=3)
ent_state.grid(column=1, row=5, sticky='we', padx=5, pady=3)

lbl_code = tk.Label(master=frm_address, text='Postal Code:')
ent_code = tk.Entry(master=frm_address)
lbl_code.grid(column=0, row=6, sticky='w', padx=5, pady=3)
ent_code.grid(column=1, row=6, sticky='we', padx=5, pady=3)

lbl_country = tk.Label(master=frm_address, text='Country:')
ent_country = tk.Entry(master=frm_address)
lbl_country.grid(column=0, row=7, sticky='w', padx=5, pady=3)
ent_country.grid(column=1, row=7, sticky='we', padx=5, pady=3)

frm_address.pack(fill=tk.X)

def btn_cancel_clicked():
    window.destroy()

def btn_submit_clicked():
    address = {}
    address['first_name'] = ent_first_name.get()
    address['last_name'] = ent_last_name.get()
    address['address1'] = ent_address1.get()
    address['address2'] = ent_address2.get()
    address['city'] = ent_city.get()
    address['state'] = ent_state.get()
    address['code'] = ent_code.get()
    address['country'] = ent_country.get()
    tk.messagebox.showinfo(title='Address', message=address)

frm_buttons = tk.Frame(master=window)
frm_buttons_group = tk.Frame(master=frm_buttons)
btn_submit = tk.Button(
    master=frm_buttons_group,
    text='OK',
    width=10,
    command=btn_submit_clicked)
btn_submit.pack(side=tk.LEFT, padx=6)
btn_cancel = tk.Button(
    master=frm_buttons_group,
    text='Cancel',
    width=10,
    command=btn_cancel_clicked)
btn_cancel.pack(side=tk.LEFT)
frm_buttons_group.pack(side=tk.RIGHT)
frm_buttons.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=8)

tk.mainloop()
