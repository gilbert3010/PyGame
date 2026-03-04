import pygame

class Nave():
    def __init__(self, ai_configuraciones, pantalla):
        
        self.pantalla = pantalla
        self.ai_configuraciones = ai_configuraciones
        
        # Cargar la imagen de la nave y obtener su rectángulo
        self.imagen = pygame.image.load("img/nave_espacial.png")
        self.rect = self.imagen.get_rect()
        self.pantalla_rect = pantalla.get_rect()
        
        # Iniciar cada nueva nave en la parte inferior central de la pantalla
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom
        
        #almacena un valor decimal en el centro de la nave
        self.center = float(self.rect.centerx)
        
        #bandera de movimiento
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        # Actualizar la posición de la nave según la bandera de movimiento
        if self.moving_right and self.rect.right < self.pantalla_rect.right:
            self.center += self.ai_configuraciones.factor_velocidad_nave
            
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_configuraciones.factor_velocidad_nave
            
        # Actualizar el rectángulo de la nave según self.center
        self.rect.centerx = self.center    
        
    def blitme(self):
        # Dibujar la nave en su ubicación actual
        self.pantalla.blit(self.imagen, self.rect)