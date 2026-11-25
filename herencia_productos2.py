"""
Actividad Formativa 3: Herencia en Programación Orientada a Objetos
Autor: Hector Miguel Ramirez Velazquez
Tutor: Gustavo Alfredo Valdez Gonzalez
Descripción: Extensión del Sistema de Gestión de Productos aplicando 
herencia simple, reutilización con super(), sobrescritura y métodos exclusivos.
"""

# ==============================================================================
# 1. CLASE BASE (SUPERCLASE)
# ==============================================================================
class Producto:
    """Clase base que representa un producto comercial genérico en la tienda."""

    def __init__(self, nombre: str, precio: float):
        # Atributos comunes que serán heredados por todas las subclases
        self.nombre = nombre
        self.precio = precio

    def mostrar_datos(self):
        """Método base para imprimir los datos generales del producto."""
        print("-" * 55)
        print(f"Producto: {self.nombre}")
        print(f"Precio base: ${self.precio:.2f}")

    def calcular_precio_con_iva(self) -> float:
        """Método heredable que calcula el precio final con IVA (16%)."""
        return self.precio * 1.16


# ==============================================================================
# 2. CLASE DERIVADA 1: PRODUCTO ELECTRÓNICO
# ==============================================================================
class ProductoElectronico(Producto):
    """
    Subclase que hereda de Producto y especializa artículos de tecnología.
    Reutiliza nombre y precio mediante super().
    """

    def __init__(self, nombre: str, precio: float, marca: str, garantia_meses: int):
        # Llamada al constructor de la clase base
        super().__init__(nombre, precio)
        # Atributos exclusivos de ProductoElectronico
        self.marca = marca
        self.garantia_meses = garantia_meses

    # Sobrescritura (Override) del método de la clase base
    def mostrar_datos(self):
        """Extiende mostrar_datos() añadiendo marca y meses de garantía."""
        super().mostrar_datos()
        print("Categoría: Electrónica")
        print(f"Marca:     {self.marca}")
        print(f"Garantía:  {self.garantia_meses} meses")
        print("-" * 55)

    # Método exclusivo de ProductoElectronico
    def verificar_garantia_extendida(self):
        """Evalúa si el artículo aplica para garantía extendida en tienda."""
        if self.garantia_meses >= 12:
            print(f"[Garantía] {self.nombre} ({self.marca}) incluye cobertura extendida de fábrica.")
        else:
            print(f"[Garantía] {self.nombre} ({self.marca}) cuenta solo con garantía estándar.")


# ==============================================================================
# 3. CLASE DERIVADA 2: PRODUCTO PERECEDERO
# ==============================================================================
class ProductoPerecedero(Producto):
    """
    Subclase que hereda de Producto y modela artículos con fecha de caducidad.
    Incorpora atributos y métodos orientados al control de inventario fresco.
    """

    def __init__(self, nombre: str, precio: float, fecha_caducidad: str, dias_para_vencer: int):
        # Invocación al constructor padre
        super().__init__(nombre, precio)
        # Atributos exclusivos de ProductoPerecedero
        self.fecha_caducidad = fecha_caducidad
        self.dias_para_vencer = dias_para_vencer

    # Sobrescritura (Override) del método de la clase base
    def mostrar_datos(self):
        """Extiende mostrar_datos() mostrando fecha de caducidad."""
        super().mostrar_datos()
        print("Categoría: Perecederos")
        print(f"Caducidad: {self.fecha_caducidad} ({self.dias_para_vencer} días restantes)")
        print("-" * 55)

    # Método exclusivo de ProductoPerecedero
    def aplicar_descuento_caducidad(self):
        """Aplica un 30% de descuento si el producto está próximo a caducar."""
        if self.dias_para_vencer <= 3:
            precio_oferta = self.precio * 0.70
            print(f"[Liquidación] {self.nombre} vence pronto. Nuevo precio: ${precio_oferta:.2f}")
        else:
            print(f"[Inventario] {self.nombre} en buen estado de vigencia. Precio normal: ${self.precio:.2f}")


# ==============================================================================
# 4. PROGRAMA PRINCIPAL (INSTANCIACIÓN Y PRUEBAS DE HERENCIA)
# ==============================================================================
if __name__ == "__main__":
    print("=== SISTEMA DE GESTIÓN DE PRODUCTOS CON HERENCIA (UNIDAD 3) ===\n")

    # Instancias de las subclases
    prod_elec = ProductoElectronico(
        nombre="Teclado Mecánico RGB",
        precio=450.00,
        marca="Logitech",
        garantia_meses=24
    )

    prod_perec = ProductoPerecedero(
        nombre="Leche Entera 1L",
        precio=28.50,
        fecha_caducidad="16/11/2026",
        dias_para_vencer=2
    )

    # 1. Prueba de métodos sobrescritos
    prod_elec.mostrar_datos()
    prod_perec.mostrar_datos()

    # 2. Prueba de método heredado directamente de la clase base Producto
    print(f"Precio con IVA ({prod_elec.nombre}): ${prod_elec.calcular_precio_con_iva():.2f}")
    print(f"Precio con IVA ({prod_perec.nombre}): ${prod_perec.calcular_precio_con_iva():.2f}\n")

    # 3. Prueba de métodos exclusivos de cada subclase
    prod_elec.verificar_garantia_extendida()
    prod_perec.aplicar_descuento_caducidad()

    print("\n=== FIN DE LA EJECUCIÓN ===")