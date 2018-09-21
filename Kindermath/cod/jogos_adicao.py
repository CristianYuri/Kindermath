from botao import Botao
from random import randint

class Jogo1(object):

	local_img = "../img/menu"
	local_som = "../som/"
	local_font = "../font/"

	lista_imgs = ["botao_padrao.png",
	              "botao_alternativo.png"] # Rever se usará lista ou dicionário

	lista_botoes = []  # Rever se usará lista ou dicionário

	lista_cores = [(255, 255, 255), (0, 0, 0)] # Rever se usará lista ou dicionário

	def __init__(self, amb, screen):
		self.amb = amb
		self.screen = screen