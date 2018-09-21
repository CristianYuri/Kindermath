import pygame
from menu import Menu
from botao import Botao
from mouse import Mouse

class Game(object):

	local_img = "../img/"
	local_som = "../som/"
	local_font = "../font/"

	rodando = True

	# construtor, responsável pela inicialização
	def __init__(self, titulo, tamanho_tela):
		self.amb = pygame
		self.amb.init()
		self.amb.display.set_caption(titulo)
		self.screen_size = largura, altura = tamanho_tela
		self.screen = self.amb.display.set_mode(self.screen_size, 0, 32)

	def rodar(self):
		self.mouse = Mouse(self.amb, self.screen, self.local_img, "minion_mouse.png")
		self.menu = Menu(self.amb, self.screen, (400, 25), 50)

		while self.rodando:
			self.screen.fill((0, 0, 0))

			for event in self.amb.event.get():
				if event.type == self.amb.QUIT:
					self.rodando = False

				eventos_mouse = pygame.mouse.get_pressed()

				self.menu.tratar_eventos(self, eventos_mouse)

			self.menu.desenhar()
			self.mouse.desenhar()

			self.amb.display.flip()

		self.amb.quit()

if __name__ == "__main__":
    g = Game("KINDERMATH",(1000,700))
    g.rodar()