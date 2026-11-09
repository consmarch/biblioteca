from libro import Libro
from material import Material


def test_libro_completo():
    libro = Libro(
        "L001",
        "El Principito",
        1943,
        "Antoine de Saint-Exupery",
        "Novela"
    )

    # Comprobar la herencia
    assert isinstance(libro, Material)

    # Comprobar los datos iniciales
    assert libro.get_codigo() == "L001"
    assert libro.get_titulo() == "El Principito"
    assert libro.get_anio_publicacion() == 1943
    assert libro.get_autor() == "Antoine de Saint-Exupery"
    assert libro.get_genero() == "Novela"
    assert libro.get_disponible() is True

    # Comprobar los setters
    libro.set_autor("Roald Dahl")
    libro.set_genero("Infantil")
    libro.set_disponible(False)

    assert libro.get_autor() == "Roald Dahl"
    assert libro.get_genero() == "Infantil"
    assert libro.get_disponible() is False

    # Comprobar la información
    resultado = libro.mostrar_informacion()

    assert "Titulo: El Principito" in resultado
    assert "Autor: Roald Dahl" in resultado
    assert "Genero: Infantil" in resultado
    assert "Estado: Prestado" in resultado