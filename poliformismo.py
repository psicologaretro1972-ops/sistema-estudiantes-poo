"""
Actividad Formativa 4: Sistema de Gestión de Inventarios en Python.
Demuestra el uso de clases abstractas (ABC), interfaces (contratos abstractos),
herencia, polimorfismo y gestión de inventario.
"""

from abc import ABC, abstractmethod


# ==========================================
# INTERFACES (Contratos abstractos en Python)
# ==========================================

class Vendible(ABC):
    """
    Interfaz que define el comportamiento obligatorio para cualquier producto
    que pueda venderse y calcular un precio final.
    """

    @abstractmethod
    def calcular_precio_final(self) -> float:
        """Calcula y retorna el precio final del producto."""
        pass


class Actualizable(ABC):
    """
    Interfaz que define la capacidad de ajustar precios o valores de forma uniforme.
    """

    @abstractmethod
    def aplicar_ajuste(self, porcentaje: float) -> None:
        """Ajusta el precio base según un porcentaje (positivo para subir, negativo para bajar)."""
        pass


# ==========================================
# CLASE ABSTRACTA BASE: Producto
# ==========================================

class Producto(ABC):
    """
    Clase abstracta base que agrupa atributos y comportamientos comunes
    a todos los productos del inventario. No puede instanciarse directamente.
    """

    def __init__(self, id_producto: str, nombre: str, precio_base: float, cantidad_stock: int):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio_base = precio_base
        self.cantidad_stock = cantidad_stock

    @abstractmethod
    def mostrar_info(self) -> str:
        """Método abstracto: cada subclase debe formatear su información específica."""
        pass

    def valor_total_stock(self, precio_unitario: float) -> float:
        """Método concreto heredado: calcula el valor monetario del stock disponible."""
        return precio_unitario * self.cantidad_stock


# ==========================================
# SUBCLASES DERIVADAS (Herencia y Polimorfismo)
# ==========================================

class Electronico(Producto, Vendible, Actualizable):
    """
    Subclase de Producto para artículos electrónicos.
    Aplica un impuesto adicional del 16% (IVA) en el cálculo de precio final.
    """

    def __init__(self, id_producto: str, nombre: str, precio_base: float, cantidad_stock: int,
                 marca: str, garantia_meses: int):
        # Invocación al constructor de la clase padre Producto
        super().__init__(id_producto, nombre, precio_base, cantidad_stock)
        self.marca = marca
        self.garantia_meses = garantia_meses

    # Implementación polimórfica de Vendible
    def calcular_precio_final(self) -> float:
        iva = 0.16
        return round(self.precio_base * (1 + iva), 2)

    # Implementación polimórfica de Actualizable
    def aplicar_ajuste(self, porcentaje: float) -> None:
        self.precio_base = round(self.precio_base * (1 + porcentaje / 100), 2)

    # Implementación polimórfica de Producto
    def mostrar_info(self) -> str:
        precio_final = self.calcular_precio_final()
        total = self.valor_total_stock(precio_final)
        return (
            f"[Electrónico] ID: {self.id_producto} | {self.nombre} ({self.marca}) | "
            f"Garantía: {self.garantia_meses} meses | Stock: {self.cantidad_stock} | "
            f"Precio final: ${precio_final:.2f} | Valor stock: ${total:.2f}"
        )


class Alimento(Producto, Vendible, Actualizable):
    """
    Subclase de Producto para alimentos.
    Aplica un descuento promocional del 10% si es perecedero para rotar inventario.
    """

    def __init__(self, id_producto: str, nombre: str, precio_base: float, cantidad_stock: int,
                 fecha_caducidad: str, es_perecedero: bool):
        super().__init__(id_producto, nombre, precio_base, cantidad_stock)
        self.fecha_caducidad = fecha_caducidad
        self.es_perecedero = es_perecedero

    # Implementación polimórfica de Vendible
    def calcular_precio_final(self) -> float:
        if self.es_perecedero:
            return round(self.precio_base * 0.90, 2)  # 10% de rotación rápida
        return round(self.precio_base, 2)

    # Implementación polimórfica de Actualizable
    def aplicar_ajuste(self, porcentaje: float) -> None:
        self.precio_base = round(self.precio_base * (1 + porcentaje / 100), 2)

    # Implementación polimórfica de Producto
    def mostrar_info(self) -> str:
        precio_final = self.calcular_precio_final()
        total = self.valor_total_stock(precio_final)
        tipo_alimento = "Perecedero" if self.es_perecedero else "No perecedero"
        return (
            f"[Alimento] ID: {self.id_producto} | {self.nombre} ({tipo_alimento}, "
            f"Cad: {self.fecha_caducidad}) | Stock: {self.cantidad_stock} | "
            f"Precio final: ${precio_final:.2f} | Valor stock: ${total:.2f}"
        )


