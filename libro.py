
from material import Material


class Libro(Material):

    def __init__(self, codigo, titulo, anio_publicacion, autor, genero):
        super().__init__(codigo, titulo, anio_publicacion)

        self.__autor = autor
        self.__genero = genero

    def get_autor(self):
        return self.__autor

    def get_genero(self):
        return self.__genero

    def set_autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    def set_genero(self, nuevo_genero):
        self.__genero = nuevo_genero

    def mostrar_informacion(self):
        informacion = super().mostrar_informacion()

        return (
            f"{informacion}\n"
            f"Autor: {self.__autor}\n"
            f"Genero: {self.__genero}"
        )
