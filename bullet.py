import pygame  # Importa o módulo pygame para manipulação de gráficos.
from pygame.sprite import Sprite  # Importa a classe Sprite para criar sprites.

class Bullet(Sprite):
    """Uma classe que administra projéteis disparados pela espaçonave."""
    
    def __init__(self, ai_settings, screen, ship):
        """
        Cria um objeto para o projétil na posição atual da espaçonave.
        
        Args:
            ai_settings: Configurações do jogo.
            screen: Superfície onde o projétil será desenhado.
            ship: Objeto da espaçonave que dispara o projétil.
        """
        super(Bullet, self).__init__()  # Inicializa a classe base Sprite.
        self.screen = screen  # Armazena a superfície da tela para desenhar o projétil.

        # Cria um retângulo para o projétil em (0, 0) e define a posição inicial
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)  # Define o retângulo do projétil.
        self.rect.centerx = ship.rect.centerx  # Centraliza o projétil com a espaçonave.
        self.rect.top = ship.rect.top  # Define a posição inicial no topo da espaçonave.

        # Armazena a posição do projétil como um valor decimal para movimento suave
        self.y = float(self.rect.y)  # Armazena a posição Y como um valor decimal.

        # Atributos do projétil
        self.color = ai_settings.bullet_color  # Define a cor do projétil.
        self.speed_factor = ai_settings.bullet_speed_factor  # Define a velocidade do projétil.

    def update(self):
        """
        Move o projétil para cima na tela.
        """
        self.y -= self.speed_factor  # Atualiza a posição Y do projétil.
        self.rect.y = self.y  # Atualiza a posição do retângulo para refletir o movimento.

    def draw_bullet(self):
        """
        Desenha o projétil na tela.
        """
        pygame.draw.rect(self.screen, self.color, self.rect)  # Desenha o projétil na tela.