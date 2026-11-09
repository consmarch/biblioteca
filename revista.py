
from material import Material


class Revista(Material):

    def __init__(self, codigo, titulo, anio_publicacion, numero_edicion, periodicidad):
        super().__init__(codigo, titulo, anio_publicacion)

        self.__numero_edicion = numero_edicion
        self.__periodicidad = periodicidad

    def get_numero_edicion(self):
        return self.__numero_edicion

    def get_periodicidad(self):
        return self.__periodicidad

    def set_numero_edicion(self, nuevo_numero):
        self.__numero_edicion = nuevo_numero

    def set_periodicidad(self, nueva_periodicidad):
        self.__periodicidad = nueva_periodicidad

    def mostrar_informacion(self):
        informacion = super().mostrar_informacion()

        return (
            f"{informacion}\n"
            f"Numero de edicion: {self.__numero_edicion}\n"
            f"Periodicidad: {self.__periodicidad}"
        )
