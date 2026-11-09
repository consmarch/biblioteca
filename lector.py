
class Lector:

    def __init__(self, codigo, nombre, apellido, telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono

    # Getters

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_telefono(self):
        return self.__telefono

    # Setters

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_apellido(self, nuevo_apellido):
        self.__apellido = nuevo_apellido

    def set_telefono(self, nuevo_telefono):
        self.__telefono = nuevo_telefono

    # Mostrar informacion del lector

    def mostrar_informacion(self):
        return (
            f"Codigo: {self.__codigo}\n"
            f"Nombre: {self.__nombre}\n"
            f"Apellido: {self.__apellido}\n"
            f"Telefono: {self.__telefono}"
        )
