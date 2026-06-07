import customtkinter
import tkinter 
import random

customtkinter.set_appearance_mode("dark") # графическе стили
customtkinter.set_default_color_theme("blue")

chars = 'qwertyuiopasdfghjklzxcvbnm' #символы
symbols = '!@#$%^&*()_+"№;:?-=}{]['
numbers = '0123456789'

chars = list(chars+chars.upper()+symbols+numbers) # список символов


def generate(): #функция для кнопки "генерировать"
    len_passwords = int(entry_len.get())
    count_passwords = int(entry_count.get())
    for i in range(count_passwords): # цикл для количества паролей
        password = ''
        for j in range(len_passwords): # цикл количества символов
            password += random.choice(chars)
        text_field.insert(tkinter.END, password + '\n') # вывод паролей в текствое поле


def clear(): # функция очистки тестового поля
    text_field.delete(0.0, tkinter.END)



window = customtkinter.CTk() # графическое окно
window.title('Генератор паролей') # навзвание окна
window.geometry('600x600') # размеры окна


customtkinter.CTkLabel(window, text='Кол-во паролей: ').place(x=180,y=30) # виджет "количество паролей"
entry_count = customtkinter.CTkEntry(window, width=50) # поле для ввода количества паролей и его размер
entry_count.place(x=290, y=30) # расположение этого поля

customtkinter.CTkLabel(window, text='Длинна пароля: ').place(x=180,y=60) # виджет "длинна паролей"
entry_len = customtkinter.CTkEntry(window, width=50) # поле для ввода длинны паролей и его размер
entry_len.place(x=290, y=60) # расположение этого поля

btn_clear = customtkinter.CTkButton(window, text='Очистить', command = clear) # кнопка "очистить" + привязка в функции "очистить"
btn_clear.place(x=350, y=100) # расположение этой кнопки

btn_generate = customtkinter.CTkButton(window, text='Генерировать', command = generate) # кнопка "генерировать" + привязка в функции "генерировать"
btn_generate.place(x=150, y=100) # расположение этой кнопки

text_field = customtkinter.CTkTextbox(window, width=560, height=400) # текстовое поле для вывода паролей
text_field.place(x=20, y=150) # расположение этого поля

window.mainloop() # не дает окну закрыться после запуска