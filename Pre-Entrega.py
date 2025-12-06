# Lista principal de productos
productos = []
opcion = ""

while opcion != "5":
    print ("="*40)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    opcion = input("Seleccione una opción: ").strip()

   # Agregar producto
    pos=0
    if opcion == "1":
       print("---- Agregar producto ----")
       nombre = input("Ingrese el nombre del producto: ").strip()
       categoria = input("Ingrese la categoría: ").strip()
       if nombre != "" and categoria != "":
          precio = input("Ingrese el precio (sin centavos): ").strip()
        
          while precio == "" or not precio.isdigit():
            print("El precio debe ser un número entero.")
            precio = input("Ingrese nuevamente el precio (sin centavos): ").strip()
          precio = int(precio)
          productos.append([nombre, categoria, precio])
          print("Producto agregado correctamente.")
       else:
        print("Datos inválidos. Intente nuevamente.")


   # Mostrar productos
    elif opcion == "2":
        print("---- Lista de productos ----")
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            print("Numero | Producto | Categoria | Precio")
            for i in range(len(productos)):
                p=productos[i]    
                print(f"{i+1}.   |   {p[0]}   |   {p[1]}   |   ${p[2]}  ")  

    # Buscar producto
    elif opcion == "3":
        print("---- Buscar producto ----")
        nombre_buscar = input("Ingrese el nombre del producto: ").strip()
        encontrado = False
        for i in range(len(productos)):
            p=productos[i]
            if nombre_buscar in p[0].lower():
                print(f"{i+1}.   |   {p[0]}   |   {p[1]}   |   ${p[2]}  ")  
                encontrado = True
        if not encontrado:
            print("No se encontró ningún producto con ese nombre.")

   # Eliminar producto
    elif opcion == "4":
     print("---- Eliminar producto ----")

     if len(productos) == 0:
        print("No hay productos para eliminar.")
     else:
        # Mostrar productos antes de eliminar
        for i in range(len(productos)):
            p = productos[i]
            print(f"{i+1}.   |   {p[0]}   |   {p[1]}   |   ${p[2]}")
        numero_buscar = input("Ingrese el número del producto a eliminar: ").strip()
        # Validar que sea un número
        if numero_buscar.isdigit():
            numero_buscar = int(numero_buscar)

            # Validar que esté dentro del rango
            if 1 <= numero_buscar <= len(productos):
                eliminado = productos.pop(numero_buscar - 1)  # Eliminación correcta
                print("Producto eliminado:", eliminado[0])
            else:
                print("Número fuera de rango.")
        else:
            print("Debe ingresar un número válido.")
   # Salir
    elif opcion == "5":
        print("Saliendo del sistema.")
        break
    # Opcion no valida
    else:
        print("Opcion incorrecta. Intente nuevamente.")
