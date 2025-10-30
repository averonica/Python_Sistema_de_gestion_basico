# Lista principal de productos
productos = []
opcion = ""

while opcion != "5":
    print("--------------------")
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
       precio = input("Ingrese el precio (sin centavos): ").strip()
       if nombre != "" and categoria != "" and precio != "":
          while not precio.isdigit():
            precio = input("Ingrese nuevamente el precio (sin centavos): ").strip()
          precio = int(precio)
          productos.append([nombre, categoria, precio])
          print("Producto agregado correctamente.")
       else:
        print("Datos invalidos. Intente nuevamente.")

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
           for i in range(len(productos)):
             p=productos[i]
             print(f"{i+1}.   |   {p[0]}   |   {p[1]}   |   ${p[2]}  ")  # mostrar todos los productos cargados
        numero_buscar = input("Ingrese el numero del producto a eliminar: ").strip()
        if numero_buscar.isdigit():
            #numero_buscar = int(numero_buscar)
          for i in range(len(productos)):
                if numero_buscar in productos[i].lower():
                 p=productos[i]
                 p.remove(p)
                 print("Producto eliminado:", numero_buscar[i])
                else:
                 print("No se encontró ningún producto con ese numero.")
        else:
          print("Debe ingresar un numero valido.")

    # Salir
    elif opcion == "5":
        print("Saliendo del sistema.")
        break
    # Opcion no valida
    else:
        print("Opcion incorrecta. Intente nuevamente.")
