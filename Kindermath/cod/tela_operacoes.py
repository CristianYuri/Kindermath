from botao import Botao

class TelaOperacoes(object):

	local_img = "../img/tela_operacoes"
	local_som = "../som/"
	local_font = "../font/"

	lista_imgs = ["botao_padrao.png",
	              "botao_alternativo.png"] # Rever se usará lista ou dicionário

	lista_opcoes = ["Adição",
	                "Subtração",
	                "Multiplicação"] 

	lista_botoes = []  # Rever se usará lista ou dicionário

	lista_cores = [(255, 255, 255), (0, 0, 0)] # Rever se usará lista ou dicionário

	comando = ""

	def __init__(self, amb, screen, pos_inicial, dist_bloco):
		self.amb = amb
		self.screen = screen
		self.pos_inicial = pos_inicial
		self.dist_bloco = dist_bloco
		self.criar_botoes()

	def criar_botoes(self):
		for texto in self.lista_opcoes:
			self.lista_botoes.append(Botao(self.amb, self.screen, self.lista_imgs, self.pos_inicial, texto, self.local_font + "FreeSerif.ttf", self.lista_cores))
			self.pos_inicial = (self.pos_inicial[0] + 320, self.pos_inicial[1])

	# def para definir ações de cada opção do menu ao ser selecionada
	def selecionar_opcao(self, campo):
		if self.comando == "Adição":
			print("adicao")

		elif self.comando == "Subtração":
			print("subtracao")

		elif self.comando == "Multiplicação":
			print("multiplicacao")

	def tratar_eventos(self, campo, clique):
		for botao in self.lista_botoes:
			botao.tratar_eventos(self, clique)
			self.selecionar_opcao(campo)
			self.comando = ""

	def desenhar(self):
		for botao in self.lista_botoes:
			botao.desenhar()