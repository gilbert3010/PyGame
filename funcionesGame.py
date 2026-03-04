import sys
import pygame
from balas import Bala


def verificar_eventos_keydown(evento, nave, ai_config, pantalla, balas):
#responde a las pulsaciones de teclas
    if evento.key == pygame.K_RIGHT:
        nave.rect.centerx += 1
        nave.moving_right = True
    elif evento.key == pygame.K_LEFT:
        nave.rect.centerx -= 1
        nave.moving_left = True
    elif evento.key == pygame.K_SPACE:
        #crear una nueva bala y agregarla al grupo de balas
        nueva_bala = Bala(ai_config, pantalla, nave)
        balas.add(nueva_bala)


def verificar_eventos_keyup(evento, nave):
#responde a las pulsaciones de teclas
    if evento.key == pygame.K_RIGHT:
        nave.moving_right = False
    elif evento.key == pygame.K_LEFT:
        nave.moving_left = False


def verificar_eventos(ai_config, pantalla, nave, balas):
    # Observar eventos de teclado y de ratón
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            verificar_eventos_keydown(event, nave, ai_config, pantalla, balas)
        elif event.type == pygame.KEYUP:
            verificar_eventos_keyup(event, nave)
            
def actualizar_pantalla(ai_config, pantalla, nave, balas):
    # Redibujar la pantalla durante cada pasada por el bucle
    pantalla.fill(ai_config.bg_color)
    # Vuelve a dibujar todas las balas detras de la nave y luego dibuja la nave
    for bala in balas.sprites():
        bala.draw_bala()
        
    nave.blitme()
    
    # Redibujar la pantalla durante cada pasada por el bucle        
    pygame.display.flip()
