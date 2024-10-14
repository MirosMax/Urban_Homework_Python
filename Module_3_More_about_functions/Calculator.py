import tkinter as tk

def get_values():
    num1 = int(number_1_entry.get())
    num2 = int(number_2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry('400x400')
window.resizable(False, False)
button_add = tk.Button(window, text='+', width=2, height=2, command=add)
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text='-', width=2, height=2, command=sub)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text='*', width=2, height=2, command=mul)
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text='/', width=2, height=2, command=div)
button_div.place(x=250, y=200)
number_1_entry = tk.Entry(window, width=30)
number_1_entry.place(x=100, y=75)
number_2_entry = tk.Entry(window, width=30)
number_2_entry.place(x=100, y=130)
answer_entry = tk.Entry(window, width=30)
answer_entry.place(x=100, y=300)
number_1 = tk.Label(window, text='Введите первое число')
number_1.place(x=100, y=50)
number_2 = tk.Label(window, text='Введите второе число')
number_2.place(x=100, y=105)
answer = tk.Label(window, text='Результат')
answer.place(x=100, y=275)
window.mainloop()

