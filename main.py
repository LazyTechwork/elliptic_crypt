from tkinter import *

window = Tk()
window.title("Эллиптическая криптография")
window.geometry('800x400')

active_private_key_label = Label(window, text="Текущий приватный ключ")
active_private_key_label.grid(column=0, row=0, pady=10)

choose_private_key_button = Button(window, text="Выбрать ключ")
choose_private_key_button.grid(column=2, row=0, pady=10)

active_private_key_text = Entry(window)
active_private_key_text.insert(0, "./")
active_private_key_text.grid(column=1, row=0, pady=10)

generate_keypairs_button = Button(window, text="Сгенерировать пары ключей")
generate_keypairs_button.grid(column=0, row=1, columnspan=3, pady=5)

message_input_label = Label(window, text="Введите сообщение")
message_input_label.grid(row=2, column=0, columnspan=2)

message_input = Text(window, width=50, height=6)
message_input.grid(row=3, column=0, columnspan=2, pady=10)

encode_button = Button(window, text="Закодировать")
decode_button = Button(window, text="Раскодировать")
encode_button.grid(row=4, column=0)
decode_button.grid(row=4, column=1)

window.mainloop()
