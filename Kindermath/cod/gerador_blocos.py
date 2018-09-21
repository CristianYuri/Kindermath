from bloco import Bloco
from random import randint

class GeradorBlocos(object):

	lista_blocos = []
	resposta = 0

	def __init__(self, amb, screen, local_img, operacao):
		self.amb = amb
		self.screen = screen
		self.local_img = local_img
		self.operacao = operacao

		self.tratar_operacao()
		self.criar_blocos()
		self.lista_blocos[randint(0, 3)].gerar_texto(str(self.resposta))

	def tratar_operacao(self):
		if self.operacao == "adicao":
			numero1 = randint(0, 20)
			numero2 = randint(0, 20)
			self.resposta = numero1 + numero2
			self.questao = (str(numero1) + " + " + str(numero2))

	def gerar_numeros(self):
		num = randint(0, 20)
		
		while num == self.resposta:
			num = randint(0, 20)

		return num


	def tratar_eventos(self, clique, pos_mouse):
			for bloco in self.lista_blocos:
				if bloco.rect_objeto.collidepoint(pos_mouse):
					bloco.img = "alternativa.png"
					bloco.carregar_objeto()

					if clique == (1, 0, 0):
						print(int(bloco.num))
						if int(bloco.num) == self.resposta:
							print("Voce acertou, parabens!")
						else:
							print("Voce errou, otario!")
				else:
					bloco.img = "bloco_alternativa.png"
					bloco.carregar_objeto()


	# TEMPORARIO - iSSO É UM TESTE
	def criar_blocos(self):
		self.lista_blocos = [Bloco(self.amb, self.screen, self.local_img, "bloco_alternativa.png", (250, 200), str(self.gerar_numeros())),
		                     Bloco(self.amb, self.screen, self.local_img, "bloco_alternativa.png", (550, 200), str(self.gerar_numeros())),
		                     Bloco(self.amb, self.screen, self.local_img, "bloco_alternativa.png", (250, 450), str(self.gerar_numeros())),
		                     Bloco(self.amb, self.screen, self.local_img, "bloco_alternativa.png", (550, 450), str(self.gerar_numeros()))
		                     ]
		self.bloco_principal = Bloco(self.amb, self.screen, self.local_img, "bloco_resposta.png", (225, 0), self.questao)

	def desenhar(self):
		for bloco in self.lista_blocos:
			bloco.desenhar()

		self.bloco_principal.desenhar()
