from lector import Lector


def test_lector_completo():
    lector = Lector("LE001", "Lucia", "Perez", "1122334455")

    # Comprobar los datos iniciales
    assert lector.get_codigo() == "LE001"
    assert lector.get_nombre() == "Lucia"
    assert lector.get_apellido() == "Perez"
    assert lector.get_telefono() == "1122334455"

    # Comprobar los setters
    lector.set_nombre("Maria")
    lector.set_apellido("Gomez")
    lector.set_telefono("1199887766")

    assert lector.get_nombre() == "Maria"
    assert lector.get_apellido() == "Gomez"
    assert lector.get_telefono() == "1199887766"

    # Comprobar la información
    resultado = lector.mostrar_informacion()

    assert "Codigo: LE001" in resultado
    assert "Nombre: Maria" in resultado
    assert "Apellido: Gomez" in resultado
    assert "Telefono: 1199887766" in resultado