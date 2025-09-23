class Employee:

    def __init__(self, name, salary):
            print("Empleado creado")
            self._name = name
            self._salary = salary
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary >= 0:
            self._salary = new_salary
            print(f"El nuevo salario del empleado es: {self._salary}")
        else:
            print("Error: No se fija el salario del empleado ya que se ingresó un numero negativo")

    @property
    def name(self):
        return self._name
    
    def promote(self, increase):
        current_salary = self._salary
        self.salary = int(self._salary + (self._salary * increase))
        if current_salary == self._salary:
            print("No se realizó el aumento")
        else:
            print(f"Aumento realizado.")



employee1 = Employee("Luis", 100)
print(f"El nombre del empleado es: {employee1.name}")
print(f"El salario del empleado es: {employee1.salary}")
employee1.salary = 200
employee1.promote(0.1)
print(f"El salario del empleado es: {employee1.salary}")
print("\n")

employee2 = Employee("Ana",100)
print(f"El nombre del empleado es: {employee2.name}")
print(f"El salario del empleado es: {employee2.salary}")
employee2.salary = -300
employee2.promote(-1.1)
print(f"El salario del empleado es: {employee2.salary}")
