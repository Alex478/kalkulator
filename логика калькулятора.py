import tkinter as tk
from PIL import Image, ImageTk

def plus(): # ф. сложения - готово
    M.append(en2.get())
    M.append('+')
    en2.delete(0, 100)
def minus(): #
    M.append(en2.get())
    M.append('-')
    en2.delete(0, 100)
def pro(): # 
    M.append(en2.get())
    M.append('*')
    en2.delete(0, 100)
def delen(): # 
    M.append(en2.get())
    M.append('/')
    en2.delete(0, 100)

def ravno():# ф. выводит итог - готово ( нужно сделать для более 2х значений)
    b = en2.get()
    M.append(b)
    print(M)
    en2.delete(0,100)
    if M[1] == s[0]:
        x = int(M[0]) + int(M[2])
    elif M[1] == s[1]:
        x = int(M[0]) - int(M[2])
    elif M[1] == s[2]:
        x = int(M[0]) / int(M[2])
    elif M[1] == s[3]:
        x= int(M[0]) * int(M[2])
    return en2.insert(0, x)

def knop(n):# заменяет цифру в текстовом поле на ту, что на кнопке - не готово
    en2.insert('end',str(n))
    return

def sbros(): # ф. очищает поле расчета
    global M
    M = []
    return en2.delete(0,100)

x = 500
y = 500
root = tk.Tk()
root.geometry('{}x{}'.format(x, y))
root.attributes("-alpha", 0.9) # полупрозрачное окно
# поле для расчета
#lab1 = tk.Label(width= 16, font= 'Arial 36', bg = 'white')
#lab1.place(x= 20, y= 25)
en2 = tk.Entry(root, width= 15, font='Arial 36',justify= 'center',
               background= 'white')
en2.place(x= 20, y= 25)

#кнопки
class but:
    def __init__(self, text, x1, y1):
        self.but = tk.Button(font= 'Arial 30', width=3, text = text)
        self.but.place(x= x1, y= y1)
class but_formula:
    def __init__(self, text, x1, y1, command):
        self.but = tk.Button(font= 'Arial 30', width=3, text = text,
                             command= command)
        self.but.place(x= x1, y= y1)
        
# создание кнопок - проблема присвоить команду без начального введения цифр
Koor1 = [[20,120],[140,120],[260,120],[20,215],[140,215],[260,215],
        [20,310],[140,310],[260,310]] # координаты для кнопок с цифрами
for i in range(len(Koor1)): # кнопки с цифрами
    but_formula(i + 1, Koor1[i][0], Koor1[i][1],
                lambda x = i + 1: knop(x))
but_formula(0, 20,405, lambda x = 0: knop(x)) # кнопка с цифрами

but_formula('C', 380,120,sbros) # кнопки с формулами
but_formula('+', 380,215, plus) # кнопки с формулами
but_formula('-', 380,310, minus) # кнопки с формулами
but_formula('=', 140,405, ravno) # кнопки с формулами
but_formula('/', 260,405, delen) # кнопки с формулами
but_formula('*', 380,405, pro) # кнопки с формулами

sbros()#  для начала очистить поле  
# логика  - нужно использовать стек - пока для 2х элементов,
#                                       надо и больше придумать
M = [] # стек
s = ('+','-','/','*')



        
root.mainloop()
