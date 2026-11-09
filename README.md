# Sistema de Gestion de Biblioteca

## Descripcion del proyecto

Este proyecto consiste en el desarrollo de un sistema de gestion de biblioteca realizado en Python. Su objetivo es administrar los materiales disponibles, registrar lectores y controlar los prestamos y las devoluciones.

El sistema funciona mediante un menu interactivo que permite realizar distintas operaciones y generar un informe en formato PDF con la informacion registrada.

## Funcionalidades principales

El sistema permite:

- Registrar libros.
- Registrar revistas.
- Registrar lectores.
- Mostrar los materiales registrados.
- Mostrar los lectores registrados.
- Realizar prestamos de materiales.
- Registrar devoluciones.
- Consultar el historial de prestamos.
- Generar un informe en formato PDF.

## Tecnologias utilizadas

- Python: lenguaje de programacion utilizado para desarrollar el sistema.
- Pytest: herramienta utilizada para realizar las pruebas unitarias.
- FPDF2: biblioteca utilizada para generar informes PDF.
- Git: sistema de control de versiones.
- GitHub: plataforma para alojar y compartir el codigo del proyecto.

## Organizacion de los archivos

El proyecto esta organizado en los siguientes archivos:

| Archivo | Descripcion |
|---|---|
| main.py | Contiene el menu principal y las funciones para interactuar con el sistema. |
| biblioteca.py | Administra los materiales, lectores y prestamos. |
| material.py | Define la clase base Material. |
| libro.py | Define la clase Libro, que hereda de Material. |
| revista.py | Define la clase Revista, que hereda de Material. |
| lector.py | Define la clase Lector. |
| prestamo.py | Define la clase Prestamo y sus operaciones. |
| prueba_manual.py | Permite realizar comprobaciones manuales. |
| requirements.txt | Contiene las dependencias necesarias para ejecutar el proyecto. |
| tests/ | Contiene las pruebas unitarias realizadas con Pytest. |

## Conceptos de programacion orientada a objetos

Durante el desarrollo se aplicaron los siguientes conceptos:

- Encapsulamiento: se utilizaron atributos privados y metodos getters y setters para acceder y modificar los datos de los objetos.
- Herencia: las clases Libro y Revista heredan los atributos y metodos de la clase Material.
- Polimorfismo: las clases Libro y Revista redefinen el metodo mostrar_informacion() para mostrar sus datos particulares.
- Abstraccion: se representaron las caracteristicas y comportamientos comunes de los materiales mediante la clase base Material.

## Instalacion y ejecucion

Para ejecutar el proyecto es necesario tener Python instalado.

1. Abrir una terminal en la carpeta del proyecto.

2. Crear el entorno virtual:

   ```cmd
   py -m venv venv
   ```

3. Activar el entorno virtual:

   ```cmd
   venv\Scripts\activate
   ```

4. Instalar las dependencias:

   ```cmd
   py -m pip install -r requirements.txt
   ```

5. Ejecutar el sistema:

   ```cmd
   py main.py
   ```

## Pruebas unitarias

Para comprobar el funcionamiento de las clases y funciones se utilizo Pytest.

Para ejecutar todas las pruebas, utilizar el siguiente comando:

```cmd
py -m pytest -v
```

El proyecto cuenta con 15 pruebas unitarias que verifican el registro de datos, las busquedas, los prestamos, las devoluciones, las validaciones y la generacion del informe PDF.

## Generacion del informe PDF

El sistema permite generar un archivo llamado informe_biblioteca.pdf, que contiene la informacion de los materiales, lectores y prestamos registrados.

## Consideraciones

Los datos se almacenan en memoria mientras el programa esta en ejecucion. Por este motivo, al cerrar el sistema y volver a iniciarlo, los registros realizados anteriormente no se conservan.

## Conclusion

Este proyecto permitio poner en practica los conceptos de programacion orientada a objetos, el manejo de errores, las pruebas unitarias y la organizacion de un proyecto mediante distintos archivos de Python. Tambien permitio trabajar con herramientas de control de versiones y generacion de documentos PDF.