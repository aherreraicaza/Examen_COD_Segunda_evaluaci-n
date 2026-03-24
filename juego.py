from tablero import Tablero


class Juego:
    """
    Clase principal que gestiona una partida de Hundir la Flota.
    Coordina los ataques y muestra los resultados por pantalla.
    """

    YA_DISPARADA = -1
    AGUA = 0
    TOCADO = 1
    HUNDIDO = 2

    def __init__(self):
        """
        Inicializa el juego creando el tablero y lanza ataques de prueba.
        """
        self.tablero = Tablero()

        self.lanzar_ataque(1, 1)
        self.lanzar_ataque(1, 2)
        self.lanzar_ataque(1, 3)
        self.lanzar_ataque(1, 4)
        self.lanzar_ataque(1, 5)

        self.lanzar_ataque(1, 1)

        self.lanzar_ataque(0, 0)

    def lanzar_ataque(self, x, y):
        """
        Lanza un ataque a la posición (x, y) y muestra el resultado.
        :param x: fila del ataque
        :param y: columna del ataque
        """
        print(f"Ataque a ({x}, {y})")
        resultado = self.tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)

    def mostrar_resultado(self, resultado):
        """
        Imprime por pantalla el resultado de un disparo.
        :param resultado: valor entero devuelto por comprobar_impacto
        """
        if resultado == self.YA_DISPARADA:
            print("Ya disparada")
        elif resultado == self.AGUA:
            print("Agua")
        elif resultado == self.TOCADO:
            print("Tocado")
        elif resultado == self.HUNDIDO:
            print("Hundido")


if __name__ == "__main__":
    Juego()