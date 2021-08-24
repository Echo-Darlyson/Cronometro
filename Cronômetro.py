import tkinter as tk
from functools import partial
from time import sleep

tela = tk.Tk()
tela.geometry("203x203")
tela.title("Cronômetro")

fotobotao = tk.PhotoImage(file = "botaoverm.png").subsample(4, 4)

#Função Cronômetro
def Cronômetro(label):
	m = 0
	while True:
		if m < 10:
			m1 = f"0{m}"
		else:
			m1 = m
		for s in range (60):
			if s < 10:
				label.caixa["text"] = f"{m1} : 0{s}"
			else:
				label.caixa["text"] = f"{m1} : {s}"
			label.caixa.update()
			sleep(1)
		m += 1
	
			
#Molde para os Botões
class Botão:
	def __init__(self, texto, x, y, comando, pos, tam = 1, fonte = "Arial"):
		self.botão = tk.Button(tela, text = texto, command = comando, font = (fonte, tam))
		self.botão.place(relx = x, rely = y, anchor = pos)


#Molde para os Labels
class CaixaTexto:
	def __init__(self, tam = 1, fonte = "Arial"):
		self.caixa = tk.Label(tela, font = (fonte, tam))


#CaixaDeTexto
back = CaixaTexto()
back.caixa.place(x = 0, y = 0)
back.caixa["bg"] = "White"
back.caixa["width"] = 203
back.caixa["height"] = 203
l1 = CaixaTexto(30, "Bauhaus 93")
l1.caixa["bg"] = "White"
l1.caixa["fg"] = "Red"
l1.caixa.place(relx = .5, rely = .3, anchor = "center")


#Botão
b1 = Botão("Começar", .5, .8, partial(Cronômetro, l1), "center")
b1.botão["border"] = 0
b1.botão["image"] = fotobotao
b1.botão["activebackground"] = "White"
b1.botão["bg"] = "White"
b1.botão["highlightthickness"] = 0


tela.mainloop()
