import sys
import pygame
from pygame.sprite import Group

from configuraciones import Configuraciones
from estadisticas import Estadisticas
from button import Button
from nave import Nave
import funcionesGame as fg


def run_game():
    # Inicializar el juego y crear un objeto para almacenar la configuración
    pygame.init()
    ai_config = Configuraciones()
    pantalla = pygame.display.set_mode(
        (ai_config.screen_width, ai_config.screen_height)
    )
    pygame.display.set_caption("Invasión alienígena")
    
    #crea el botón Play
    play_button = Button(ai_config, pantalla, "Play")

    # Crea una instancia para almacenar estadísticas del juego
    estadisticas = Estadisticas(ai_config)

    # Crear una nave
    nave = Nave(ai_config, pantalla)

    # Crear grupos para balas y aliens
    balas = Group()
    aliens = Group()

    # Crear la flota de aliens
    fg.crear_flota(ai_config, pantalla, nave, aliens)

    # Bucle principal del juego
    while True:
        # Eventos
        fg.verificar_eventos(ai_config, pantalla, estadisticas, play_button, nave, aliens, balas)
        
        if estadisticas.game_active:
        # Actualizaciones
            nave.update()
            fg.update_balas(ai_config, pantalla, nave, balas, aliens, estadisticas)
            fg.update_aliens(ai_config, estadisticas, pantalla, nave, aliens, balas)

        # Dibujar
        fg.actualizar_pantalla(ai_config, pantalla, estadisticas, nave, aliens, balas, play_button)


if __name__ == "__main__":
    run_game()
