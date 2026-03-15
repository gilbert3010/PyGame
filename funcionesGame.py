import sys
from time import sleep
import pygame
from balas import Bala
from alien import Alien


def verificar_eventos_keydown(evento, nave, ai_config, pantalla, balas):
    # Responde a las pulsaciones de teclas
    if evento.key == pygame.K_d or evento.key == pygame.K_RIGHT:
        nave.moving_right = True
    elif evento.key == pygame.K_a or evento.key == pygame.K_LEFT:
        nave.moving_left = True
    elif evento.key == pygame.K_SPACE:
        fuego_bala(ai_config, pantalla, nave, balas)
    elif evento.key == pygame.K_q:
        pygame.quit()
        sys.exit()


def verificar_eventos_keyup(evento, nave):
    # Responde al soltado de teclas
    if evento.key == pygame.K_d or evento.key == pygame.K_RIGHT:
        nave.moving_right = False
    elif evento.key == pygame.K_a or evento.key == pygame.K_LEFT:
        nave.moving_left = False


def verificar_eventos(ai_config, pantalla, estadisticas, play_button, nave, aliens, balas):
    # Observar eventos de teclado y de ratón
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            verificar_eventos_keydown(event, nave, ai_config, pantalla, balas)
        elif event.type == pygame.KEYUP:
            verificar_eventos_keyup(event, nave)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_config, pantalla, estadisticas, play_button, nave, aliens, balas, mouse_x, mouse_y)
            
def check_play_button(ai_config, pantalla, estadisticas, play_button, nave, aliens, balas, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    # Iniciar un nuevo juego al hacer clic en Play
    if button_clicked and not estadisticas.game_active:
        #restablece la configuración del juego a un estado inicial
        ai_config.inicializa_configuraciones_dinamicas()
        #ocultar el cursor del ratón
        pygame.mouse.set_visible(False)
        
        #restablece las estadisticas del juego
        estadisticas.reset_stats()  
        estadisticas.game_active = True
        
        # Vaciar listas de aliens y balas
        aliens.empty()
        balas.empty()
        
        # Crear una nueva flota y centrar la nave
        crear_flota(ai_config, pantalla, nave, aliens)
        nave.centrar_nave()


def actualizar_pantalla(ai_config, pantalla, estadisticas, marcador, nave, aliens, balas, play_button):
    # Redibujar la pantalla durante cada pasada por el bucle
    pantalla.fill(ai_config.bg_color)

    # Dibujar balas
    for bala in balas.sprites():
        bala.draw()

    # Dibujar nave y aliens
    nave.blitme()
    aliens.draw(pantalla)
    
    # Dibujar el marcador
    marcador.muestra_puntaje()
    
    #dibuja el boton de play si el juego esta inactivo
    if not estadisticas.game_active:
        play_button.draw_button()

    # Hacer visible el nuevo cuadro de pantalla
    pygame.display.flip()


def update_balas(ai_config, pantalla, estadisticas, marcador, nave, balas, aliens):
    # Actualiza las posiciones de las balas y se deshace de las antiguas
    balas.update()

    # Eliminar balas que han desaparecido
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)

    check_bala_alien_collisions(ai_config, pantalla, estadisticas, marcador, nave, aliens, balas)


def check_bala_alien_collisions(ai_config, pantalla, estadisticas, marcador, nave, aliens, balas):
    # Comprobar colisiones balas–aliens
    collisions = pygame.sprite.groupcollide(balas, aliens, True, True)
    
    if collisions:
        for aliens in collisions.values():
            estadisticas.puntaje += ai_config.puntos_alien * len(aliens)
            marcador.prep_puntaje()
    
    # Si se destruyen todos los aliens, crear nueva flota
    if len(aliens) == 0:
        balas.empty()
        ai_config.aumentar_velocidad()
        crear_flota(ai_config, pantalla, nave, aliens)


def fuego_bala(ai_config, pantalla, nave, balas):
    # Crear una nueva bala y agregarla al grupo de balas
    if len(balas) < ai_config.balas_permitidas:
        nueva_bala = Bala(ai_config, pantalla, nave)
        balas.add(nueva_bala)


def get_number_aliens_x(ai_config, alien_width):
    # Determina el número de aliens que caben en una fila
    available_space_x = ai_config.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_config, nave_height, alien_height):
    # Determina el número de filas de aliens que caben en la pantalla
    available_space_y = (
        ai_config.screen_height - (3 * alien_height) - nave_height
    )
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def crear_alien(ai_config, pantalla, aliens, alien_number, row_number):
    # Crea un alien y lo coloca en la fila
    alien = Alien(ai_config, pantalla)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def crear_flota(ai_config, pantalla, nave, aliens):
    # Crea una flota completa de aliens
    alien = Alien(ai_config, pantalla)
    number_aliens_x = get_number_aliens_x(ai_config, alien.rect.width)
    number_rows = get_number_rows(
        ai_config, nave.rect.height, alien.rect.height
    )

    # Crear cada fila de aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            crear_alien(ai_config, pantalla, aliens, alien_number, row_number)


def check_fleet_edges(ai_config, aliens):
    # Responde apropiadamente si algún alien ha llegado al borde de la pantalla
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_config, aliens)
            break


def change_fleet_direction(ai_config, aliens):
    # Baja toda la flota y cambia la dirección de la flota
    for alien in aliens.sprites():
        alien.rect.y += ai_config.fleet_drop_speed
    ai_config.fleet_direction *= -1


def nave_golpeada(ai_config, estadisticas, pantalla, nave, aliens, balas):
    # Responde a la nave siendo golpeada por un alien
    if estadisticas.naves_restantes > 0:
        # Disminuir naves restantes
        estadisticas.naves_restantes -= 1

        # Vaciar listas de aliens y balas
        aliens.empty()
        balas.empty()

        # Crear una nueva flota y centrar la nave
        crear_flota(ai_config, pantalla, nave, aliens)
        nave.centrar_nave()   

        # Pausa
        sleep(0.5)
    else:
        estadisticas.game_active = False
        pygame.mouse.set_visible(True)
        

def check_aliens_bottom(ai_config, estadisticas, pantalla, nave, aliens, balas):
    # Comprueba si algún alien ha llegado al fondo de la pantalla
    pantalla_rect = pantalla.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= pantalla_rect.bottom:
            # Tratar esto como si la nave hubiera sido golpeada
            nave_golpeada(ai_config, estadisticas, pantalla, nave, aliens, balas)
            break




def update_aliens(ai_config, estadisticas, pantalla, nave, aliens, balas):
    # Comprueba si la flota está en el borde y actualiza la posición de los aliens
    check_fleet_edges(ai_config, aliens)
    aliens.update()

    # Busca colisiones alien–nave
    if pygame.sprite.spritecollideany(nave, aliens):
        nave_golpeada(ai_config, estadisticas, pantalla, nave, aliens, balas)
    
    #busca aliens que han llegado al fondo de la pantalla
    check_aliens_bottom(ai_config, estadisticas, pantalla, nave, aliens, balas)
