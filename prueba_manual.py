
from biblioteca import Biblioteca
from libro import Libro
from revista import Revista
from lector import Lector


# Crear la biblioteca
biblioteca = Biblioteca()

# Crear libros y revistas
libro1 = Libro(
    1, "El Principito", 1943,
    "Antoine de Saint-Exupery", "Novela"
)

revista1 = Revista(
    2, "National Geographic", 2025,
    125, "Mensual"
)

# Crear un lector
lector1 = Lector(
    1, "Lucia", "Perez", "2994000000"
)

# Agregar los elementos a la biblioteca
biblioteca.agregar_material(libro1)
biblioteca.agregar_material(revista1)
biblioteca.agregar_lector(lector1)


# Mostrar los materiales
print("===== MATERIALES DE LA BIBLIOTECA =====")

for material in biblioteca.get_materiales():
    print(material.mostrar_informacion())
    print("-----------------------------")


# Realizar un prestamo
print("\n===== REALIZAR PRESTAMO =====")

prestamo = biblioteca.realizar_prestamo(
    1, 1, 1, "08/11/2026"
)

print(prestamo.mostrar_informacion())

print("\n¿El libro esta disponible?")
print(libro1.get_disponible())


# Registrar la devolucion
print("\n===== REGISTRAR DEVOLUCION =====")

biblioteca.registrar_devolucion(
    1, "10/11/2026"
)

print(prestamo.mostrar_informacion())

print("\n¿El libro esta disponible?")
print(libro1.get_disponible())
