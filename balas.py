import sys
import pygame
from pygame.sprite import Sprite


class Bala(Sprite):
    #sirve para manejar las balas disparadas por la nave
    def __init__(self, ai_configuraciones, pantalla, nave):
        super(Bala, self).__init__()
        self.pantalla = pantalla
        
        # Crear un rectángulo para la bala en (0, 0) y luego establecer la posición correcta
        self.rect = pygame.Rect(0, 0, ai_configuraciones.bala_width, ai_configuraciones.bala_height)
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top
        
        #almacena la posicion de la bala como una valor decimal
        self.y = float(self.rect.y)
        
        self.color = ai_configuraciones.bala_color
        self.factor_velocidad = ai_configuraciones.bala_factor_velocidad


    def update(self):
        #mover la bala hacia arriba en la pantalla
        #actualizar la posicion decimal de la bala
        self.y -= self.factor_velocidad
        #actualizar la posicion del rectangulo
        self.rect.y = self.y
    
    def draw_bala(self):
        #dibujar la bala en la pantalla
        pygame.draw.rect(self.pantalla, self.color, self.rect)
