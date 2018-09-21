#Classe responsavel pela definicao, movimentacao, visibilidade e eventos do mouse
class Mouse(object):

	def __init__(self, amb, screen, local_arquivo, arquivo):
		self.amb = amb
		self.screen = screen
		self.local_arquivo = local_arquivo
		self.arquivo = arquivo
		
		self.carregar_mouse()
		self.definir_visib_cursor(False)

	def carregar_mouse(self):
		self.img = self.amb.image.load(self.local_arquivo + self.arquivo).convert_alpha()
		self.rect_img = self.img.get_rect()

	# Define a visibilidade do cursor do pygame
	def definir_visib_cursor(self, visibilidade=True):
		self.amb.mouse.set_visible(visibilidade)

	def tratar_mov_mouse(self):
		self.rect_img.x, self.rect_img.y = self.amb.mouse.get_pos()
		self.rect_img.x -= self.img.get_width()/6
		self.rect_img.y -= self.img.get_height()/50

		# Util para mover objetos na tela 
		self.mov_x, self.mov_y = self.amb.mouse.get_rel()

	def desenhar(self):
		self.tratar_mov_mouse()
		self.screen.blit(self.img, self.rect_img)
