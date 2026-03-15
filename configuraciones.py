class Configuraciones:
    # Clase para almacenar todas las configuraciones de Alien Invasion
    def __init__(self):
        # Pantalla
        self.screen_width = 990
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Nave
        self.cantidad_naves = 3

        # Balas
        self.bala_width = 3
        self.bala_height = 15
        self.bala_color = (60, 60, 60)
        self.balas_permitidas = 3

        # Aliens
        self.fleet_drop_speed = 10
        # que tan rapido se incrementa la velocidad del juego
        self.escala_aceleracion = 1.1
        
        self.inicializa_configuraciones_dinamicas()
    
    def inicializa_configuraciones_dinamicas(self):
        # Configuraciones que cambian a lo largo del juego
        self.factor_velocidad_nave = 1.5
        self.bala_factor_velocidad = 3
        self.factor_velocidad_alien = 1
        # 1 a la derecha; -1 a la izquierda
        self.fleet_direction = 1
        #puntaje
        self.puntos_alien = 50
    
    def aumentar_velocidad(self):
        # Aumenta las configuraciones de velocidad
        self.factor_velocidad_nave *= self.escala_aceleracion
        self.bala_factor_velocidad *= self.escala_aceleracion
        self.factor_velocidad_alien *= self.escala_aceleracion