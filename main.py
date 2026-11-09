
from biblioteca import Biblioteca
from libro import Libro
from revista import Revista
from lector import Lector
from fpdf import FPDF
import os


def registrar_libro(biblioteca):
    print("\n--- REGISTRAR LIBRO ---")

    codigo = int(input("Codigo: "))
    titulo = input("Titulo: ")
    anio = int(input("Anio de publicacion: "))
    autor = input("Autor: ")
    genero = input("Genero: ")

    libro = Libro(codigo, titulo, anio, autor, genero)

    biblioteca.agregar_material(libro)

    print("Libro registrado correctamente.")


def registrar_revista(biblioteca):
    print("\n--- REGISTRAR REVISTA ---")

    codigo = int(input("Codigo: "))
    titulo = input("Titulo: ")
    anio = int(input("Anio de publicacion: "))
    numero = int(input("Numero de edicion: "))
    periodicidad = input("Periodicidad: ")

    revista = Revista(codigo, titulo, anio, numero, periodicidad)

    biblioteca.agregar_material(revista)

    print("Revista registrada correctamente.")


def registrar_lector(biblioteca):
    print("\n--- REGISTRAR LECTOR ---")

    codigo = int(input("Codigo: "))
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Telefono: ")

    lector = Lector(codigo, nombre, apellido, telefono)

    biblioteca.agregar_lector(lector)

    print("Lector registrado correctamente.")


def mostrar_materiales(biblioteca):
    print("\n--- MATERIALES DE LA BIBLIOTECA ---")

    materiales = biblioteca.get_materiales()

    if not materiales:
        print("No hay materiales registrados.")
        return

    for material in materiales:
        print(material.mostrar_informacion())
        print("------------------------")


def mostrar_lectores(biblioteca):
    print("\n--- LECTORES REGISTRADOS ---")

    lectores = biblioteca.get_lectores()

    if not lectores:
        print("No hay lectores registrados.")
        return

    for lector in lectores:
        print(lector.mostrar_informacion())
        print("------------------------")


def realizar_prestamo(biblioteca):
    print("\n--- REALIZAR PRESTAMO ---")

    codigo_prestamo = int(input("Codigo del prestamo: "))
    codigo_lector = int(input("Codigo del lector: "))
    codigo_material = int(input("Codigo del material: "))
    fecha = input("Fecha del prestamo: ")

    prestamo = biblioteca.realizar_prestamo(
        codigo_prestamo,
        codigo_lector,
        codigo_material,
        fecha
    )

    print("Prestamo realizado correctamente.")
    print(prestamo.mostrar_informacion())


def registrar_devolucion(biblioteca):
    print("\n--- REGISTRAR DEVOLUCION ---")

    codigo = int(input("Codigo del prestamo: "))
    fecha = input("Fecha de devolucion: ")

    prestamo = biblioteca.registrar_devolucion(codigo, fecha)

    print("Devolucion registrada correctamente.")
    print(prestamo.mostrar_informacion())


def mostrar_prestamos(biblioteca):
    print("\n--- HISTORIAL DE PRESTAMOS ---")

    prestamos = biblioteca.get_prestamos()

    if not prestamos:
        print("No hay prestamos registrados.")
        return

    for prestamo in prestamos:
        print(prestamo.mostrar_informacion())
        print("------------------------")


def generar_pdf(biblioteca):
    print("\n--- GENERAR INFORME PDF ---")

    ruta_fuente = "C:/Windows/Fonts/arial.ttf"

    if not os.path.exists(ruta_fuente):
        raise FileNotFoundError("No se encontro la fuente Arial.")

    pdf = FPDF()
    pdf.add_page()

    pdf.add_font("Arial", fname=ruta_fuente)
    pdf.set_font("Arial", size=16)

    pdf.multi_cell(
        0, 10, "INFORME DE BIBLIOTECA",
        align="C", new_x="LMARGIN", new_y="NEXT"
    )
    pdf.ln(5)

    pdf.set_font("Arial", size=13)

    pdf.multi_cell(
        0, 10, "MATERIALES",
        new_x="LMARGIN", new_y="NEXT"
    )

    for material in biblioteca.get_materiales():
        pdf.set_font("Arial", size=11)
        pdf.multi_cell(
            0, 8, material.mostrar_informacion(),
            new_x="LMARGIN", new_y="NEXT"
        )
        pdf.ln(2)

    pdf.set_font("Arial", size=13)
    pdf.multi_cell(
        0, 10, "LECTORES",
        new_x="LMARGIN", new_y="NEXT"
    )

    for lector in biblioteca.get_lectores():
        pdf.set_font("Arial", size=11)
        pdf.multi_cell(
            0, 8, lector.mostrar_informacion(),
            new_x="LMARGIN", new_y="NEXT"
        )
        pdf.ln(2)

    pdf.set_font("Arial", size=13)
    pdf.multi_cell(
        0, 10, "PRESTAMOS",
        new_x="LMARGIN", new_y="NEXT"
    )

    for prestamo in biblioteca.get_prestamos():
        pdf.set_font("Arial", size=11)
        pdf.multi_cell(
            0, 8, prestamo.mostrar_informacion(),
            new_x="LMARGIN", new_y="NEXT"
        )
        pdf.ln(2)

    pdf.output("informe_biblioteca.pdf")

    print("PDF generado correctamente.")




def mostrar_menu():
    print("\n================================")
    print("       SISTEMA DE BIBLIOTECA")
    print("================================")
    print("1. Registrar libro")
    print("2. Registrar revista")
    print("3. Registrar lector")
    print("4. Mostrar materiales")
    print("5. Mostrar lectores")
    print("6. Realizar prestamo")
    print("7. Registrar devolucion")
    print("8. Mostrar prestamos")
    print("9. Generar informe PDF")
    print("0. Salir")
    print("================================")


def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opcion: ")

        try:
            if opcion == "1":
                registrar_libro(biblioteca)

            elif opcion == "2":
                registrar_revista(biblioteca)

            elif opcion == "3":
                registrar_lector(biblioteca)

            elif opcion == "4":
                mostrar_materiales(biblioteca)

            elif opcion == "5":
                mostrar_lectores(biblioteca)

            elif opcion == "6":
                realizar_prestamo(biblioteca)

            elif opcion == "7":
                registrar_devolucion(biblioteca)

            elif opcion == "8":
                mostrar_prestamos(biblioteca)

            elif opcion == "9":
                generar_pdf(biblioteca)

            elif opcion == "0":
                print("Gracias por utilizar la biblioteca.")
                break

            else:
                print("Opcion incorrecta. Intente nuevamente.")

        except (ValueError, TypeError, FileNotFoundError, OSError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
