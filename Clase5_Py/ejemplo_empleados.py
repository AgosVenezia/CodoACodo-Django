from abc import ABC, abstractmethod

# Clase abstracta de Empleado para que otras subclases hereden
class Empleado(ABC):

    def __init__(self,nombre,apellido):
        self.__nombre=nombre               # El __ es el encapsulamiento, son privadas
        self.__apellido=apellido

    def __str__(self):
        return f"{self.__apellido}"

    # GETTER
    @property  
    def apellido(self):
        return self.__apellido

    # SETTER: tomar un parámetro que yo le envío y guardarlo en el interior de la propiedad privada
    @apellido.setter
    def apellido(self, nuevo_apellido):
        self.__apellido = nuevo_apellido
    
    @property                              # Decorador que hace público el encapsulamiento
    def nombre_completo(self):
        return f"Empleado: {self.__nombre} {self.__apellido}"

    @property
    @abstractmethod
    def salario(self):
        pass

    def metodo_uno(self):
        return 10

#empleado_uno = Empleado("Agos", "Venezia")   TypeError: Can't instantiate abstract class Empleado with abstract method salario

#Subclase que hereda de la clase abstracta Empleado
class EmpleadoFullTime(Empleado):

    def __init__(self, nombre, apellido, salario):
        #propiedades heredadas
        super().__init__(nombre, apellido)    #super llama a la superclase
        #propiedades agregadas
        self.__salario = salario

    def __str__(self):
        return super().__str__()  #Llamar al str de la superclase

    @property
    def salario(self):
        return self.__salario 

empleado_uno = EmpleadoFullTime("Agos","Venezia",45000)
#print(empleado_uno)
#print(empleado_uno.salario)
print(empleado_uno.nombre_completo)


class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, apellido, horas_trabajadas, valor_hora):
        super().__init__(nombre, apellido)
        self.__horas_trabajadas = horas_trabajadas
        self.__valor_hora = valor_hora
    
    @property
    def salario(self):
        return self.__horas_trabajadas*self.__valor_hora

empleado_dos = EmpleadoPorHora("Fede","Liquin",40,1000)
print(empleado_dos.salario)


class Nomina:

    def __init__(self):
        self.__lista_empleados = []

    def agregar_empleado(self,empleado):
        self.__lista_empleados.append(empleado)

    def print(self):
        for empleado in self.__lista_empleados:
            if isinstance(empleado,Empleado):
                print(f"{empleado.nombre_completo} - ${empleado.salario}")
            else:
                print(f"En la nómina hay un no empleado")

nomina_empleados = Nomina()

empleado_uno = EmpleadoFullTime("Mario", "Lobos", 50000)
#print(empleado_uno.__apellido)        #AttributeError: 'EmpleadoFullTime' object has no attribute '__apellido'
print(empleado_uno.apellido)           #Se accede con el GETTER
empleado_uno.__apellido = "pepito"     #Se asigna con el SETTER
nomina_empleados.agregar_empleado(empleado_uno)
nomina_empleados.agregar_empleado(EmpleadoPorHora("Gustavo", "Perez", 12, 1000))
nomina_empleados.agregar_empleado(33)      #En la nómina hay un no empleado
nomina_empleados.print()
print(nomina_empleados._Nomina__lista_empleados[0]) #El guión bajo inicial rompe el encapsulamiento


# HERENCIA MÚLTIPLE
class Estudiante():

    def __init__(self,legajo):
        self.__legajo = legajo 

    @property
    def legajo(self):
        return self.__legajo

    def metodo_uno(self):
        return 100000

class EstudiantePasante(Empleado,Estudiante):  #El orden importa

    def __init__(self,nombre,apellido,legajo):
        Empleado.__init__(self,nombre,apellido)
        Estudiante.__init__(self,legajo)

    @property
    def salario(self):
        return 0

    def __str__(self):
        return f"{self.nombre_completo}, Legajo: {self.legajo}"

estudiante_uno = EstudiantePasante("Enzo","Perez","IF-5564")
print(estudiante_uno.metodo_uno())
print(estudiante_uno)

nomina_empleados.agregar_empleado(estudiante_uno)
nomina_empleados.print()