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
    resultado.sorf
    if len(resultado) == 0:
        print("No existen prendas con ese rango de precio")
    else: 
        print(f"Los resultados son: {resultado}")


while True:
    opcion = leer_opcion()

    if opcion == 1:
        categoria = input("Ingrese el nombre de la categoria (polera, pantalon, chaqueta, vestido, poleron, camisa): ")
        unidades_categoria(categoria, prendas, bodega)

    elif opcion == 2:
        p_min = (input("Ingrese precio minimo"))
        p_max = (input("Ingrese precio maximo"))
        if p_min >= 0 or p_min < p_max:
            busqueda_precio(p_min, p_max, prendas, bodega)
        else: 
            print("ingrese un numero mayor que 0 o menor al maximo")


