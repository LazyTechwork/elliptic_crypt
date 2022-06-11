from tkinter import *

from Secret_key import make_keypair

window = Tk()
window.title("Эллиптическая криптография")
window.geometry('800x400')

private_key_label = Label(window, text="Приватный ключ")
private_key_label.grid(column=0, row=0, pady=5)

private_key_field = Entry(window)
private_key_field.grid(column=1, row=0, pady=5)


def generate_keypair_event():
    priv, pub = make_keypair()
    public_key_field.delete(0, END)
    public_key_field.insert(0, f'{pub[0]:X}')
    private_key_field.delete(0, END)
    private_key_field.insert(0, f'{priv:X}')


generate_keypair = Button(window, text="Сгенерировать пару ключей", command=generate_keypair_event)
generate_keypair.grid(column=2, row=0, pady=5)

public_key_label = Label(window, text="Публичный ключ")
public_key_label.grid(column=0, row=1, pady=5)

public_key_field = Entry(window)
public_key_field.grid(column=1, row=1, pady=5)

message_input_label = Label(window, text="Введите сообщение")
message_input_label.grid(row=2, column=0, columnspan=2)

message_input = Text(window, width=50, height=6)
message_input.grid(row=3, column=0, columnspan=2, pady=10)

sign_key_label = Label(window, text="Ключ подписания")
sign_key_label.grid(column=0, row=4, pady=5)

sign_key_field = Entry(window)
sign_key_field.grid(column=1, row=4, pady=5)

encode_button = Button(window, text="Закодировать")
decode_button = Button(window, text="Раскодировать")
encode_button.grid(row=5, column=0)
decode_button.grid(row=5, column=1)

window.mainloop()
