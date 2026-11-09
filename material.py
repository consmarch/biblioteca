
class Material:
    def __init__(self, codigo, titulo, anio_publicacion):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__anio_publicacion = anio_publicacion
        self.__disponible = True

    # Getters: permiten consultar los atributos

    def get_codigo(self):
        return self.__codigo

    def get_titulo(self):
        return self.__titulo

    def get_anio_publicacion(self):
        return self.__anio_publicacion

    def get_disponible(self):
        return self.__disponible

    # Setters: permiten modificar los atributos

    def set_codigo(self, nuevo_codigo):
        self.__codigo = nuevo_codigo

    def set_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    def set_anio_publicacion(self, nuevo_anio):
        self.__anio_publicacion = nuevo_anio

    def set_disponible(self, estado):
        self.__disponible = estado

    # Muestra la información del material

    def mostrar_informacion(self):
        estado = "Disponible" if self.__disponible else "Prestado"

        return (
            f"Codigo: {self.__codigo}\n"
            f"Titulo: {self.__titulo}\n"
            f"Anio de publicacion: {self.__anio_publicacion}\n"
            f"Estado: {estado}"
        )
