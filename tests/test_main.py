import pytest
import main as app

from biblioteca import Biblioteca
from libro import Libro
from lector import Lector


def test_registros_y_mostrar_materiales_lectores(monkeypatch, capsys):
    biblioteca = Biblioteca()

    # Comprobar los mensajes cuando no hay datos
    app.mostrar_materiales(biblioteca)
    app.mostrar_lectores(biblioteca)

    # Simular los datos que ingresaría el usuario
    datos = iter([
        "101", "El Principito", "1943",
        "Antoine de Saint-Exupery", "Novela",

        "202", "National Geographic", "2020",
        "125", "Mensual",

        "301", "Lucia", "Perez", "1122334455"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda mensaje="": next(datos)
    )

    # Registrar los datos
    app.registrar_libro(biblioteca)
    app.registrar_revista(biblioteca)
    app.registrar_lector(biblioteca)

    # Mostrar los datos registrados
    app.mostrar_materiales(biblioteca)
    app.mostrar_lectores(biblioteca)

    assert len(biblioteca.get_materiales()) == 2
    assert len(biblioteca.get_lectores()) == 1

    resultado = capsys.readouterr().out

    assert "Libro registrado correctamente." in resultado
    assert "Revista registrada correctamente." in resultado
    assert "Lector registrado correctamente." in resultado
    assert "El Principito" in resultado
    assert "Lucia" in resultado
    assert "No hay materiales registrados." in resultado
    assert "No hay lectores registrados." in resultado


def test_prestamos_devoluciones_y_mostrar_historial(monkeypatch, capsys):
    biblioteca = Biblioteca()

    libro = Libro(
        101, "El Principito", 1943,
        "Antoine de Saint-Exupery", "Novela"
    )

    lector = Lector(301, "Lucia", "Perez", "1122334455")

    biblioteca.agregar_material(libro)
    biblioteca.agregar_lector(lector)

    # Comprobar el historial vacío
    app.mostrar_prestamos(biblioteca)

    # Realizar un préstamo
    datos_prestamo = iter(["501", "301", "101", "08/11/2026"])

    monkeypatch.setattr(
        "builtins.input",
        lambda mensaje="": next(datos_prestamo)
    )

    app.realizar_prestamo(biblioteca)

    assert libro.get_disponible() is False

    # Registrar una devolución
    datos_devolucion = iter(["501", "10/11/2026"])

    monkeypatch.setattr(
        "builtins.input",
        lambda mensaje="": next(datos_devolucion)
    )

    app.registrar_devolucion(biblioteca)

    assert libro.get_disponible() is True

    # Mostrar el historial
    app.mostrar_prestamos(biblioteca)

    resultado = capsys.readouterr().out

    assert "No hay prestamos registrados." in resultado
    assert "Prestamo realizado correctamente." in resultado
    assert "Devolucion registrada correctamente." in resultado
    assert "Estado: Devuelto" in resultado


def test_generar_pdf(monkeypatch, tmp_path):
    biblioteca = Biblioteca()

    libro = Libro(
        101, "El Principito", 1943,
        "Antoine de Saint-Exupery", "Novela"
    )

    lector = Lector(301, "Lucia", "Perez", "1122334455")

    biblioteca.agregar_material(libro)
    biblioteca.agregar_lector(lector)

    biblioteca.realizar_prestamo(
        501, 301, 101, "08/11/2026"
    )

    # Comprobar el error cuando falta la fuente Arial
    with monkeypatch.context() as m:
        m.setattr(app.os.path, "exists", lambda ruta: False)

        with pytest.raises(FileNotFoundError):
            app.generar_pdf(biblioteca)

    # Generar el PDF en una carpeta temporal
    monkeypatch.chdir(tmp_path)

    app.generar_pdf(biblioteca)

    archivo = tmp_path / "informe_biblioteca.pdf"

    assert archivo.exists()
    assert archivo.stat().st_size > 0


def test_menu_y_funcion_main(monkeypatch, capsys):
    # Mostrar el menú
    app.mostrar_menu()

    # Simular una opción incorrecta, un error de ingreso y la salida
    datos = iter(["99", "1", "abc", "0"])

    monkeypatch.setattr(
        "builtins.input",
        lambda mensaje="": next(datos)
    )

    app.main()

    resultado = capsys.readouterr().out

    assert "SISTEMA DE BIBLIOTECA" in resultado
    assert "Opcion incorrecta." in resultado
    assert "Error:" in resultado
    assert "Gracias por utilizar la biblioteca." in resultado