import sys
import pygame
from bullet import Bullet
from alien import Alien

def update_screen(ai_settings, screen, ship, aliens, bullets): 
    """
    Atualiza as imagens na tela e alterna para a nova tela.

    Essa função é chamada a cada iteração do loop principal para redesenhar
    a tela com os elementos atualizados.
    """
    # Preenche a tela com a cor de fundo definida nas configurações.
    screen.fill(ai_settings.bg_color)
    
    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()


    # Desenha a espaçonave na posição atual.
    ship.blitme()
    
    aliens.draw(screen)

    # Torna visível a tela mais recente desenhada.
    pygame.display.flip()

def check_keydown_events(event, ai_settings, screen, ship, bullets): 
    """
    Responde a pressionamentos de tecla.
    Define as flags de movimento da espaçonave como True quando as teclas
    correspondentes são pressionadas.
    """
    if event.key == pygame.K_RIGHT:  # Tecla de seta para a direita
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # Tecla de seta para a esquerda
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q: 
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """Dispara um projétil se o limite ainda não foi alcançado."""
    # Verifica se o número de projéteis na tela está abaixo do limite
    if len(bullets) < ai_settings.bullets_allowed:
        # Cria um novo projétil e o adiciona ao grupo de projéteis
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """
    Responde a solturas de tecla.
    Define as flags de movimento da espaçonave como False quando as teclas
    correspondentes são liberadas.
    """
    if event.key == pygame.K_RIGHT:  # Tecla de seta para a direita
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:  # Tecla de seta para a esquerda
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """
    Responde a eventos de pressionamento de teclas e de mouse.
    Identifica os eventos capturados e chama as funções apropriadas para
    processá-los.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Fechamento da janela
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # Pressionamento de uma tecla
             check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:  # Soltura de uma tecla
            check_keyup_events(event, ship)

def update_bullets(bullets):
    """Atualiza a posição dos projéteis e remove os que estão fora da tela."""
    # Atualiza as posições dos projéteis
    bullets.update()

    # Remove projéteis que saíram da tela
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:  # Se o projétil estiver fora da tela
            bullets.remove(bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """Determina o número de alienígenas que cabem em uma linha."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """
    Cria um alienígena e o posiciona na linha e coluna especificada.
    """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """
    Cria uma frota completa de alienígenas.
    """
    # Cria um alienígena para calcular o número de alienígenas em uma linha
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    # Cria a frota de alienígenas
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
        
def get_number_rows(ai_settings, ship_height, alien_height):
    """
    Determina o número de linhas com alienígenas que cabem na tela.
    """
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

     
def check_fleet_edges(ai_settings, aliens):
    """Responde apropriadamente se algum alienígena alcançou uma borda."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break  # Sai do loop após encontrar um alienígena na borda

def change_fleet_direction(ai_settings, aliens):
    """Faz toda a frota descer e muda a sua direção."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed  # Move a frota para baixo
    ai_settings.fleet_direction *= -1  # Inverte a direção da frota

def update_aliens(ai_settings, aliens):
    """
    Verifica se a frota está em uma das bordas e então atualiza as posições
    de todos os alienígenas da frota.
    """
    check_fleet_edges(ai_settings, aliens)  # Checa se a frota deve mudar de direção
    aliens.update()  # Move os alienígenas
