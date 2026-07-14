#Comienzo prueba transversal

# NOMBRE, CATEGORIA, TALLA, COLOR, MATERIAL, ES UNISEX
prendas = {
    'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon', True],
    'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
    'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester', True],
    'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
    'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon', True],
    'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon', False],
}

#Precio, unidades
bodega = {
    'S001': [7990, 12],
    'S002': [19990, 0],
    'S003': [29990, 3],
    'S004': [24990, 6],
    'S005': [17990, 8],
    'S006': [14990, 2],

}

def leer_opcion():
    print('''
            ========== MENÚ PRINCIPAL ==========
            1. Unidades por categoría
            2. Búsqueda de prendas por rango de precio
            3. Actualizar precio de prenda
            4. Agregar prenda
            5. Eliminar prenda
            6. Salir
            =====================================
            ''')
    try:
        opcion = int(input("Ingrese una opción: "))
        if 1 <= opcion > 6:
            print("Ingrese un numero entre el 1 y el 6")
            return False
        else:
            return opcion
    except ValueError:
        print("Ingrese un numero entero")
        return False
    
def unidades_categoria(categoria, prendas, bodega):
    total = 0

    for codigo, datos in prendas.items():
        if datos[1] == categoria.lower():
            total += bodega[codigo][1]

    print(f"El total de {categoria} es de: {total}")
    
def busqueda_precio(p_min, p_max, prendas, bodega):
    resultado = []
    for codigo, datos in bodega.items():
        if datos[0] >= p_min and datos[0] <= p_max and datos[1] != 0:
            resultado.append(f"{prendas[codigo][0]}--{codigo}")
    resultado.sort()
    if len(resultado) == 0:
        print("No existen prendas con ese rango de precio")
    else: 
        print(f"Los resultados son: {resultado}")

def buscar_codigo(codigo, bodega):
    if codigo.upper() in bodega:
        return True
    return False

def actualizar_precio(codigo, nuevo_precio, bodega):
    if buscar_codigo(codigo, bodega):
        bodega[codigo.upper()][0] = nuevo_precio
        return True 
    return False

def valida_codigo(codigo, bodega):
    if codigo.strip() == "":
        return False
    if buscar_codigo(codigo, bodega):
        return False
    return True

def valida_nombre(nombre):
    if nombre.strip() == "":
        return False
    return True

def valida_categoria(categoria):
    if categoria.strip() == "":
        return False
    return True

def valida_talla(talla):
    if talla.strip() == "":
        return False
    return True

def valida_color(color):
    if color.strip() == "":
        return False
    return True

def valida_material(material):
    if material.strip() == "":
        return False
    return True

def valida_es_unisex(es_unisex):
    if es_unisex == "s":
        return True
    return False

def valida_precio(precio):
    if precio > 0:
        return True
    return False

def valida_unidades(unidades):
    if unidades >= 0:
        return True
    return False

def agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades, bodega):
    if buscar_codigo(codigo, bodega):
        return False
    prendas[codigo] = [nombre, categoria, talla, color, material, es_unisex]
    bodega [codigo] = [int(precio), int(unidades)]
    return True


def eliminar_prenda(codigo, prendas, bodega):
    if buscar_codigo(codigo, bodega):
        prendas.pop(codigo.upper())
        bodega.pop(codigo.upper())
        return True
    return False



while True:
    opcion = leer_opcion()

    if opcion == 1:
        categoria = input("Ingrese el nombre de la categoria (polera, pantalon, chaqueta, vestido, poleron, camisa): ")
        unidades_categoria(categoria, prendas, bodega)

    elif opcion == 2:
        while True:
                try:
                    p_min = int(input("Ingrese precio minimo: "))
                    p_max = int(input("Ingrese precio maximo: "))
                    if p_min >= 0 and p_min <= p_max: 
                        busqueda_precio(p_min, p_max, prendas, bodega)
                        break
                    else: 
                        print ("Ingrese un numero mayor que 0 y menos que el minimo")

                except ValueError:
                    print("Debe ingresar numeros enteros")
                    continue

            



    elif opcion == 3: 
        while True:
            codigo = input("Ingrese el codigo de la prenda: ")
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio de la prenda: "))
            except ValueError: 
                print("Ingrese un numero entero")
                continue
            if actualizar_precio(codigo, nuevo_precio, bodega):
                print("Nuevo precio actualizado")
            else:
                print("El codigo no existe")
            
            respuesta = input("Desea actualizar otro precio (s/n): ")
            if respuesta.lower() == "n":
                break

    elif opcion == 4:
        codigo = input("Ingrese el codigo de la prenda: ")
        nombre = input("Ingrese el nombre: ")
        categoria = input("Ingrese la categoria: ")
        talla = input("Ingrese la talla: ")
        color = input("Ingrese el color: ")
        material =input("Ingrese el material: ") 
        es_unisex = input("Es unisex? (s/n): ")
        precio = input("Ingrese su precio: ") 
        unidades = input("Ingrese las unidades: ")

        if not valida_codigo(codigo, bodega):
            print("Codigo invalido o El código ya existe ")
        elif not valida_nombre(nombre):
            print("Nombre invalido")
        elif not valida_categoria(categoria):
            print("Categoria invalido")
        elif not valida_talla(talla):
            print("Talla invalida")
        elif not valida_color(color):
            print ("Color invalido")
        elif not valida_material(material):
            print("Material invalido")
        elif not valida_es_unisex(es_unisex):
            print("Debe ingresar s o n")
        elif not valida_precio(precio):
            print("Precio Invalido")
        elif not valida_unidades(unidades):
            print("Unidades invalidas")
        else: 
            es_unisex_bool = valida_es_unisex(es_unisex)
            if agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades, bodega):
                print("Prenda agregada")
            else:
                print("El código ya existe")

    elif opcion == 5:
        codigo = input("Ingrese el codigo de la prenda: ")
        if eliminar_prenda(codigo, prendas, bodega):
            print("Prenda eliminada")
        else: 
            print("El codigo no existe")
    
    elif opcion == 6:
        print("Programa finalizado")
        break

