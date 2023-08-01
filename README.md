

![pythonLogo](https://github.com/RobertGiantSteps/The-Complete-Bootcamp/assets/91851811/ed50dc29-cc81-47ff-963c-bf2204a6819a)
# The Complete Python Bootcamp

Curso de Python

[](https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9373062?start=7#overview)

## Sección 2- Python Setup

1. Comand Line Basics
2. Installing Python(Step by Step)
3. Running Python Code
4. Getting the Notebooks and the Course Material

[https://github.com/Pierian-Data/Complete-Python-3-Bootcamp](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp)

1. Git and Github Overview(Optional)

<aside>
💡 [https://docs.github.com/es/get-started/quickstart/hello-world](https://docs.github.com/es/get-started/quickstart/hello-world)

</aside>

<aside>
💡 [https://docs.github.com/es/get-started/quickstart/git-and-github-learning-resources](https://docs.github.com/es/get-started/quickstart/git-and-github-learning-resources)

</aside>

[Set up Git - GitHub Docs](https://docs.github.com/en/get-started/quickstart/set-up-git)


## 1-MacOS and Linux Command Line (Terminal)

Para saber donde nos encontramos:

```bash
pwd
```

Para listar el contenido de la ubicación donde nos encontramos (archivos y carpetas):

```bash
ls
```

Para ver archivos ocultos:

```bash
ls -a
```

Si deseamos desplazarnos a uno de esos archivos o carpetas,escribimos:

```bash
cd Desktop
```

Para regresar :

```bash
cd ..
```

## 2-Installing Python

Primero instalamos y descargamos Anaconda Navigator(esto incluye librerías y herramientas para trabajar con Python) :

<aside>
🐍 www.anaconda.com/downloads

</aside>

Descargamos la versión 64-Bit Graphical Installer

Luego abrimos Anaconda Navigator

<aside>
🐍 Este navegador es esencialmente una interfaz gráfica para los diversos entornos de desarrollo con los que viene Anaconda

</aside>

Para este curso usaremos Jupyter Notebook este usa el navegador como interfaz visual para escribir código,este se iniciara en la unidad de usuario principal,dependiendo del sistema operativo y en todo caso se deberían ver todos los directorios y todas las carpetas esto nos permite explorar archivos y carpetas en mi computadora.

<aside>
🐍 Si presionamos New nos da la opción de crear un nuevo cuaderno Python 3 ,Text File,Folder,Terminal,Vamos a la carpeta o la creamos donde crearemos el nuevo Notebook con New y luego Python 3.Jupyter Notebook es esencialmente un entorno hay celdas individuales donde escribir código Python,no require conexión a internet todo pasa localmente

</aside>

| Shift + Enter | Ejecuta la celda y creara una nueva debajo |
| --- | --- |
| help /Keyboard shorcuts | Para enumerar los atajos de teclado |
| Markdown en menu desplegable  | convierte la celda en una celda de texto |

Para salir de un Notebook simplemente cerramos la pestaña ,si el icono esta verde es que todavía esta corriendo,para detenerlo marcamos la casilla y Shutdown,el código y el texto se guarda allí,pero no se [eliminan.Si](http://eliminan.Si) deseamos eliminar este cuaderno por completo de la memoria de la computadora ,marcamos la casilla y luego presionamos en el icono del bote de basura o papelera

# Introducción a los tipos de datos de Python.

| Name | Type | Description | Traducción |
| --- | --- | --- | --- |
| Integer | int | Whole numbers,such as: 3 300 200 | Números enteros, tales como: 3 300 200 |
| Floting point | float | Number with a decimal point:2.3 4.6 100.0 | Número con punto decimal: 2.3 4.6 100.0 |
| Strings | str | Ordered sequence of characters:”hello” ‘Sammy’ “2000”  | Secuencia ordenada de caracteres: “hola” ‘Sammy’ “2000” |
| Lists | list | Ordered sequence of objects: [10,”hello”,200.3] | Secuencia ordenada de objetos: [10,”hola”,200.3] |
| Dictionaries | dict | Unordered Key:Value pairs: {”mykey”:”value”,”name”:”Frankie”} | Pares clave:valor no ordenados: {”mykey”:”value”,”name”:”Frankie”} |
| Tuples | tup | Ordered immutable sequence of objects. (10,”hello”,200.3) | Secuencia inmutable ordenada de objetos. (10,”hola”,200.3) |
| Sets(conjuntos) | set | Unordered collection of unique objects:{”a”,”b”} | Colección desordenada de objetos únicos:{”a”,”b”} |
| Booleans | bool | Logical value indicating True or False | Valor lógico que indica Verdadero o Falso |

