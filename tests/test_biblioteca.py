import pytest

from biblioteca import Biblioteca
from material import Material
from libro import Libro
from lector import Lector


def crear_biblioteca_con_datos():
    biblioteca = Biblioteca()

    libro = Libro(
        "L001",
        "El Principito",
        1943,
        "Antoine de Saint-Exupery",
        "Novela"
    )

    lector = Lector(
        "LE001",
        "Lucia",
        "Perez",
        "1122334455"
    )

    biblioteca.agregar_material(libro)
    biblioteca.agregar_lector(lector)

    return biblioteca, libro, lector


def test_biblioteca_comienza_vacia_y_agrega_datos():
    biblioteca = Biblioteca()

    assert biblioteca.get_materiales() == []
    assert biblioteca.get_lectores() == []
    assert biblioteca.get_prestamos() == []

    libro = Material("M001", "Diccionario", 2020)
    lector = Lector("LE001", "Lucia", "Perez", "1122334455")

    assert biblioteca.agregar_material(libro) == libro
    assert biblioteca.agregar_lector(lector) == lector

    assert len(biblioteca.get_materiales()) == 1
    assert len(biblioteca.get_lectores()) == 1

    # Comprobar que los getters devuelven copias
    materiales = biblioteca.get_materiales()
    lectores = biblioteca.get_lectores()

    materiales.clear()
    lectores.clear()

    assert len(biblioteca.get_materiales()) == 1
    assert len(biblioteca.get_lectores()) == 1


def test_validaciones_al_agregar():
    biblioteca = Biblioteca()

    # No permite agregar objetos de tipos incorrectos
    with pytest.raises(TypeError):
        biblioteca.agregar_material("No es un material")

    with pytest.raises(TypeError):
        biblioteca.agregar_lector("No es un lector")

    biblioteca.agregar_material(
        Material("M001", "Diccionario", 2020)
    )

    biblioteca.agregar_lector(
        Lector("LE001", "Lucia", "Perez", "1122334455")
    )

    # No permite códigos repetidos
    with pytest.raises(ValueError):
        biblioteca.agregar_material(
            Material("M001", "Otro libro", 2022)
        )

    with pytest.raises(ValueError):
        biblioteca.agregar_lector(
            Lector("LE001", "Maria", "Gomez", "1199887766")
        )


def test_buscar_material_y_lector():
    biblioteca, libro, lector = crear_biblioteca_con_datos()

    assert biblioteca.buscar_material("L001") == libro
    assert biblioteca.buscar_lector("LE001") == lector

    # Comprobar búsquedas inexistentes
    with pytest.raises(ValueError):
        biblioteca.buscar_material("NOEXISTE")

    with pytest.raises(ValueError):
        biblioteca.buscar_lector("NOEXISTE")


def test_realizar_prestamo_y_validaciones():
    biblioteca, libro, lector = crear_biblioteca_con_datos()

    prestamo = biblioteca.realizar_prestamo(
        "P001",
        "LE001",
        "L001",
        "08/11/2026"
    )

    assert prestamo.get_codigo() == "P001"
    assert prestamo.get_lector() == lector
    assert prestamo.get_material() == libro
    assert libro.get_disponible() is False
    assert len(biblioteca.get_prestamos()) == 1

    # Agregar otro libro para comprobar el código repetido
    otro_libro = Libro(
        "L002",
        "Matilda",
        1988,
        "Roald Dahl",
        "Infantil"
    )

    biblioteca.agregar_material(otro_libro)

    with pytest.raises(ValueError):
        biblioteca.realizar_prestamo(
            "P001",
            "LE001",
            "L002",
            "09/11/2026"
        )

    # No permite prestar nuevamente el mismo material
    with pytest.raises(ValueError):
        biblioteca.realizar_prestamo(
            "P002",
            "LE001",
            "L001",
            "09/11/2026"
        )


def test_registrar_devolucion_y_validaciones():
    biblioteca, libro, lector = crear_biblioteca_con_datos()

    biblioteca.realizar_prestamo(
        "P001",
        "LE001",
        "L001",
        "08/11/2026"
    )

    prestamo = biblioteca.registrar_devolucion(
        "P001",
        "10/11/2026"
    )

    assert prestamo.get_fecha_devolucion() == "10/11/2026"
    assert prestamo.esta_activo() is False
    assert libro.get_disponible() is True

    # No permite devolver dos veces
    with pytest.raises(ValueError):
        biblioteca.registrar_devolucion(
            "P001",
            "11/11/2026"
        )

    # No permite devolver un préstamo inexistente
    with pytest.raises(ValueError):
        biblioteca.registrar_devolucion(
            "P999",
            "11/11/2026"
        )

    # Comprobar que el getter de préstamos devuelve una copia
    prestamos = biblioteca.get_prestamos()
    prestamos.clear()

    assert len(biblioteca.get_prestamos()) == 1