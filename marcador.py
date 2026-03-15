import pygame.font

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
        
    def prep_puntaje(self):
        """Convierte el puntaje en una imagen renderizada."""
        puntaje_str = "{:,}".format(self.estadisticas.puntaje)
        self.puntaje_image = self.font.render(puntaje_str, True, self.text_color, self.ai_config.bg_color)

        # Mostrar el puntaje en la esquina superior derecha de la pantalla
        self.puntaje_rect = self.puntaje_image.get_rect()
        self.puntaje_rect.right = self.pantalla_rect.right - 20
        self.puntaje_rect.top = 20
        
    def muestra_puntaje(self):
        """Dibuja el puntaje en la pantalla."""
        self.pantalla.blit(self.puntaje_image, self.puntaje_rect)