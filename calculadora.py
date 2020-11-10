from functools import partial
from tkinter import *


def bt_click(bt):

    if str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric():
        x = float(ed1.get())
        y = float(ed2.get())
        if bt == 1:
            lb4["text"] = x+y
        elif bt == 2:
            lb4["text"] = x-y
        elif bt == 3:
            lb4["text"] = x*y
        elif bt == 4:
            lb4["text"] = x/y
    else:
        lb4["text"] = "Algum valor informado inválido!"


janela = Tk()
janela.title("Calculadora")
janela["bg"] = "azure"
janela["background"] = "azure"

lb1 = Label(janela, text="Digite um número:")
lb2 = Label(janela, text="Digite outro número:")
lb3 = Label(janela, text="Resultado:")
lb4 = Label(janela, text="_")

bt1 = Button(janela, width=20, text="Soma")
bt2 = Button(janela, width=20, text="Subtração")
bt3 = Button(janela, width=20, text="Multiplicação")
bt4 = Button(janela, width=20, text="Divisão")

ed1 = Entry(janela)
ed2 = Entry(janela)

bt1["command"] = partial(bt_click, 1)
bt2["command"] = partial(bt_click, 2)
bt3["command"] = partial(bt_click, 3)
bt4["command"] = partial(bt_click, 4)

lb1.place(x=8, y=8)
lb2.place(x=8, y=32)
lb3.place(x=256, y=32)
lb4.place(x=320, y=32)

ed1.place(x=128, y=8)
ed2.place(x=128, y=32)

bt1.place(x=8, y=64)
bt2.place(x=160, y=64)
bt3.place(x=320, y=64)
bt4.place(x=480, y=64)

# largura x altura + distancia da margem esquerda + distancia da margem do topo
janela.geometry("640x100+160+160")

janela.mainloop()
