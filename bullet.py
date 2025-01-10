import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Uma classe que administra projéteis disparados pela espaçonave"""
    
    def __init__(self, ai_settings, screen, ship):
        
        super(Bullet, self).__init__() # Inicializa a classe base Sprite
        self.screen = screen
        
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx # Centraliza o projétil com a espaçonave
        self.rect.top = ship.rect.top  # Define a posição inicial no topo da espaçonave

        # Armazena a posição do projétil como um valor decimal para movimento suave
        self.y = float(self.rect.y)

        # Atributos do projétil
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """
        Move o projétil para cima na tela.
        """
        self.y -= self.speed_factor  # Atualiza a posição Y do projétil
        self.rect.y = self.y  # Atualiza a posição do rect para refletir o movimento

    def draw_bullet(self):
        """
        Desenha o projétil na tela.
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        