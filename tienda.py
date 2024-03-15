from abc import ABC, abstractmethod
from producto import ListaProductos, Producto

class Tienda(ABC):
    @abstractmethod
    def ingresar_producto(self):
        pass
    @abstractmethod
    def listar_productos(self):
        pass
    @abstractmethod
    def realizar_ventas(self):
        pass

class Restaurante(Tienda):
    def __init__(self, nombre: str, costo_delivery: int):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__listado_productos = ListaProductos()
        
    @property
    def nombre(self):
        return self.__nombre
    
    def __str__(self):
        return self.nombre
        
    def ingresar_producto(self, nombre, precio, cantidad):
        producto = Producto(nombre, precio)
        self.__listado_productos.agregar_item(producto)
        
    @property
    def listado_productos(self):
        return self.__listado_productos
        
    def listar_productos(self):
        self.listado_productos.listar("restaurante")
        
    def realizar_ventas(self):
        pass
        
        
class Supermercado(Tienda):
    def __init__(self, nombre: str, costo_delivery: int):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__listado_productos = ListaProductos()
        
    @property
    def nombre(self):
        return self.__nombre
    
    def __str__(self):
        return self.nombre
    
    @property
    def listado_productos(self):
        return self.__listado_productos
    
    def ingresar_producto(self, nombre, precio, cantidad):
        producto = Producto(nombre, precio, cantidad)
        self.__listado_productos.agregar_item(producto)
        
    def listar_productos(self):
        self.listado_productos.listar("supermercado")
        
    def realizar_ventas(self, nombre, cantidad):
        producto = Producto(nombre, 0, cantidad)
        if producto not in self.listado_productos.items:
            print("Producto no existe")
            return
        
        i = self.listado_productos.items.index(producto)
        
        if self.listado_productos.items[i].cantidad < 1:
            print("No hay unidades disponibles")
            return
        
        if self.listado_productos.items[i] >= producto:
            self.listado_productos.items[i] -= producto
        else:
            print(f"Solo hay {self.listado_productos.items[i].cantidad} unidades para ser vendidos")
            self.listado_productos.items[i] -= self.listado_productos.items[i]

class Farmacia(Tienda):
    def __init__(self, nombre: str, costo_delivery: int):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__listado_productos = ListaProductos()
        
    @property
    def nombre(self):
        return self.__nombre
    
    def __str__(self):
        return self.nombre
    
    @property
    def listado_productos(self):
        return self.__listado_productos
    
    def ingresar_producto(self, nombre, precio, cantidad):
        producto = Producto(nombre, precio, cantidad)
        self.__listado_productos.agregar_item(producto)
        
    def listar_productos(self):
        self.listado_productos.listar("farmacia")
        
    def realizar_ventas(self, nombre, cantidad):
        if cantidad > 3:
            print("No se pueden vender mas de 3 unidades")
            return
        
        producto = Producto(nombre, 0, cantidad)
        
        if producto not in self.listado_productos.items:
            print("Producto no existe")
            return
        
        i = self.listado_productos.items.index(producto)
        
        if self.listado_productos.items[i].cantidad < 1:
            print("No hay unidades disponibles")
            return
        
        if self.listado_productos.items[i] >= producto:
            self.listado_productos.items[i] -= producto
        else:
            print(f"Solo hay {self.listado_productos.items[i]} unidades para ser vendidos")
            self.listado_productos.items[i] -= self.listado_productos.items[i]
    
    
    
    
    