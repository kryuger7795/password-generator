import customtkinter


window = customtkinter.CTk()
window.title('Генератор')
window.geometry('600x600')



entry_count = customtkinter.CTkEntry(window, width=10)
entry_count.place(x=290, y=30)


entry_len = customtkinter.CTkEntry(window, width=10)
entry_len.place(x=290, y=60)

window.mainloop()