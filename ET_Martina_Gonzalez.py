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
    
