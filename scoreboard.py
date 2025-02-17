import pygame.font
from pygame.sprite import Group
from ship import Ship

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

        # Prepara as imagens das pontuações iniciais
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_level(self):
        """Transforma o nível em uma imagem renderizada."""
        # Renderiza o nível como uma imagem
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        # Posiciona o nível abaixo da pontuação
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right  # Alinha à direita da pontuação
        self.level_rect.top = self.score_rect.bottom + 10  # Posiciona 10 pixels abaixo da pontuação
    
    def prep_score(self):
        """Transforma a pontuação em uma imagem renderizada."""
        # Converte a pontuação em uma string
        score_str = str(self.stats.score)
        
        # Arredonda a pontuação para o múltiplo de 10 mais próximo
        rounded_score = int(round(self.stats.score, -1))

        # Formata a pontuação com separadores de milhar
        score_str = "{:,}".format(rounded_score)

        # Renderiza a pontuação como uma imagem
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # Posiciona a pontuação na parte superior direita da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20  # 20 pixels da borda direita
        self.score_rect.top = 20  # 20 pixels do topo

    def show_score(self):
        """Desenha a pontuação na tela."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        
        # Desenha as espaçonaves 
        self.ships.draw(self.screen)

        
    def prep_high_score(self):
        """Transforma a pontuação máxima em uma imagem renderizada."""
        # Arredonda a pontuação máxima para o múltiplo de 10 mais próximo
        high_score = int(round(self.stats.high_score, -1))

        # Formata a pontuação máxima com separadores de milhar
        high_score_str = "{:,}".format(high_score)

        # Renderiza a pontuação máxima como uma imagem
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # Centraliza a pontuação máxima na parte superior da tela
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx  # Centraliza horizontalmente
        self.high_score_rect.top = self.score_rect.top  # Alinha ao topo da pontuação atual
        
    def prep_ships(self):
        """Mostra quantas espaçonaves restam."""
        # Cria um grupo para armazenar as imagens das espaçonaves
        self.ships = Group()

        # Cria uma espaçonave para cada vida restante
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)  # Cria uma nova instância da espaçonave
            ship.rect.x = 10 + ship_number * ship.rect.width  # Posiciona horizontalmente
            ship.rect.y = 10  # Posiciona verticalmente
            self.ships.add(ship)  # Adiciona a espaçonave ao grupo
    
