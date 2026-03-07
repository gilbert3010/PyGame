import sys
import pygame
from balas import Bala
from alien import Alien




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
        fuego_bala(ai_config, pantalla, nave, balas)
    elif evento.key == pygame.K_q:
        sys.exit()




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
            
def actualizar_pantalla(ai_config, pantalla, nave, aliens, balas):
    # Redibujar la pantalla durante cada pasada por el bucle
    pantalla.fill(ai_config.bg_color)
    # Vuelve a dibujar todas las balas detras de la nave y luego dibuja la nave
    for bala in balas.sprites():
        bala.draw_bala()
        
    nave.blitme()
    aliens.draw(pantalla)
    
    # Redibujar la pantalla durante cada pasada por el bucle        
    pygame.display.flip()



def update_balas(balas):
    #actualiza la posicion de las alas y elimina las antiguas
    #actualiza las posiciones de las balas y se deshace de las antiguas
    balas.update()
    
    #deshace las balas antiguas
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)
            
def fuego_bala(ai_config, pantalla, nave, balas):
    #crear una nueva bala y agregarla al grupo de balas
    if len(balas) < ai_config.balas_permitidas:
        nueva_bala = Bala(ai_config, pantalla, nave)
        balas.add(nueva_bala)


def get_number_aliens_x(ai_config, alien_width):
    #determina el numero de aliens que caben en una fila
    available_space_x = ai_config.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_config, nave_height, alien_height):
    #determina el numero de filas de aliens que caben en la pantalla
    available_space_y = (ai_config.screen_height - (3 * alien_height) - nave_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def crear_alien(ai_config, pantalla, aliens, alien_number, row_number):
    #crea un alien y lo coloca en la fila
    alien = Alien(ai_config, pantalla)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def crear_flota(ai_config, pantalla, nave, aliens):
    #crea una flota completa de aliens
    #crear un alien y encontrar el numero de aliens en una fila
    #el espacio entre cada alien es igual al ancho de un alien
    alien = Alien(ai_config, pantalla)
    number_aliens_x = get_number_aliens_x(ai_config, alien.rect.width)
    number_rows = get_number_rows(ai_config, nave.rect.height, alien.rect.height)
    
    #crear la primera fila de aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            crear_alien(ai_config, pantalla, aliens, alien_number, row_number)
