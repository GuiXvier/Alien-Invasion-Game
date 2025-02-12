class Settings:
    """
    Uma classe para armazenar todas as configurações do jogo Alien Invasion.
    """
    def __init__(self):
        """
        Inicializa as configurações do jogo.
        """
        # Configurações da tela
        self.screen_width = 1200  # Largura da tela em pixels.
        self.screen_height = 800  # Altura da tela em pixels.
        self.bg_color = (230, 230, 230)  # Cor de fundo da tela no formato RGB (cinza claro).
        
        # Configurações da espaçonave 
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        
        # Configurações dos projéteis 
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        # Configurações dos alienígenas
        self.alien_speed_factor = 1  # Velocidade dos alienígenas
        self.fleet_drop_speed = 10   # Velocidade de descida quando atingem a borda
        self.fleet_direction = 1     # 1 para direita, -1 para esquerda
        
        
