import pygame.font
from pygame.sprite import Group
from nave import Nave

class Marcador():
    #una clase para mostrar información sobre el puntaje
    def __init__(self, ai_config, pantalla, estadisticas):
        self.pantalla = pantalla
        self.pantalla_rect = pantalla.get_rect()
        self.ai_config = ai_config
        self.estadisticas = estadisticas

        # Configuración de fuente para el marcador
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Preparar la imagen del puntaje inicial
        self.prep_puntaje()
        self.prep_puntaje_alto()
        self.prep_nivel()
        self.prep_nave()
        
    def prep_puntaje(self):
        """Convierte el puntaje en una imagen renderizada."""
        puntaje_redondeado = int(round(self.estadisticas.puntaje, -1))
        puntaje_str = "{:,}".format(puntaje_redondeado)
        self.puntaje_image = self.font.render(puntaje_str, True, self.text_color, self.ai_config.bg_color)

        # Mostrar el puntaje en la esquina superior derecha de la pantalla
        self.puntaje_rect = self.puntaje_image.get_rect()
        self.puntaje_rect.right = self.pantalla_rect.right - 20
        self.puntaje_rect.top = 20
        
    def prep_puntaje_alto(self):
        """Convierte el puntaje en una imagen renderizada."""
        puntaje_alto = int(round(self.estadisticas.puntaje_alto, -1))
        puntaje_alto_str = "{:,}".format(puntaje_alto)
        self.puntaje_alto_image = self.font.render(puntaje_alto_str, True, self.text_color, self.ai_config.bg_color)

        # Mostrar el puntaje alto en el centro de la pantalla
        self.puntaje_alto_rect = self.puntaje_alto_image.get_rect()
        self.puntaje_alto_rect.centerx = self.pantalla_rect.centerx
        self.puntaje_alto_rect.top = self.puntaje_rect.top
        
    def prep_nivel(self):
        """Convierte el nivel en una imagen renderizada."""
        nivel_str = str(self.estadisticas.nivel)
        self.nivel_image = self.font.render(nivel_str, True, self.text_color, self.ai_config.bg_color)

        # Mostrar el nivel debajo del puntaje
        self.nivel_rect = self.nivel_image.get_rect()
        self.nivel_rect.right = self.puntaje_rect.right - 20
        self.nivel_rect.top = self.puntaje_rect.bottom + 10
        
    def prep_nave(self):
        """Muestra cuántas naves quedan."""
        self.naves = Group()
        for nave_num in range(self.estadisticas.naves_restantes):
            nave = Nave(self.ai_config, self.pantalla)
            nave.rect.x = 10 + nave_num * nave.rect.width
            nave.rect.y = 10
            self.naves.add(nave)
        
    def muestra_puntaje(self):
        """Dibuja el puntaje en la pantalla."""
        self.pantalla.blit(self.puntaje_image, self.puntaje_rect)
        self.pantalla.blit(self.puntaje_alto_image, self.puntaje_alto_rect)
        self.pantalla.blit(self.nivel_image, self.nivel_rect)
        # Dibuja las naves restantes
        self.naves.draw(self.pantalla)