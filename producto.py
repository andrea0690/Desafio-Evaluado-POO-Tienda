
class Producto():
    def __init__(self, nombre, precio = 0, cantidad = 0):
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio
        
    @property
    def nombre(self):
        return self.__nombre
        
    @property
    def cantidad (self):
        return self.__cantidad
    
    @property
    def precio (self):
        return self.__precio
    
    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad if cantidad >= 0 else 0
        
    def __str__(self):
        return f"nombre {self.nombre} cantidad {self.cantidad} precio {self.precio}"
        
    def __eq__(self, other):
       return self.nombre.lower() == other.nombre.lower()
        
    def __iadd__(self, other):
        if self == other:
            self.cantidad += other.cantidad
        return self
    
    def __sub__(self, other):
        if self == other:
            self.cantidad -= other.cantidad
        return self
    
    def __ge__(self, other):
        if self == other:
            return self.cantidad >= other.cantidad
        return False
        
        
class ListaProductos():
    def __init__(self):
        self.__items = []
        
    def agregar_item(self, item: Producto):
        if item in self.items:
            indice = self.items.index(item)
            self.items[indice] += item
        else:
            self.__items.append(item)
        
    @property
    def items(self):
        return self.__items
        
    def listar(self, tienda):
        if tienda == "supermercado":
            retorno = (":::::::: DETALLE DE ESTA VENTA :::::::::\n"
            "NOMBRE\t\tPRECIO\t\tCANTIDAD\n")
            items = [
                "{0}\t\t{1}\t\t{2}\n".format(i.nombre, i.precio, str(i.cantidad) + " Pocos productos disponibles" if i.cantidad < 10 else i.cantidad)
                for i in self.items
            ]
            print(f"{retorno}{''.join(items)}")
        if tienda == "farmacia":
            retorno = (":::::::: DETALLE DE ESTA VENTA :::::::::\n"
            "NOMBRE\t\tPRECIO\n")
            items = [
                "{0}\t\t{1}\n".format(i.nombre, str(i.precio) + " Envio gratis al solicitar este producto" if i.precio > 15000 else i.precio)
                for i in self.items
            ]
            print(f"{retorno}{''.join(items)}")
        if tienda == "restaurante":
            retorno = (":::::::: DETALLE DE ESTA VENTA :::::::::\n"
            "NOMBRE\t\tPRECIO\n")
            items = [
                f"{i.nombre}\t\t{i.precio}\n"
                for i in self.items
            ]
            print(f"{retorno}{''.join(items)}")