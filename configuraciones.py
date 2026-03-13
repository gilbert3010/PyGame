class Configuraciones:
    # Clase para almacenar todas las configuraciones de Alien Invasion
    def __init__(self):
        # Pantalla
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Nave
        self.factor_velocidad_nave = 1.5
        self.cantidad_naves = 3

        # Balas
        self.bala_factor_velocidad = 1
        self.bala_width = 3
        self.bala_height = 15
        self.bala_color = (60, 60, 60)
        self.balas_permitidas = 3

        # Aliens
        self.factor_velocidad_alien = 1
        self.fleet_drop_speed = 10
        # 1 a la derecha; -1 a la izquierda
        self.fleet_direction = 1
