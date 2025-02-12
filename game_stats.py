class GameStats:
    """
    Armazena dados estatísticos do jogo 'Invasão Alienígena'.
    """

    def __init__(self, ai_settings):
        """
        Inicializa os dados estatísticos do jogo.
        :param ai_settings: Instância das configurações do jogo.
        """
        self.ai_settings = ai_settings  # Armazena as configurações do jogo.
        self.reset_stats()  # Inicializa as estatísticas variáveis.
        # Inicia a Invasão Alienígena em um estado ativo 
        self.game_active = True 

    def reset_stats(self):
        """
        Inicializa as estatísticas que podem mudar durante o jogo.
        """
        self.ships_left = self.ai_settings.ship_limit  
