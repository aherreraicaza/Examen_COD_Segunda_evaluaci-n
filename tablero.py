from nave import Nave
from casilla import Casilla


class Tablero:
    """
    Representa el tablero de juego de Hundir la Flota.
    Contiene el casillero (matriz de Casillas) con las naves colocadas.
    """

    YA_DISPARADA = -1
    AGUA = 0
    TOCADO = 1
    HUNDIDO = 2

    def __init__(self, tamanho=10):
        """
        Inicializa el tablero, crea las naves y las coloca en el casillero.
        :param tamanho: tamaño del tablero (tamanho x tamanho)
        """
        self.tamanho = tamanho

        # Crear las naves
        por1 = Nave("Destructor",        "portaaviones", 5)
        fra1 = Nave("Bismarck",          "fragata",      3)
        fra2 = Nave("Prince of Wales",   "fragata",      3)
        fra3 = Nave("Graf Spee",         "fragata",      3)
        sub1 = Nave("U-47",              "submarino",    1)
        sub2 = Nave("U-96",              "submarino",    1)
        sub3 = Nave("U-505",             "submarino",    1)
        sub4 = Nave("U-534",             "submarino",    1)

        self.casillero = [
            [Casilla() for _ in range(tamanho)]
            for _ in range(tamanho)
        ]

        self.casillero[1][1] = Casilla(nave=por1)
        self.casillero[1][2] = Casilla(nave=por1)
        self.casillero[1][3] = Casilla(nave=por1)
        self.casillero[1][4] = Casilla(nave=por1)
        self.casillero[1][5] = Casilla(nave=por1)

        self.casillero[3][3] = Casilla(nave=fra1)
        self.casillero[4][3] = Casilla(nave=fra1)
        self.casillero[5][3] = Casilla(nave=fra1)

        self.casillero[7][1] = Casilla(nave=fra2)
        self.casillero[7][2] = Casilla(nave=fra2)
        self.casillero[7][3] = Casilla(nave=fra2)

        self.casillero[9][1] = Casilla(nave=fra3)
        self.casillero[9][2] = Casilla(nave=fra3)
        self.casillero[9][3] = Casilla(nave=fra3)

        self.casillero[4][6] = Casilla(nave=sub1)
        self.casillero[9][9] = Casilla(nave=sub2)
        self.casillero[7][6] = Casilla(nave=sub3)
        self.casillero[9][5] = Casilla(nave=sub4)

    def comprobar_impacto(self, x, y):
        """
        Procesa un disparo en la posición (x, y) del tablero.
        Si la nave es hundida, actualiza el estado de TODAS sus casillas.
        :param x: fila del disparo
        :param y: columna del disparo
        :return: YA_DISPARADA(-1), AGUA(0), TOCADO(1) o HUNDIDO(2)
        """
        resultado = self.casillero[x][y].recibir_disparo()

        if resultado == self.HUNDIDO:
            nave_hundida = self.casillero[x][y].nave
            self._actualizar_casillas_hundidas(nave_hundida)

        return resultado

    def _actualizar_casillas_hundidas(self, nave):
        """
        Recorre todo el tablero y actualiza a HUNDIDO las casillas
        que pertenecen a la nave que acaba de ser hundida.
        :param nave: objeto Nave que ha sido hundido
        """
        for fila in self.casillero:
            for casilla in fila:
                if casilla.nave is nave:
                    casilla.actualizar_estado_hundido()