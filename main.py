import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


window = customtkinter.CTk()
window.title('Генератор')
window.geometry('600x600')


customtkinter.CTkLabel(window, text='Кол-во паролей: ').place(x=180,y=30)
entry_count = customtkinter.CTkEntry(window, width=50)
entry_count.place(x=290, y=30)

customtkinter.CTkLabel(window, text='Длинна пароля: ').place(x=180,y=60)
entry_len = customtkinter.CTkEntry(window, width=50)
entry_len.place(x=290, y=60)

btn_clear = customtkinter.CTkButton(window, text='Очистить')
btn_clear.place(x=350, y=100)

btn_generate = customtkinter.CTkButton(window, text='Генерировать')
btn_generate.place(x=150, y=100)

text_field = customtkinter.CTkTextbox(window, width=560, height=400)
text_field.place(x=20, y=150)


window.mainloop()