from revista import Revista
from material import Material


def test_revista_completa():
    revista = Revista(
        "R001",
        "National Geographic",
        2020,
        125,
        "Mensual"
    )

    # Comprobar la herencia
    assert isinstance(revista, Material)

    # Comprobar los datos iniciales
    assert revista.get_codigo() == "R001"
    assert revista.get_titulo() == "National Geographic"
    assert revista.get_anio_publicacion() == 2020
    assert revista.get_numero_edicion() == 125
    assert revista.get_periodicidad() == "Mensual"
    assert revista.get_disponible() is True

    # Comprobar los setters
    revista.set_numero_edicion(130)
    revista.set_periodicidad("Semanal")
    revista.set_disponible(False)

    assert revista.get_numero_edicion() == 130
    assert revista.get_periodicidad() == "Semanal"
    assert revista.get_disponible() is False

    # Comprobar la información
    resultado = revista.mostrar_informacion()

    assert "Titulo: National Geographic" in resultado
    assert "Numero de edicion: 130" in resultado
    assert "Periodicidad: Semanal" in resultado
    assert "Estado: Prestado" in resultado