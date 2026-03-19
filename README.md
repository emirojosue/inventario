#  Sistema de Inventario Básico

Este es un programa de consola desarrollado en **Python** que permite registrar productos de forma segura y eficiente. El sistema incluye validaciones en tiempo real para evitar errores humanos durante la carga de datos.

---

##  Descripción del Proyecto
El programa funciona como una herramienta de entrada de datos para un inventario. Solicita el nombre, el precio y la cantidad de un artículo, verifica que la información sea lógica (por ejemplo, que no haya números en el nombre o letras en el precio) y genera un cálculo automático del valor total del stock.

**¿Para qué sirve?**
* Controlar el ingreso de mercancía.
* Evitar errores de cálculo manual.
* Asegurar que la base de datos del inventario sea coherente.

---

##  Requisitos e Instalación

### 1. Descargar Python
Para ejecutar este programa, necesitas tener instalado Python en tu equipo:
1. Visita [python.org](https://python.org).
2. Descarga la versión más reciente para tu sistema operativo (Windows, macOS o Linux).

### Instalación
1. Ejecuta el instalador descargado.
2. **IMPORTANTE:** Marca la casilla que dice **"Add Python to PATH"** antes de hacer clic en *Install Now*. Esto permitirá que el programa funcione desde cualquier terminal.

---

##  Cómo ejecutar el proyecto

Sigue estos pasos para poner en marcha el inventario:

1. **Obtener el código:** Guarda el archivo del programa con el nombre `inventario.py`.
2. **Abrir la terminal:** 
   - En Windows: Presiona `Win + R`, escribe `cmd` y pulsa Enter.
   - En Mac/Linux: Abre la aplicación "Terminal".
3. **Localizar el archivo:** Usa el comando `cd` para ir a la carpeta donde guardaste el archivo. 
   *(Ejemplo: `cd Documents/Proyectos`)*.
4. **Ejecutar:** Escribe el siguiente comando y presiona Enter:
   ```bash
   python inventario.py
