# Tarea_4
Control de versiones y documentación de código referente a la tarea 4 de Física Computacional
El propósito de esta tarea es practicar los conceptos de control de versiones bajo la implementación de Git y la creación de documentos de referencia utilizando MkDocs. Su resultado final es un link (URL) que incluye la documentación, utilizando su cuenta de GitHub como host para la página web. Usted debe entregar:

- Un URL con el cual se accesa de manera pública su página web que contiene la documentación del código (10%).

Utilice este tutorial para más información en cómo generar documentación con MkDocs: [https://realpython.com/python-project-documentation-with-mkdocs/](https://realpython.com/python-project-documentation-with-mkdocs/) (ignore lo referente a Type Hints). Es posible que tenga que crear una cuenta para visualizar el artículo.

El objetivo de este proyecto es documentar tres funciones que se utilizan para resolver ODEs: `euler`, `rk2` y `rk4` del laboratorio de la Semana 13 "ODE.ipynb". Las tres funciones se deben encontrar en un archivo `ode.py` contenido en un directorio `ode`. Recuerde que los archivos de MkDocs se encuentran al mismo nivel del directorio del módulo `ode`.

Usted debe escribir las funciones y documentar su uso, argumentos esperados y resultados de salida. Su documentación debe incluir los siguientes apartados:

1. `index.md`: introducción a los métodos utilizados en forma de método numérico, con las ecuaciones relevantes (recuerde que estos documentos usan el mismo lenguaje Markdown).

2. `reference.md`: contiene la documentación de las tres funciones. Debe ser generado de forma automática con los docstrings que contiene el módulo como tal. Los docstrings deben contener ejemplos de uso. Utilice el estilo de docstrings (PEP 257 compliant) que utilizamos en clase (ver `sum.py` en Semana 09 del repositorio del curso).

Usted solo debe entregar el URL de su página web con el host en GitHub, que contiene toda la información del módulo.
