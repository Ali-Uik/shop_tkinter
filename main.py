import tkinter as tk


def add_prod_info(string):
    prod_info.insert(0, string)


window = tk.Tk()
window.geometry(f"550x550+100+100")
window.resizable(False, False)
logo = tk.PhotoImage(file='icon.png')
window.iconphoto(False, logo)
window.config(bg='#77DB8B')
window.title("Sotuvchi")
font_button = ('Times New Roman', 12)

# row = 0
tk.Button(text='Qidirish', bd=2, font=font_button).grid(row=0, column=0, stick='wens', padx=5, pady=5)
tk.Button(text='Hisobot', bd=2, font=font_button).grid(row=0, column=1, stick='wens', padx=5, pady=5)
tk.Button(text='Sozlash', bd=2, font=font_button).grid(row=0, column=2, stick='wens', padx=5, pady=5)
tk.Button(text='Kalkulyator', bd=2, font=font_button).grid(row=0, column=3, stick='wens', padx=5, pady=5)
salesman_info = tk.Label(window, text='Kassir: John Uik', font=('Times New Roman', 12, 'bold'), padx=20, fg='red',
                         relief=tk.RAISED).grid(row=0, column=4, stick='wens', padx=5, pady=5)

# window.grid_columnconfigure(0, minsize=60)
# window.grid_columnconfigure(1, minsize=60)
# window.grid_columnconfigure(2, minsize=60)
# window.grid_columnconfigure(3, minsize=60)
# window.grid_rowconfigure(0, minsize=60)
# window.grid_rowconfigure(1, minsize=60)
# window.grid_rowconfigure(2, minsize=60)
# window.grid_rowconfigure(3, minsize=60)

prod_info = tk.Entry(window, font=('Times New Roman', 15), relief=tk.RAISED)
calc_info = tk.Entry(window, font=('Times New Roman', 15), relief=tk.RAISED)
# row 1
prod_info.grid(row=1, column=0, columnspan=4, stick='we', padx=5)
calc_info.grid(row=1, column=4, rowspan=5, stick='wens', padx=5)

# row 2
product_info = tk.Label(window, text='Ko\'p sotiladigan mahsulotlar', font=('Times New Roman', 12, 'bold'), fg='red', relief=tk.RAISED).\
    grid(row=2, column=0, columnspan=4, stick='we', padx=5, pady=5)
# row 3
tk.Button(text='Non', bd=2, font=font_button, command=lambda: add_prod_info('Non')). \
    grid(row=3, column=0, stick='wens', padx=5, pady=5)
tk.Button(text='Shakar', bd=2, font=font_button, command=lambda: add_prod_info('Shakar')). \
    grid(row=3, column=1, stick='wens', padx=5, pady=5)
tk.Button(text='Un', bd=2, font=font_button, command=lambda: add_prod_info('Un')). \
    grid(row=3, column=2, stick='wens', padx=5, pady=5)
tk.Button(text='Tuz', bd=2, font=font_button, command=lambda: add_prod_info('Tuz')). \
    grid(row=3, column=3, stick='wens', padx=5, pady=5)
# row 4
tk.Button(text='Suv 10 l', bd=2, font=font_button, command=lambda: add_prod_info('Suv 10 l')). \
    grid(row=4, column=0, stick='wens', padx=5, pady=5)
tk.Button(text='Suv 5 l', bd=2, font=font_button, command=lambda: add_prod_info('Suv 5 l')). \
    grid(row=4, column=1, stick='wens', padx=5, pady=5)
tk.Button(text='Suv 1 l', bd=2, font=font_button, command=lambda: add_prod_info('Suv 1 l')). \
    grid(row=4, column=2, stick='wens', padx=5, pady=5)
tk.Button(text='Suv 0.5 l', bd=2, font=font_button, command=lambda: add_prod_info('Suv 0.5 l')). \
    grid(row=4, column=3, stick='wens', padx=5, pady=5)
# row 5
tk.Button(text='Tuxum', bd=2, font=font_button, command=lambda: add_prod_info('Tuxum')). \
    grid(row=5, column=0, stick='wens', padx=5, pady=5)
tk.Button(text='Yog\'', bd=2, font=font_button, command=lambda: add_prod_info('Yog\'')). \
    grid(row=5, column=1, stick='wens', padx=5, pady=5)
tk.Button(text='Britva', bd=2, font=font_button, command=lambda: add_prod_info('Britva')). \
    grid(row=5, column=2, stick='wens', padx=5, pady=5)
tk.Button(text='Sovun', bd=2, font=font_button, command=lambda: add_prod_info('Sovun')). \
    grid(row=5, column=3, stick='wens', padx=5, pady=5)
window.mainloop()
