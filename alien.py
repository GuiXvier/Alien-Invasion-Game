import pygame  # Importa o módulo pygame para manipulação de gráficos.
from pygame.sprite import Sprite  # Importa a classe Sprite para criar sprites.
from PIL import Image  # Importa a classe Image da biblioteca PIL para manipulação de imagens.

class Alien(Sprite):
    """Uma classe que representa um único alienígena da frota."""
    
    def __init__(self, ai_settings, screen):
        """Inicializa o alienígena e define sua posição inicial."""
        super(Alien, self).__init__()  # Inicializa a classe base Sprite.
        self.screen = screen  # Armazena a superfície da tela para desenhar o alienígena.
        self.ai_settings = ai_settings  # Armazena as configurações do jogo.
        # Configurações dos alienígenas 
        self.alien_speed_factor = 1
        
        # Carrega a imagem do alienígena, redimensiona e salva como BMP
        image_alien = Image.open('images/alien.png')  # Abre a imagem do alienígena.
        new_image = image_alien.resize((75, 75))  # Redimensiona a imagem para 75x75 pixels.
        new_image.save('images/alien.bmp')  # Salva a imagem redimensionada como BMP.

        self.image = pygame.image.load('images/alien.bmp')  # Carrega a imagem redimensionada no pygame.
        self.rect = self.image.get_rect()  # Obtém o retângulo delimitador da imagem.

        # Inicia cada novo alienígena próximo à parte superior esquerda da tela
        self.rect.x = self.rect.width  # Define a posição X inicial.
        self.rect.y = self.rect.height  # Define a posição Y inicial.

        # Armazena a posição exata do alienígena
        self.x = float(self.rect.x)  # Armazena a posição X como um valor decimal para movimentos suaves.

    def blitme(self):
        """Desenha o alienígena em sua posição atual."""
        self.screen.blit(self.image, self.rect)  # Desenha o alienígena na tela.
        
    def check_edges(self):
        """Devolve True se o alienígena estiver na borda da tela."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        return False
        
    def update(self):
        """Move o alienígena para a direita ou para a esquerda."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x