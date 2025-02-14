import pygame.font  # Import necessário para usar fontes no pygame

class Button():
    """
    Classe para criar e exibir um botão na tela do jogo.
    """

    def __init__(self, ai_settings, screen, msg):
        """
        Inicializa os atributos do botão.
        """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Define as dimensões e propriedades do botão
        self.width, self.height = 200, 50  # Largura e altura do botão
        self.button_color = (0, 255, 0)  # Cor do botão (verde)
        self.text_color = (255, 255, 255)  # Cor do texto (branco)
        self.font = pygame.font.SysFont(None, 48)  # Fonte do texto

        # Constrói o objeto rect do botão e o centraliza na tela
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # A mensagem do botão deve ser preparada apenas uma vez
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """
        Transforma a mensagem em uma imagem renderizada e centraliza o texto no botão.
        """
        # Renderiza o texto como uma imagem
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        
        # Obtém o retângulo da imagem do texto e centraliza no botão
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):  
        # Desenha um botão em branco e, em seguida, desenha a mensagem  
        self.screen.fill(self.button_color, self.rect)  
        self.screen.blit(self.msg_image, self.msg_image_rect)  

