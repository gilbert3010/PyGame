import sys
import pygame
from pygame.sprite import Group
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
    nave = Nave(ai_config, pantalla)
    #crea un grupo para almacenar las balas
    balas = Group()
    
    
    # Iniciar el bucle principal del juego
    while True:
        # Observar eventos de teclado y de ratón
        fg.verificar_eventos(ai_config, pantalla, nave, balas)
        nave.update()
        balas.update()
        #Deshace las balas que han desaparecido
        for bala in balas.copy():
            if bala.rect.bottom <= 0:
                balas.remove(bala)
                
        fg.actualizar_pantalla(ai_config, pantalla, nave, balas)
        
        
run_game()
