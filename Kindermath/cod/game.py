import pygame
from mouse import Mouse
from menu import Menu
from tela_operacoes import TelaOperacoes

class Game(object):

	local_img = "../img/"
	local_som = "../som/"
	local_font = "../font/"

	dict_tela = {"menu": True,
				 "tela_operacoes": False,
				 "jogo": False}

	rodando = True

	# construtor, responsável pela inicialização
	def __init__(self, titulo, tamanho_tela):
		self.amb = pygame
		self.amb.init()
		self.amb.display.set_caption(titulo)
		self.screen_size = largura, altura = tamanho_tela
		self.screen = self.amb.display.set_mode(self.screen_size, 0, 32)
		#self.clock = self.amb.time.Clock()

	def rodar(self):
		self.mouse = Mouse(self.amb, self.screen, self.local_img, "minion_mouse.png")
		self.menu = Menu(self.amb, self.screen, (400, 25), 50)
		self.tela_operacoes = TelaOperacoes(self.amb, self.screen, (100, 200), 50)

		while self.rodando:
			self.screen.fill((0, 0, 0))

			for event in self.amb.event.get():
				if event.type == self.amb.QUIT:
					self.rodando = False

				eventos_mouse = pygame.mouse.get_pressed()

				if self.dict_tela["menu"]:
					self.menu.tratar_eventos(self, eventos_mouse)
				elif self.dict_tela["tela_operacoes"]:
					self.tela_operacoes.tratar_eventos(self, eventos_mouse)
			
			if self.dict_tela["menu"]:
				self.menu.desenhar()
			elif self.dict_tela["tela_operacoes"]:
				self.tela_operacoes.desenhar()
			
			self.mouse.desenhar()

			self.amb.display.flip()
			#self.clock.tick(20)

		self.amb.quit()

if __name__ == "__main__":
    g = Game("KINDERMATH",(1000,700))
    g.rodar()