def leer_productos(ruta):
    lista=[]
    try:
        with open (ruta,"r",encoding= "utf-8") as f:
            for linea in f:
                campos=linea.strip().split(";")
                try:
                    lista.append((campos[0],float(campos[1]),int(campos[2])))
                except ValueError:
                    print("Error")
    except FileNotFoundError:
        print("fitxero txarto")
    return lista;



def valor_inventario(lista):
    total=[]
    for producto in lista:
        total=+producto[1]*producto[2]
    return total

def consultarPrecio(producto):
    print("Muy bieeen si existeeee: ", producto[0], "Precio: ", producto[1])

def vender(producto, cantidad,lista,stock):
    if not isinstance(cantidad, int):
        raise ValueError("La cantidad debe ser un número entero válido y no negativo.")

    if stock < cantidad:
        raise ValueError("Que no hay suficientes gilipollasssss")
    else:
        lista[producto]=(lista["precio"],stock-cantidad)
        return lista