import pygame


class Estadisticas:
    """Clase que sigue las estadísticas del juego."""

    def __init__(self, ai_config):
        """Inicializa las estadísticas del juego."""
        self.ai_config = ai_config
        self.reset_stats()
        # Iniciar el juego en estado inactivo
        self.game_active = False

    def reset_stats(self):
        """Establece las estadísticas que cambian durante el juego."""
        self.naves_restantes = self.ai_config.cantidad_naves
