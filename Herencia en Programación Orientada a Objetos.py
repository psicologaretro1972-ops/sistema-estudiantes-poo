"""
Actividad Formativa 3: Herencia en Programación Orientada a Objetos
Autora: María del Rocío Ruíz Sánchez | Matrícula: 25390
Descripción: Extensión del sistema de gestión de estudiantes (Unidad 2)
aplicando herencia simple, reutilización con super(), sobrescritura y métodos exclusivos.
"""

# ==============================================================================
# 1. CLASE BASE (SUPERCLASE)
# ==============================================================================
class Estudiante:
    """Clase base que representa a un estudiante universitario genérico."""

    def __init__(self, nombre: str, carrera: str, promedio: float):
        # Atributos comunes que serán heredados por todas las subclases
        self.nombre = nombre
        self.carrera = carrera
        self.promedio = promedio

    def mostrar_informacion(self):
        """Método base para desplegar los datos generales del estudiante."""
        print("-" * 50)
        print(f"Estudiante: {self.nombre}")
        print(f"Carrera:    {self.carrera}")
        print(f"Promedio:   {self.promedio}")

    def evaluar_estatus(self) -> str:
        """Método heredable que determina el estatus académico según el promedio."""
        if self.promedio >= 9.0:
            return "Excelencia Académica"
        elif self.promedio >= 7.0:
            return "Regular Aprobado"
        return "En Riesgo Académico"


# ==============================================================================
# 2. CLASE DERIVADA 1: ESTUDIANTE DE LICENCIATURA
# ==============================================================================
class EstudianteLicenciatura(Estudiante):
    """
    Subclase que hereda de Estudiante y especializa el perfil para nivel pregrado.
    Reutiliza nombre, carrera y promedio mediante super().
    """

    def __init__(self, nombre: str, carrera: str, promedio: float,
                 semestre: int, servicio_social_activo: bool = False):
        # Llamada al constructor de la clase base para reutilizar código
        super().__init__(nombre, carrera, promedio)
        # Atributos únicos de la subclase EstudianteLicenciatura
        self.semestre = semestre
        self.servicio_social_activo = servicio_social_activo

    # Sobrescritura (Override) del método de la clase base
    def mostrar_informacion(self):
        """Extiende mostrar_informacion() de Estudiante añadiendo datos de licenciatura."""
        super().mostrar_informacion()  # Reutiliza la impresión base
        estado_ss = "En curso" if self.servicio_social_activo else "Pendiente"
        print(f"Nivel:      Licenciatura (Semestre {self.semestre})")
        print(f"Serv. Soc.: {estado_ss}")
        print("-" * 50)

    # Método exclusivo de EstudianteLicenciatura
    def verificar_servicio_social(self):
        """Evalúa si el alumno cumple el requisito de semestre para servicio social."""
        if self.servicio_social_activo:
            print(f"[Servicio Social] {self.nombre} ya se encuentra realizando su servicio.")
        elif self.semestre >= 7:
            print(f"[Servicio Social] {self.nombre} es elegible para iniciar trámite (Sem. {self.semestre}).")
        else:
            faltan = 7 - self.semestre
            print(f"[Servicio Social] {self.nombre} aún no cumple créditos (faltan {faltan} semestres).")


# ==============================================================================
# 3. CLASE DERIVADA 2: ESTUDIANTE DE POSGRADO
# ==============================================================================
class EstudiantePosgrado(Estudiante):
    """
    Subclase que hereda de Estudiante y modela a alumnos de maestría o doctorado.
    Incorpora atributos y métodos orientados a investigación y tesis.
    """

    def __init__(self, nombre: str, carrera: str, promedio: float,
                 tema_tesis: str, asesor: str):
        # Invocación al constructor padre
        super().__init__(nombre, carrera, promedio)
        # Atributos exclusivos de EstudiantePosgrado
        self.tema_tesis = tema_tesis
        self.asesor = asesor

    # Sobrescritura (Override) del método de la clase base
    def mostrar_informacion(self):
        """Extiende mostrar_informacion() mostrando proyecto de investigación y asesor."""
        super().mostrar_informacion()
        print(f"Nivel:      Posgrado")
        print(f"Tesis:      {self.tema_tesis}")
        print(f"Asesor:     {self.asesor}")
        print("-" * 50)

    # Método exclusivo de EstudiantePosgrado
    def evaluar_avance_tesis(self, porcentaje_avance: int):
        """Registra y valida el progreso de investigación del estudiante de posgrado."""
        print(f"[Investigación] Tesis '{self.tema_tesis}' | Avance actual: {porcentaje_avance}%")
        if porcentaje_avance >= 80 and self.promedio >= 8.5:
            print(f" -> Dictamen de {self.asesor}: Autorizado para examen de grado.")
        else:
            print(f" -> Dictamen de {self.asesor}: Continuar desarrollo experimental.")


# ==============================================================================
# 4. PROGRAMA PRINCIPAL (INSTANCIACIÓN Y PRUEBAS DE HERENCIA)
# ==============================================================================
if __name__ == "__main__":
    print("=== SISTEMA ACADÉMICO CON HERENCIA (UNIDAD 3) ===\n")

    # Instancia de EstudianteLicenciatura (reutiliza datos base + propios)
    alumno_lic = EstudianteLicenciatura(
        nombre="María del Rocío Ruíz Sánchez",
        carrera="Ingeniería en Desarrollo de Software",
        promedio=9.5,
        semestre=3,
        servicio_social_activo=False
    )

    # Instancia de EstudiantePosgrado
    alumno_pos = EstudiantePosgrado(
        nombre="Carlos Pérez",
        carrera="Maestría en Ciencia de Datos",
        promedio=9.2,
        tema_tesis="Optimización de Modelos Predictivos en Educación",
        asesor="Dr. Gustavo Alfredo Valdez González"
    )

    # 1. Prueba de métodos sobrescritos
    alumno_lic.mostrar_informacion()
    alumno_pos.mostrar_informacion()

    # 2. Prueba de método heredado directamente de la clase base Estudiante
    print(f"Estatus heredado ({alumno_lic.nombre}): {alumno_lic.evaluar_estatus()}")
    print(f"Estatus heredado ({alumno_pos.nombre}): {alumno_pos.evaluar_estatus()}\n")

    # 3. Prueba de métodos exclusivos de cada subclase
    alumno_lic.verificar_servicio_social()
    alumno_pos.evaluar_avance_tesis(85)

    print("\n=== FIN DE LA EJECUCIÓN ===")