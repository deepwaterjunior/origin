from tkinter import *
from tkinter import scrolledtext
import SnlisGen
from SnlisGen import randomizer


def random():
    return randomizer()

# Окно программы
window = Tk()
window.geometry('300x600')
window.title("ГЕНЕРАТОР СНИЛС")

# вывод текста

file = open('snilsList.txt', 'r+')
data = file.read()

txt = scrolledtext.ScrolledText(window, width=40, height=40)
txt.grid(column=1, row=3)
txt.insert(1.0, data)

# кнопка
btn = Button(window, text="Сгенерировать СНИЛС", command=random())
btn.grid(column=1, row=0)


window.mainloop()
