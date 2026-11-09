import pytest

from prestamo import Prestamo
from lector import Lector
from libro import Libro


def crear_prestamo():
    lector = Lector("LE001", "Lucia", "Perez", "1122334455")

    libro = Libro(
        "L001",
        "El Principito",
        1943,
        "Antoine de Saint-Exupery",
        "Novela"
    )

    libro.set_disponible(False)

    prestamo = Prestamo(
        "P001",
        lector,
        libro,
        "08/11/2026"
    )

    return prestamo, libro


def test_prestamo_completo():
    prestamo, libro = crear_prestamo()

    # Comprobar los datos iniciales
    assert prestamo.get_codigo() == "P001"
    assert prestamo.get_lector().get_nombre() == "Lucia"
    assert prestamo.get_material() == libro
    assert prestamo.get_fecha_prestamo() == "08/11/2026"
    assert prestamo.get_fecha_devolucion() is None
    assert prestamo.esta_activo() is True

    # Comprobar la información del préstamo
    resultado = prestamo.mostrar_informacion()

    assert "Lector: Lucia Perez" in resultado
    assert "Material: El Principito" in resultado
    assert "Estado: Prestado" in resultado

    # Registrar la devolución
    prestamo.registrar_devolucion("10/11/2026")

    assert prestamo.get_fecha_devolucion() == "10/11/2026"
    assert prestamo.esta_activo() is False
    assert libro.get_disponible() is True

    resultado = prestamo.mostrar_informacion()

    assert "Estado: Devuelto" in resultado
    assert "Fecha de devolucion: 10/11/2026" in resultado


def test_no_permite_devolver_dos_veces():
    prestamo, libro = crear_prestamo()

    prestamo.registrar_devolucion("10/11/2026")

    with pytest.raises(ValueError):
        prestamo.registrar_devolucion("11/11/2026")