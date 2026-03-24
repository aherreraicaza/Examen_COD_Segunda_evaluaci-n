class Nave:
    """
    Representa una nave del juego Hundir la Flota.
    Gestiona la vida y el estado de hundimiento.
    """

    TOCADO = 1
    HUNDIDO = 2

    def __init__(self, nombre, tipo, vida):
        """
        Inicializa la nave.
        :param nombre: nombre de la nave (ej. "Bismarck")
        :param tipo: tipo de nave (ej. "fragata")
        :param vida: número de casillas que ocupa / puntos de vida
        """
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.hundido = False

    def recibir_disparo(self):
        """
        Reduce la vida de la nave en 1.
        Si la vida llega a 0, marca la nave como hundida.
        :return: TOCADO(1) si sigue a flote, HUNDIDO(2) si se hunde
        """
        self.vida -= 1

        if self.vida <= 0:
            self.hundido = True
            print(f"{self.nombre} hundido")
            return self.HUNDIDO
        else:
            print(f"{self.nombre} tocado. Vida restante: {self.vida}")
            return self.TOCADO