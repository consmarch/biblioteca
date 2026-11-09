from material import Material


def test_material_completo():
    material = Material("M001", "El Principito", 1943)

    # Comprobar los datos iniciales
    assert material.get_codigo() == "M001"
    assert material.get_titulo() == "El Principito"
    assert material.get_anio_publicacion() == 1943
    assert material.get_disponible() is True

    # Comprobar los setters
    material.set_codigo("M002")
    material.set_titulo("Matilda")
    material.set_anio_publicacion(1988)
    material.set_disponible(False)

    assert material.get_codigo() == "M002"
    assert material.get_titulo() == "Matilda"
    assert material.get_anio_publicacion() == 1988
    assert material.get_disponible() is False

    # Comprobar la información
    resultado = material.mostrar_informacion()

    assert "Codigo: M002" in resultado
    assert "Titulo: Matilda" in resultado
    assert "Estado: Prestado" in resultado