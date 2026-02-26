import sys
import pygame

def run_game():
    # Inicializar el juego y crear una ventana de juego
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("invasion alienigena")
    # Iniciar el bucle principal del juego
    while True:
        # Observar eventos de teclado y de ratón
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Redibujar la pantalla durante cada pasada por el bucle        
        pygame.display.flip()
        
run_game()