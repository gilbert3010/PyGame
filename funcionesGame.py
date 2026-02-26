import sys
import pygame

def verificar_eventos(nave):
    # Observar eventos de teclado y de ratón
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                nave.rect.centerx += 1
                nave.moving_right = True
            elif event.key == pygame.K_LEFT:
                nave.rect.centerx -= 1
                nave.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                nave.moving_right = False
            elif event.key == pygame.K_LEFT:
                nave.moving_left = False    
            
def actualizar_pantalla(ai_config, pantalla, nave):
    # Redibujar la pantalla durante cada pasada por el bucle
    pantalla.fill(ai_config.bg_color)
    nave.blitme()
    
    # Redibujar la pantalla durante cada pasada por el bucle        
    pygame.display.flip()