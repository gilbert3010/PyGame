import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # Representa a un solo alien en la pantalla
    def __init__(self, ai_configuraciones, pantalla):
        super().__init__()
        self.pantalla = pantalla
        self.ai_configuraciones = ai_configuraciones

        # Cargar la imagen del alien y establecer su rect
        self.image = pygame.image.load("img/nave_ovni.png")
        self.rect = self.image.get_rect()

        # Posición inicial cerca de la parte superior izquierda
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Posición exacta en x
        self.x = float(self.rect.x)

    def blitme(self):
        # Dibujar el alien en su posición actual
        self.pantalla.blit(self.image, self.rect)

    def check_edges(self):
        # Devuelve True si el alien está en el borde de la pantalla
        screen_rect = self.pantalla.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        # Mueve el alien horizontalmente
        self.x += (
            self.ai_configuraciones.factor_velocidad_alien
            * self.ai_configuraciones.fleet_direction
        )
        self.rect.x = self.x
