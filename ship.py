import pygame  # Biblioteca Pygame para gráficos e jogos.
import pygame.image  # Submódulo do Pygame para manipulação de imagens.

class Ship:
    """
    Representa a espaçonave do jogador no jogo.

    Essa classe gerencia a imagem da nave, sua posição na tela e o método para desenhá-la.
    """
    
    def __init__(self, screen):
        """
        Inicializa a espaçonave e define sua posição inicial.

        :param screen: Superfície onde a nave será desenhada, geralmente a tela principal do jogo.
        """
        self.screen = screen  # Referência à tela onde a nave será desenhada.

        # Carrega a imagem da nave do arquivo especificado.
        # O caminho 'images/ship.bmp' deve ser válido e conter a imagem.
        self.image = pygame.image.load('images/ship.bmp')  
        
        # Obtém o retângulo da imagem da nave, que é usado para posicionar a imagem na tela.
        self.rect = self.image.get_rect()
        
        # Obtém o retângulo da tela, usado como referência para alinhar a nave na tela.
        self.screen_rect = screen.get_rect()
        
        # Define a posição inicial da nave:
        # Centraliza a nave horizontalmente no centro da tela.
        self.rect.centerx = self.screen_rect.centerx
        # Posiciona a parte inferior da nave na parte inferior da tela.
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """
        Desenha a espaçonave na posição atual.

        Utiliza o método `blit` da superfície `screen` para desenhar a imagem da nave 
        na posição especificada pelo retângulo `rect`.
        """
        self.screen.blit(self.image, self.rect)
