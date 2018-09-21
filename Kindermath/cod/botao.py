class Botao(object):

	local_img = "../img/"
	local_som = "../som/"
	local_font = "../font/"

	dict_botao = {"esquerdo":(1, 0, 0),
	              "meio":    (0, 1, 0),
	              "direito": (0, 0, 1)}

	def __init__(self, amb, screen, lista_imgs, pos_botao, texto, arq_font, lista_cores):
		self.amb = amb
		self.screen = screen
		self.lista_imgs = lista_imgs # lista das imagens que formam o botao (padrao e alternativo)
		self.pos_botao = pos_botao
		self.lista_cores = lista_cores # cores do texto dentro do botao
		self.texto = texto
		self.fonte = self.amb.font.Font(self.local_font + arq_font, 40)

		self.carregar_botao(self.lista_imgs[0]) # self.carregar_botao(self.dict_imgs["padrao"]) 
		self.gerar_texto(self.lista_cores[0]) # self.gerar_texto(self.dict_cores["padrao"])

	def carregar_botao(self, img):
		self.botao = self.amb.image.load(self.local_img + img).convert_alpha()
		self.rect_botao = self.botao.get_rect()
		self.rect_botao.x, self.rect_botao.y = self.pos_botao

	def gerar_texto(self, cor):
		self.texto_render = self.fonte.render(self.texto, 1, cor)
		self.gerar_pos_texto()

	def gerar_pos_texto(self):
		pos_x, pos_y = self.rect_botao.center

		pos_x -= self.texto_render.get_width() / 2
		pos_y -= self.texto_render.get_height() / 2
		
		self.pos_texto = (pos_x, pos_y)

	def tratar_eventos(self, campo, clique):
		if self.rect_botao.collidepoint(self.amb.mouse.get_pos()):
			self.carregar_botao(self.lista_imgs[1])
			if clique == self.dict_botao["esquerdo"]:
				campo.comando = self.texto
		else:
			self.carregar_botao(self.lista_imgs[0])

	def desenhar(self):
		self.screen.blit(self.botao, self.rect_botao)
		self.screen.blit(self.texto_render, self.pos_texto)

""" 
				if bot.rect_objeto.collidepoint((self.mouse.rect_mouse.x, self.mouse.rect_mouse.y)):
					if bot.img_alter != " ":
						bot.carregar_objeto(bot.img_alter)
					
					if bot.cor_alter != " ":
						bot.gerar_texto(bot.cor_alter)
				else:
					bot.carregar_objeto(bot.img)
					bot.gerar_texto(bot.cor_padrao)

					"""
