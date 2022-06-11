from tkinter import *

from Secret_key import make_keypair, scalar_mult

current_priv, current_pub = make_keypair()
current_shared = scalar_mult(current_priv, current_pub)

window = Tk()
window.title("Эллиптическая криптография")
window.geometry('800x400')

private_key_label = Label(window, text="Приватный ключ")
private_key_label.grid(column=0, row=0, pady=5)

private_key_field = Entry(window)
private_key_field.grid(column=1, row=0, pady=5)


def generate_keypair_event():
    global current_priv, current_pub, current_shared
    current_priv, current_pub = make_keypair()
    current_shared = scalar_mult(current_priv, current_pub)
    public_key_field.delete(0, END)
    public_key_field.insert(0, f'{current_pub[0]:X},{current_pub[1]:X}')
    private_key_field.delete(0, END)
    private_key_field.insert(0, f'{current_priv:X}')


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


def encode():
    global current_shared
    message = message_input.get("1.0", END).strip()
    shared_mod = current_shared[0] % 100
    print("Secret key %X %X" % (current_shared[0], current_shared[1]))
    print("Shared modificator", shared_mod)
    converted_message = ""
    for ch in message:
        converted_message += "%X " % (ord(ch) + shared_mod)
    message_input.delete("1.0", END)
    message_input.insert("1.0", converted_message)


def decode():
    global current_priv
    message = message_input.get("1.0", END).strip().split(" ")
    pub_x, pub_y = map(lambda x: int(x, 16), sign_key_field.get().split(","))
    shared = scalar_mult(current_priv, (pub_x, pub_y))
    shared_mod = shared[0] % 100
    print("Secret key %X %X" % (shared[0], shared[1]))
    print("Shared modificator", shared_mod)
    converted_message = ""
    for ch in message:
        converted_message += chr(int(ch, 16) - shared_mod)
    message_input.delete("1.0", END)
    message_input.insert("1.0", converted_message.strip())


encode_button = Button(window, text="Закодировать", command=encode)
decode_button = Button(window, text="Раскодировать", command=decode)
encode_button.grid(row=5, column=0)
decode_button.grid(row=5, column=1)

window.mainloop()
