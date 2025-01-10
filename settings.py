import ctypes  # Biblioteca que fornece acesso a funções e estruturas de baixo nível, como interações com o sistema operacional.

class Settings:
    """
    Uma classe para armazenar todas as configurações do jogo.

    Essa classe contém atributos que definem as propriedades básicas do jogo,
    como dimensões da tela e cor de fundo. Esses atributos são usados por 
    outras partes do programa para manter consistência e facilitar ajustes globais.
    """
    
    def __init__(self):
        """
        Inicializa os atributos de configuração do jogo.
        """
        
        """
            Configurações da tela
        """
        # Obtém a interface para manipular a resolução da tela usando a biblioteca ctypes.
        self.user32 = ctypes.windll.user32
        
        # Define a largura da tela do jogo como 1200 pixels.
        self.screen_width = 1200
        
        # Define a altura da tela do jogo com base na altura total do monitor do sistema.
        # A função `GetSystemMetrics(1)` retorna a altura da tela do monitor principal.
        # Subtrai 100 pixels para criar uma margem na interface do jogo.
        self.screen_height = self.user32.GetSystemMetrics(1) - 100
        
        # Define a cor de fundo da tela do jogo em formato RGB (Red, Green, Blue).
        # Nesse caso, a cor é um roxo escuro, representado por (22, 8, 47).
        self.bg_color = (22, 8, 47)
        
        """
            Configurações da espaçonave
        """
        
        self.ship_speed_factor = 1.5
        
        """
            Configurações dps projéteis
        """
        
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 255
        self.bullets_allowed = 3
