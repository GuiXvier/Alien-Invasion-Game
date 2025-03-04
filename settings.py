import ctypes
class Settings:
    """
    Uma classe para armazenar todas as configurações do jogo Alien Invasion.
    """
    def __init__(self):
        """Inicializa as configurações estáticas do jogo."""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # Cor de fundo da tela (cinza claro)

        # Configurações da espaçonave
        self.ship_limit = 3  # Número máximo de vidas/naves

        # Configurações dos projéteis
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)  # Cor dos projéteis (cinza escuro)
        self.bullets_allowed = 3  # Número máximo de projéteis na tela

        # Configurações dos alienígenas
        self.fleet_drop_speed = 30  # Velocidade de descida da frota de alienígenas

        # Taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1
        
        # A taxa com que os pontos para cada alienígena aumentam
        self.score_scale = 1.5

        # Inicializa as configurações dinâmicas do jogo
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Inicializa as configurações que mudam no decorrer do jogo."""
        # Velocidade da espaçonave
        self.ship_speed_factor = 6.75

        # Velocidade dos projéteis
        self.bullet_speed_factor = 13.5

        # Velocidade dos alienígenas
        self.alien_speed_factor = 4.5

        # Direção da frota de alienígenas (1 = direita, -1 = esquerda)
        self.fleet_direction = 1
        
        # Pontuação 
        self.alien_points = 50
        
    def increase_speed(self):
        """Aumenta as configurações de velocidade."""
        # Aumenta a velocidade da espaçonave
        self.ship_speed_factor *= self.speedup_scale

        # Aumenta a velocidade dos projéteis
        self.bullet_speed_factor *= self.speedup_scale

        # Aumenta a velocidade dos alienígenas
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        
