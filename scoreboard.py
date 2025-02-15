import pygame.font

class Scoreboard:
    """Uma classe para mostrar informações sobre pontuação."""

    def __init__(self, ai_settings, screen, stats):
        """Inicializa os atributos da pontuação."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Configurações de fonte para as informações de pontuação
        self.text_color = (30, 30, 30)  # Cor do texto (preto)
        self.font = pygame.font.SysFont(None, 48)  # Fonte do texto

        # Prepara a imagem da pontuação inicial
        self.prep_score()
    
    def prep_score(self):
        """Transforma a pontuação em uma imagem renderizada."""
        # Converte a pontuação em uma string
        score_str = str(self.stats.score)

        # Renderiza a pontuação como uma imagem
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # Posiciona a pontuação na parte superior direita da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20  # 20 pixels da borda direita
        self.score_rect.top = 20  # 20 pixels do topo

    def show_score(self):
        """Desenha a pontuação na tela."""
        # Desenha a imagem da pontuação na posição definida por score_rect
        self.screen.blit(self.score_image, self.score_rect)