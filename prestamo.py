
class Prestamo:

    def __init__(self, codigo, lector, material, fecha_prestamo):
        self.__codigo = codigo
        self.__lector = lector
        self.__material = material
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = None

    # Getters

    def get_codigo(self):
        return self.__codigo

    def get_lector(self):
        return self.__lector

    def get_material(self):
        return self.__material

    def get_fecha_prestamo(self):
        return self.__fecha_prestamo

    def get_fecha_devolucion(self):
        return self.__fecha_devolucion

    # Comprobar si el prestamo sigue activo

    def esta_activo(self):
        return self.__fecha_devolucion is None

    # Registrar la devolucion

    def registrar_devolucion(self, fecha_devolucion):
        if not self.esta_activo():
            raise ValueError("Este material ya fue devuelto.")

        self.__fecha_devolucion = fecha_devolucion
        self.__material.set_disponible(True)

    # Mostrar informacion

    def mostrar_informacion(self):
        estado = "Prestado" if self.esta_activo() else "Devuelto"

        fecha_devolucion = (
            self.__fecha_devolucion
            if self.__fecha_devolucion is not None
            else "Pendiente"
        )

        return (
            f"Codigo de prestamo: {self.__codigo}\n"
            f"Lector: {self.__lector.get_nombre()} "
            f"{self.__lector.get_apellido()}\n"
            f"Material: {self.__material.get_titulo()}\n"
            f"Fecha de prestamo: {self.__fecha_prestamo}\n"
            f"Fecha de devolucion: {fecha_devolucion}\n"
            f"Estado: {estado}"
        )
