import pygame

class Nave():
    def __init__(self, pantalla):
        
        self.pantalla = pantalla
        
        # Cargar la imagen de la nave y obtener su rectángulo
        self.imagen = pygame.image.load("img/nave_espacial.png")
        self.rect = self.imagen.get_rect()
        self.pantalla_rect = pantalla.get_rect()
        
        # Iniciar cada nueva nave en la parte inferior central de la pantalla
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom
        
        #bandera de movimiento
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        # Actualizar la posición de la nave según la bandera de movimiento
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1    
        
    def blitme(self):
        # Dibujar la nave en su ubicación actual
        self.pantalla.blit(self.imagen, self.rect)