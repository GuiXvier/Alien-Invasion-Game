import pygame  # Importa o módulo pygame para manipulação de jogos.
from settings import Settings  # Importa a classe Settings para acessar as configurações do jogo.
from ship import Ship  # Importa a classe Ship para controlar a espaçonave.
import game_functions as gf  # Importa o módulo game_functions para funções auxiliares do jogo.
from pygame.sprite import Group  # Importa a classe Group para gerenciar grupos de sprites.
from alien import Alien  # Importa a classe Alien para criar e gerenciar alienígenas.

def run_game():
    """
    Inicializa o jogo Alien Invasion e gerencia a execução principal.
    """
    # Inicializa o pygame e configura a janela do jogo.
    pygame.init()  # Inicializa todos os módulos necessários do pygame.
    
    # Cria uma instância da classe Settings, que contém todas as configurações do jogo.
    ai_settings = Settings()

    # Inicializa a tela com as dimensões especificadas nas configurações.
    # O método pygame.display.set_mode() define o tamanho da tela baseado nos atributos
    # `screen_width` e `screen_height` da instância `ai_settings`.
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    
    # Cria uma espaçonave, um grupo de projéteis e um grupo de alienígenas
    ship = Ship(ai_settings, screen)  # Instancia a espaçonave.
    bullets = Group()  # Cria um grupo para armazenar os projéteis.
    aliens = Group()  # Cria um grupo para armazenar os alienígenas.
    
    # Cria a frota de alienígenas
    gf.create_fleet(ai_settings, screen, ship, aliens)  # Chama a função para criar a frota de alienígenas.

    # Inicia o laço principal do jogo
    while True:
        # Verifica eventos de entrada (teclado/mouse)
        gf.check_events(ai_settings, screen, ship, bullets)  # Processa eventos de teclado e mouse.
        
        # Atualiza a posição da espaçonave
        ship.update()  # Atualiza a posição da espaçonave com base nas flags de movimento.
        
        gf.update_bullets(bullets)  # Atualiza a posição dos projéteis e remove os que saíram da tela.
        
        gf.update_aliens(aliens)
        
        # Atualiza a tela com as novas posições
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)  # Redesenha a tela com os elementos atualizados.


# Inicia o jogo chamando a função principal.
run_game()