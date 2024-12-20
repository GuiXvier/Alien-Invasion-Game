# Importação das bibliotecas e módulos necessários
import pygame  # Biblioteca para criação de jogos 2D.
from settings import Settings  # Módulo que contém configurações personalizadas do jogo.
from ship import Ship  # Classe que define o comportamento e características da nave.
import game_functions as gf  # Módulo com funções auxiliares para o jogo.

# Definição da função principal que inicia e executa o jogo.
def run_game():
    # Inicializa o pygame e seus componentes.
    pygame.init()
    
    # Criação de uma instância de Settings para carregar as configurações do jogo.
    game_settings = Settings()
    
    # Define a tela de exibição com as dimensões especificadas em game_settings.
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    
    # Define o título da janela do jogo.
    pygame.display.set_caption("Alien Invasion")
    
    # Criação de uma instância de Ship, representando a nave controlada pelo jogador.
    # A nave é desenhada na tela criada anteriormente.
    ship = Ship(screen)
    
    # Inicia o loop principal do jogo, mantendo o jogo em execução até que o jogador saia.
    while True:
        # Chama uma função do módulo game_functions para verificar eventos.
        # Essa função, geralmente, verifica inputs como pressionamento de teclas ou cliques do mouse.
        gf.check_events()
        
        # Atualiza a tela com base no estado atual do jogo, redesenhando os elementos.
        # Os argumentos fornecidos permitem que a função acesse as configurações,
        # a tela e o objeto da nave para redesenhar ou ajustar a interface.
        gf.update_screen(game_settings, screen, ship)
    
# Inicia o jogo chamando a função run_game.
run_game()
