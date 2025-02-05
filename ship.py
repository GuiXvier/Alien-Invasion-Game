import pygame

class Ship:
    """Uma classe para gerenciar a espaçonave."""
    
    def __init__(self, ai_settings,screen):
        """
        Inicializa a espaçonave e define sua posição inicial.
        
        Parâmetros:
        - screen: Superfície onde a espaçonave será desenhada.
        """
        self.screen = screen  # Armazena a superfície da tela para desenhar a espaçonave.
        self.ai_settings = ai_settings
        
        # Carrega a imagem da espaçonave e obtém seu rect (retângulo delimitador).
        self.image = pygame.image.load('images/ship.bmp')  # Carrega a imagem da espaçonave.
        self.rect = self.image.get_rect()  # Obtém as dimensões e posição do retângulo da imagem.
        self.screen_rect = screen.get_rect()  # Obtém o retângulo da tela.
        
        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
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
            self.center += self.ai_settings.ship_speed_factor  # Incrementa a posição do centro

        # Verifica se o movimento para a esquerda está ativo e se a espaçonave não ultrapassou o limite esquerdo
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor  # Decrementa a posição do centro

        # Atualiza a posição do retângulo com base no valor atualizado do centro
        self.rect.centerx = self.center


    
    def blitme(self):
        """
        Desenha a espaçonave na posição atual.
        
        Utiliza o método `blit` para desenhar a imagem na tela com base no retângulo `rect`.
        """
        self.screen.blit(self.image, self.rect)
