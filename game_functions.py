# Importação de bibliotecas necessárias
import sys  # Biblioteca padrão do Python para manipulação do sistema.
import pygame  # Biblioteca Pygame para desenvolvimento de jogos.

# Função reponsável por verificar os eventos do tipo Key Down (Pressionamento de tecla)
def check_keydown_events(event, ship):
    """
    Responde a pressionamento de tecla.
    Define as flasgs de movimento da espaçonave como True quando as teclas
    correspondentes são pressioandas
    """
    
    if event.key == pygame.K_RIGHT: # Tecla de seta para direita
        ship.moving_right = True
    elif event.key == pygame.K_LEFT: # Tecla de seta para esquerda
        ship.moving_left = True
        

# Função reponsável por verificar os eventos do tipo Key Up (Soltura de tecla)        
def check_keyup_events(event, ship):
    """
    Responde a solturas de tecla.
    Define as flasgs de movimento da espaçonave como false quando as teclas
    correspondentes são pressioandas
    """
    
    if event.key == pygame.K_RIGHT: # Tecla de seta para direita
        ship.moving_right = False
    elif event.key == pygame.K_LEFT: # Tecla de seta para esquerda
        ship.moving_left = False

def check_events(ship):
    """
    Responde a eventos de pressionamento de teclas e de mouse.

    Essa função monitora todos os eventos que ocorrem no jogo (como cliques de mouse,
    pressionamento de teclas ou solicitação de fechamento da janela) e executa ações 
    com base nesses eventos.
    """
    for event in pygame.event.get():  # Itera sobre todos os eventos na fila de eventos do Pygame.
        if event.type == pygame.QUIT:  # Verifica se o evento é o fechamento da janela.
            sys.exit()  # Encerra o programa de forma segura.
        
        elif event.type == pygame.KEYDOWN: # Pressionamento de uma tecla
            check_keydown_events(event, ship)
            
        elif event.type == pygame.KEYUP: # Soltura de uma tecla
            check_keyup_events(event, ship)
            

def update_screen(ai_settings, screen, ship):
    """
    Atualiza as imagens na tela e alterna para a nova tela.

    Essa função redesenha a tela a cada iteração do loop principal, atualizando
    todos os elementos gráficos (como o fundo, a nave, inimigos, etc.) com base
    nos estados mais recentes.
    """
    # Preenche a tela com a cor de fundo definida nas configurações.
    screen.fill(ai_settings.bg_color)

    # Desenha a espaçonave na posição atual da tela.
    ship.blitme()

    # Alterna para a nova tela renderizada.
    # O `pygame.display.flip()` atualiza toda a tela, substituindo a tela anterior.
    pygame.display.flip()
