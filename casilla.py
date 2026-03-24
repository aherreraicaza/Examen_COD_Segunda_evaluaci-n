class Casilla:
    """
    ESto representa una casilla del tablero de Hundir la Flota.
    Guarda si ha sido bombardeada y el resultado del disparo.
    """

    YA_DISPARADA = -1
    AGUA = 0
    TOCADO = 1
    HUNDIDO = 2

    def __init__(self, nave=None):
        """
        Inicializa la casilla.
        :param nave: objeto Nave si hay una nave en esta casilla, None si está vacía
        """
        self.nave = nave
        self.disparada = False
        self.estado = "VACIA"

    def recibir_disparo(self):
        """
        Procesa un disparo sobre esta casilla.
        :return: YA_DISPARADA(-1), AGUA(0), TOCADO(1) o HUNDIDO(2)
        """
        if self.disparada:
            return self.YA_DISPARADA

        self.disparada = True

        if self.nave is None:
            self.estado = "AGUA"
            return self.AGUA

            resultado = self.nave.recibir_disparo()

        if resultado == self.HUNDIDO:
            self.estado = "HUNDIDO"
        else:
            self.estado = "TOCADO"

        return resultado

    def actualizar_estado_hundido(self):
        """
        Actualiza el estado de la casilla a HUNDIDO.
        Se llama desde el Tablero cuando la nave de esta casilla
        ha sido completamente hundida, para que todas las casillas
        de esa nave muestren el estado correcto.
        """
        if self.nave is not None and self.nave.hundido:
            self.estado = "HUNDIDO"