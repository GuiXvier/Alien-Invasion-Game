import pygame  # Biblioteca Pygame para gráficos e jogos.
import pygame.image  # Submódulo do Pygame para manipulação de imagens.

class Ship:
    """
    Representa a espaçonave do jogador no jogo.

    Essa classe gerencia a imagem da nave, sua posição na tela e o método para desenhá-la.
    """
    
    def __init__(self, ai_settings,screen):
        """
        Inicializa a espaçonave e define sua posição inicial.

        :param screen: Superfície onde a nave será desenhada, geralmente a tela principal do jogo.
        """
        self.screen = screen  # Referência à tela onde a nave será desenhada.
        self.ai_settings = ai_settings

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
        
        # Armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)
        
        # Flags de movimento
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """
        Atualiza a posição da espaçonave de acordo com as flags de movimento.
        O movimento é limitado pelos limites da tela.
        """
        # Verifica se o movimento para a direita está ativo e se a espaçonave não ultrapassou o limite direito
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor # Incrementa a posição do centro
        
        # Verifica se o movimento para a esquerda está ativo e se a espaçonave não ultrapassou o limite esquerdo
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # Atualiza a posição do retângulo com base no valor atualizado do centro
        self.rect.centerx = self.center
        
    def blitme(self):
        """
        Desenha a espaçonave na posição atual.

        Utiliza o método `blit` da superfície `screen` para desenhar a imagem da nave 
        na posição especificada pelo retângulo `rect`.
        """
        self.screen.blit(self.image, self.rect)
