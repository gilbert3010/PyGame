import os
import pygame

class Nave(pygame.sprite.Sprite):
    def __init__(self, ai_configuraciones, pantalla):
        super().__init__()  # Agrega esta línea
        self.pantalla = pantalla
        self.ai_configuraciones = ai_configuraciones

        # Cargar la imagen de la nave y obtener su rectángulo
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "img", "nave_espacial.png")
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.pantalla_rect = pantalla.get_rect()

        # Iniciar cada nueva nave en la parte inferior central de la pantalla
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom

        # Almacena un valor decimal en el centro de la nave
        self.center = float(self.rect.centerx)

        # Banda de movimiento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Actualizar la posición de la nave según la bandera de movimiento
        if self.moving_right and self.rect.right < self.pantalla_rect.right:
            self.center += self.ai_configuraciones.factor_velocidad_nave
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_configuraciones.factor_velocidad_nave

        # Actualizar el rectángulo de la nave según self.center
        self.rect.centerx = int(self.center)

    def blitme(self):
        # Dibujar la nave en su ubicación actual
        self.pantalla.blit(self.image, self.rect)

    def centrar_nave(self):
        # Centra la nave en la pantalla
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom
        self.center = float(self.rect.centerx)