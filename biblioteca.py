
from material import Material
from lector import Lector
from prestamo import Prestamo


class Biblioteca:

    def __init__(self):
        self.__materiales = []
        self.__lectores = []
        self.__prestamos = []

    # Agregar un material a la biblioteca

    def agregar_material(self, material):
        if not isinstance(material, Material):
            raise TypeError("El objeto debe ser un material.")

        for existente in self.__materiales:
            if existente.get_codigo() == material.get_codigo():
                raise ValueError("Ya existe un material con ese codigo.")

        self.__materiales.append(material)
        return material

    # Registrar un lector

    def agregar_lector(self, lector):
        if not isinstance(lector, Lector):
            raise TypeError("El objeto debe ser un lector.")

        for existente in self.__lectores:
            if existente.get_codigo() == lector.get_codigo():
                raise ValueError("Ya existe un lector con ese codigo.")

        self.__lectores.append(lector)
        return lector

    # Buscar un material por su codigo

    def buscar_material(self, codigo):
        for material in self.__materiales:
            if material.get_codigo() == codigo:
                return material

        raise ValueError("No se encontro el material.")

    # Buscar un lector por su codigo

    def buscar_lector(self, codigo):
        for lector in self.__lectores:
            if lector.get_codigo() == codigo:
                return lector

        raise ValueError("No se encontro el lector.")

    # Realizar un prestamo

    def realizar_prestamo(self, codigo_prestamo, codigo_lector,
                          codigo_material, fecha_prestamo):

        for prestamo in self.__prestamos:
            if prestamo.get_codigo() == codigo_prestamo:
                raise ValueError("Ya existe un prestamo con ese codigo.")

        lector = self.buscar_lector(codigo_lector)
        material = self.buscar_material(codigo_material)

        if not material.get_disponible():
            raise ValueError("El material no esta disponible.")

        nuevo_prestamo = Prestamo(
            codigo_prestamo,
            lector,
            material,
            fecha_prestamo
        )

        material.set_disponible(False)
        self.__prestamos.append(nuevo_prestamo)

        return nuevo_prestamo

    # Registrar una devolucion

    def registrar_devolucion(self, codigo_prestamo, fecha_devolucion):
        for prestamo in self.__prestamos:
            if prestamo.get_codigo() == codigo_prestamo:
                prestamo.registrar_devolucion(fecha_devolucion)
                return prestamo

        raise ValueError("No se encontro el prestamo.")

    # Getters de las listas

    def get_materiales(self):
        return list(self.__materiales)

    def get_lectores(self):
        return list(self.__lectores)

    def get_prestamos(self):
        return list(self.__prestamos)
