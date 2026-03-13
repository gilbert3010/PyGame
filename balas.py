import pygame
from pygame.sprite import Sprite


class Bala(Sprite):
    # Sirve para manejar las balas disparadas por la nave
    def __init__(self, ai_configuraciones, pantalla, nave):
        super().__init__()
        self.pantalla = pantalla
        
        # Crear un rectángulo para la bala en (0, 0) y luego establecer la posición correcta
        self.rect = pygame.Rect(
            0, 0,
            ai_configuraciones.bala_width,
            ai_configuraciones.bala_height
        )
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top
        
        # Almacena la posición de la bala como un valor decimal
        self.y = float(self.rect.y)
        
        self.color = ai_configuraciones.bala_color
        self.factor_velocidad = ai_configuraciones.bala_factor_velocidad

    def update(self):
        # Mover la bala hacia arriba en la pantalla
        self.y -= self.factor_velocidad
        self.rect.y = self.y

    def draw(self):
        # Dibujar la bala en la pantalla
        pygame.draw.rect(self.pantalla, self.color, self.rect)
