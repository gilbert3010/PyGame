import sys
import pygame
from configuraciones import Configuraciones
from nave import Nave
import funcionesGame as fg

def run_game():
    # Inicializar el juego y crear un objeto para almacenar la configuración
    pygame.init()
    ai_config = Configuraciones()
    pantalla = pygame.display.set_mode((ai_config.screen_width, ai_config.screen_height))
    pygame.display.set_caption("invasion alienigena")
    
    # Crear una nave
    nave = Nave(pantalla)
    
    
    # Iniciar el bucle principal del juego
    while True:
        # Observar eventos de teclado y de ratón
        fg.verificar_eventos(nave)
        nave.update()
        fg.actualizar_pantalla(ai_config, pantalla, nave)
        
        
run_game()