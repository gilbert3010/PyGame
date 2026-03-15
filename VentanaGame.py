import sys
import pygame
from pygame.sprite import Group

from configuraciones import Configuraciones
from estadisticas import Estadisticas
from marcador import Marcador
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

    # Crea una instancia para almacenar estadísticas del juego y crea un marcador
    estadisticas = Estadisticas(ai_config)
    marcador = Marcador(ai_config, pantalla, estadisticas)

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
        fg.verificar_eventos(ai_config, pantalla, estadisticas, marcador, play_button, nave, aliens, balas)
        
        if estadisticas.game_active:
        # Actualizaciones
            nave.update()
            fg.update_balas(ai_config, pantalla, estadisticas, marcador, nave, balas, aliens)
            fg.update_aliens(ai_config, estadisticas, pantalla, marcador, nave, aliens, balas)

        # Dibujar
        fg.actualizar_pantalla(ai_config, pantalla, estadisticas, marcador, nave, aliens, balas, play_button)


if __name__ == "__main__":
    run_game()
