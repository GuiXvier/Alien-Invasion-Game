import pygame  # Importa o módulo pygame para manipulação de jogos.
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

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
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # Cria a frota de alienígenas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Inicia o laço principal do jogo
    while True:
        # Verifica eventos de entrada (teclado/mouse)
        gf.check_events(ai_settings, screen, ship, bullets)
        
        # Atualiza a posição da espaçonave
        ship.update()
        
        gf.update_bullets(bullets)
        
        # Atualiza a tela com as novas posições
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


# Inicia o jogo chamando a função principal.
run_game()
