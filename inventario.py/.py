# Programa de inventario 

print("Bienvenido a tu inventario")

# -------------------------------
# Solicitar y validar nombre
# -------------------------------
while True:
    nombre = input("Ingrese el nombre del producto: ")

    if nombre.strip() == "":
        print("Error: el nombre no puede estar vacío.")
    elif not nombre.replace(" ", "").isalpha():
        print("Error: solo se permiten letras.")
    else:
        break


# -------------------------------
# Solicitar y validar precio
# -------------------------------
while True:
    try:
        precio = float(input("Ingrese el precio: "))
        break
    except ValueError:
        print("Error: ingrese un número válido.")


# -------------------------------
# Solicitar y validar cantidad
# -------------------------------
while True:
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        break
    except ValueError:
        print("Error: ingrese un número entero válido.")


# -------------------------------
# Calcular costo total
# -------------------------------
costo_total = precio * cantidad


# -------------------------------
# Mostrar resultados
# -------------------------------
print("Producto:", nombre, "| Precio:", precio, "| Cantidad:", cantidad, "| Total:", costo_total)


# -------------------------------
# Descripción del programa
# -------------------------------
# Este programa solicita al usuario el nombre, precio y cantidad de un producto.
# Valida que los datos ingresados sean correctos.
# Luego calcula el costo total multiplicando precio por cantidad.
# Finalmente, muestra la información en consola de forma clara.

