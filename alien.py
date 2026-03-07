import pygame
from pygame.sprite import Sprite



class Alien(Sprite):
    #Sirve para representar a un solo alien en la pantalla
    def __init__(self, ai_configuraciones, pantalla):
        #inicializar el alien y establecer su posición inicial
        super(Alien, self).__init__()
        self.pantalla = pantalla
        self.ai_configuraciones = ai_configuraciones
        
        # Cargar la imagen del alien y establecer su atributo rect
        self.image = pygame.image.load("img/nave_ovni.png")
        self.rect = self.image.get_rect()
        
        #iniciar cada nuevo alien cerca de la parte superior izquierda de la pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #almacena la posición exacta del alien
        self.x = float(self.rect.x)
        
    def blitme(self):
        #dibujar el alien en su posición actual
        self.pantalla.blit(self.image, self.rect)
