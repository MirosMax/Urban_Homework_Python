import tkinter as tk

window = tk.Tk()
window.title('Проводник')
window.geometry('450x500')
window.resizable(False, False)
window.configure(bg='white')

text = tk.Label(window, text='Файл:', width=15, height=5, background='#C9D5EE')
text.grid(column=1, row=1)

button_select = tk.Button(window, text='Выбрать файл', width=15, height=2)
button_select.grid(column=1, row=2)

window.mainloop()
