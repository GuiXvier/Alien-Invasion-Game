import pygame  # Importa o módulo pygame para manipulação de jogos.
from settings import Settings  # Importa a classe Settings para acessar as configurações do jogo.
from ship import Ship  # Importa a classe Ship para controlar a espaçonave.
import game_functions as gf  # Importa o módulo game_functions para funções auxiliares do jogo.
from pygame.sprite import Group  # Importa a classe Group para gerenciar grupos de sprites.
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    """
    Inicializa o jogo Alien Invasion e gerencia a execução principal.
    """
    # Inicializa o pygame e configura a janela do jogo.
    pygame.init()  # Inicializa todos os módulos necessários do pygame.
    
    # Cria uma instância da classe Settings, que contém todas as configurações do jogo.
    ai_settings = Settings()
    
    # Cria uma instância da classe GameStats para armazenar os dados estatísticos do jogo
    stats = GameStats(ai_settings)

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
    sb = Scoreboard(ai_settings, screen, stats) 
    
    # Cria a frota de alienígenas
    gf.create_fleet(ai_settings, screen, ship, aliens)  # Chama a função para criar a frota de alienígenas.
    
    pygame.display.set_caption("Alien Invasion")
    
    # Cria o botão Play
    play_button = Button(ai_settings, screen, "Play")

    # Inicia o laço principal do jogo
    while True:
        # Verifica eventos de entrada (teclado/mouse)
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)  # Processa eventos de teclado e mouse.
        
        if stats.game_active:
            # Atualiza a posição da espaçonave
            ship.update()  # Atualiza a posição da espaçonave com base nas flags de movimento.
            
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)  # Atualiza a posição dos projéteis e remove os que saíram da tela.
            
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
    
        # Atualiza a tela com as novas posições
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)  # Redesenha a tela com os elementos atualizados.


# Inicia o jogo chamando a função principal.
run_game()