class Ropa(Producto, Vendible, Actualizable):
    """
    Subclase de Producto para prendas de vestir.
    Aplica un recargo de temporada del 5% sobre el precio base.
    """

    def __init__(self, id_producto: str, nombre: str, precio_base: float, cantidad_stock: int,
                 talla: str, material: str):
        super().__init__(id_producto, nombre, precio_base, cantidad_stock)
        self.talla = talla
        self.material = material

    # Implementación polimórfica de Vendible
    def calcular_precio_final(self) -> float:
        return round(self.precio_base * 1.05, 2)

    # Implementación polimórfica de Actualizable
    def aplicar_ajuste(self, porcentaje: float) -> None:
        self.precio_base = round(self.precio_base * (1 + porcentaje / 100), 2)

    # Implementación polimórfica de Producto
    def mostrar_info(self) -> str:
        precio_final = self.calcular_precio_final()
        total = self.valor_total_stock(precio_final)
        return (
            f"[Ropa] ID: {self.id_producto} | {self.nombre} (Talla: {self.talla}, "
            f"Material: {self.material}) | Stock: {self.cantidad_stock} | "
            f"Precio final: ${precio_final:.2f} | Valor stock: ${total:.2f}"
        )


# ==========================================
# GESTOR DE INVENTARIO (Uso de Polimorfismo)
# ==========================================

class GestorInventario:
    """Administra una colección heterogénea de productos tratándolos de forma uniforme."""

    def __init__(self):
        self.productos: list[Producto] = []

    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def listar_inventario(self) -> None:
        """Llama a mostrar_info() en cada objeto sin importar su clase concreta."""
        print("\n--- REPORTE DE INVENTARIO ---")
        for item in self.productos:
            print(item.mostrar_info())

    def ajustar_precios_masivo(self, porcentaje: float) -> None:
        """Aplica aplicar_ajuste() polimórficamente a todos los productos actualizables."""
        print(f"\n--- APLICANDO AJUSTE DEL {porcentaje}% A TODOS LOS PRODUCTOS ---")
        for item in self.productos:
            if isinstance(item, Actualizable):
                item.aplicar_ajuste(porcentaje)

    def calcular_valor_total_inventario(self) -> float:
        """Suma el valor total de todos los productos usando polimorfismo."""
        total_general = 0.0
        for item in self.productos:
            if isinstance(item, Vendible):
                precio_u = item.calcular_precio_final()
                total_general += item.valor_total_stock(precio_u)
        return round(total_general, 2)


# ==========================================
# PROGRAMA PRINCIPAL Y PRUEBAS
# ==========================================

def ejecutar_pruebas() -> None:
    """Instancia subclases, ejecuta pruebas de polimorfismo y verifica resultados."""
    inventario = GestorInventario()

    # Instanciación de distintas subclases
    laptop = Electronico("E-001", "Laptop 15\"", 12000.00, 5, "Lenovo", 12)
    leche = Alimento("A-001", "Leche Entera 1L", 24.00, 30, "2026-12-15", True)
    chamarra = Ropa("R-001", "Chamarra Térmica", 850.00, 10, "M", "Poliéster")

    inventario.agregar_producto(laptop)
    inventario.agregar_producto(leche)
    inventario.agregar_producto(chamarra)

    # 1. Prueba inicial de polimorfismo al mostrar información
    inventario.listar_inventario()

    # 2. Prueba de ajuste de precios (+5%) y verificación posterior
    inventario.ajustar_precios_masivo(5.0)
    inventario.listar_inventario()

    # 3. Verificación del valor total del inventario
    valor_total = inventario.calcular_valor_total_inventario()
    print(f"\nValor total del inventario: ${valor_total:.2f}")

    # Aserciones básicas de prueba (unitarias rápidas)
    assert isinstance(laptop, Producto)
    assert laptop.calcular_precio_final() == round(12600.00 * 1.16, 2)
    assert leche.calcular_precio_final() == round(25.20 * 0.90, 2)
    assert chamarra.calcular_precio_final() == round(892.50 * 1.05, 2)
    print("\n[OK] Todas las pruebas de polimorfismo pasaron correctamente.")


if __name__ == "__main__":
    ejecutar_pruebas()