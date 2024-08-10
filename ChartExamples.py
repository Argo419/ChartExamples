# Примеры построения графиков

import tkinter as tk

# Функция закрытия программы
def do_close():
	window.destroy()

# Созданиие главного окна
window = tk. Tk()
window.geometry("450x450")
window.title("Примеры построения графиков")

# добавление кнопки закрытия программмы
btnClose = tk.Button(window, text="Zakryt", font = ('helvetica', 10, 'bold'),command=do_close)
btnClose.place(x=330, y=400, width=90, height=30)

# Запуск цикла mainloop
window.mainloop()
