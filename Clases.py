from abc import ABC, abstractmethod
import datetime

class Usuario(ABC):
    def __init__(self, nombre, apellido, email, contrasenia):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia

    @abstractmethod
    def __str__(self):
        return f"Nombre: {self._nombre} Apellido: {self._apellido} Email: {self._email} Contrasenia: {self._contrasenia}"

    @abstractmethod
    def validar_credenciales(self, email, contrasenia):
        pass


class Archivo():
    def __init__(self, nombre_Archivo: str, fecha: datetime.date, formato: str):
        self._nombre_Archivo = nombre_Archivo
        self._fecha = fecha
        self._formato = formato
        listaarchivos.append(self)

    def __str__(self):
        return f"{self._nombre_Archivo} FECHA:{self._fecha} FORMATO {self._formato}"


class Curso():
    
    def __init__(self, nombre_Curso , prox_Cod: int):
        self._nombre_Curso = nombre_Curso
        self._prox_Cod= prox_Cod
        self._contrasenia_matriculacion = None
    

    def __str__(self):
        return f"Nombre del curso: {self._nombre_Curso}\nCodigo:{self._prox_Cod}\nContrasenia: {self._contrasenia_matriculacion} \n"
    
    def nuevo_Archivo(self, nombre, fecha, formato):
        archivo = Archivo(nombre, fecha, formato)
        return archivo

        

    def generar_contrasenia(self):
        import random
        import string

        self._contrasenia_matriculacion = "".join(
            random.choices(string.ascii_letters + string.digits, k=6)
        )
   

        
class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anioInscripcion):
        super().__init__(nombre, apellido, email, contrasenia)
        self._legajo = legajo
        self._anio_inscripcion_carrera = anioInscripcion
        listadeAlumnos.append(self)
        self.mis_cursos = []

    @staticmethod  
    def validar_credenciales(email, contrasenia):
        for estudiante in listadeAlumnos:
            if estudiante._email == email and estudiante._contrasenia == contrasenia:
                return True
        return False

    def __str__(self):
        return f" Nombre : {self._nombre} Apellido: {self._apellido} Legajo: {self._legajo} Año de la inscripcion de la carrera: {self._anio_inscripcion_carrera}"

    def matricular_en_curso(self, curso):
        if curso not in self.mis_cursos:
            matriculacion = input(
                f"Ingrese la contraseña de matriculación para {curso._nombre_Curso}: "
            )
            if matriculacion == curso._contrasenia_matriculacion:
                self.mis_cursos.append(curso)
                print(f"Te has matriculado en {curso._nombre_Curso}")
            else:
                print("Contraseña de matriculación incorrecta.")
        else:
            print(f"Ya estás matriculado en {curso._nombre_Curso}")
    def desmatricular_curso(self, curso):
        if curso in self.mis_cursos:
            desmatriculacion = input(f"ingrese la materia a desmatricular (PARA CONFIRMAR)\t")
            if(desmatriculacion == curso._nombre_Curso):
                    self.mis_cursos.remove(curso)
                    print("te has desmatriculado correctamente")
            else:
                print("ingrese correctamente el curso")

class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, titulo, anio_egreso):
        super().__init__(nombre, apellido, email, contrasenia)
        self._titulo = titulo
        self._anio_egreso = anio_egreso
        listadeProfesores.append(self)
        self.mis_cursos = []

    @staticmethod
    def validar_credenciales(email, contrasenia):
        for profes in listadeProfesores:
            if profes._email == email and profes._contrasenia == contrasenia:
                return True
        return False

    def dictar_curso(self, curso: Curso):
        curso.generar_contrasenia()
        self.mis_cursos.append(curso)

    def __str__(self):
        return f" Nombre: {self._nombre} Apellido: {self._apellido} Email: {self._email} Contra: {self._contrasenia} titulo:{self._titulo} Año:{self._anio_egreso}"

class Carrera:
    def __init__(self , nombreCarrera , cantAnios):
        self._nombreCarrera = nombreCarrera
        self._cantAnios = cantAnios
    def __str__(self):
        print(f"carrera:{self._nombreCarrera} años:{self._cantAnios} ")
    def get_cantidad_materias(self):
        print(len(cursos_de_la_carrera))

#LISTAS
listaarchivos=[]
listadeAlumnos = []
listadeProfesores = []


#CARGA DE USUARIOS
Usuario1 = Estudiante(
    "Matias", "Fernandez", "matifernandez@gmail.com", "123", 111, 2021
)
Usuario2 = Profesor("Miguel", "Hernandez", "miguelhernandez@gmail.com", "222" , "Ingeniero","2015", )


carrera1 = Carrera = (
    'Tecnicatura en Programacion' , 2 )
cursos_disponibles = []
#cursos de la carrera
cursos_de_la_carrera = [
    {"Materia": "Inglés I", "Carrera:": carrera1},
    {"Materia": "Programación II", "Carrera:": carrera1},
    {"Materia": "Inglés II", "Carrera:": carrera1},
    {"Materia": "Laboratorio II", "Carrera:": carrera1},
    {"Materia": "Programación I", "Carrera:": carrera1},
    {"Materia": "Laboratorio I", "Carrera:": carrera1},
]



