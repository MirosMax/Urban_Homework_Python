import tkinter as tk
import os
from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(initialdir='.', title='Выберите файл',
                                          filetypes=(('Текстовый файл', '.txt'),
                                                        ('Файл Python', '.py'),
                                                        ('Все файлы', '*')))

    text['text'] += '\n' + filename
    os.startfile(filename)


window = tk.Tk()
window.title('Проводник')
window.geometry('550x150')
window.resizable(False, False)
window.configure(bg='white')

text = tk.Label(window, text='Файл:', width=80, height=5, background='#C9D5EE', foreground='#00308F')
text.grid(column=1, row=1)

button_select = tk.Button(window, text='Выбрать файл', width=15, height=2, background='#C9D5EE',
                          foreground='#00308F', command=file_select)
button_select.grid(column=1, row=2, pady=5)
window.mainloop()
