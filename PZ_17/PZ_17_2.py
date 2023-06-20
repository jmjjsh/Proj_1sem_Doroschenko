# Создание базового класса "Работник" и его наследование для создания классов
# "Менеджер" и "Инженер". В классе "Работник" будут общие методы, такие как
# "работать" и "получать зарплату", а классы-наследники будут иметь свои
class Worker:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} работает")

    def get_salary(self):
        print(f"{self.name} получает зарплату {self.salary}")


class Manager(Worker):
    def __init__(self, name, salary, team):
        super().__init__(name, salary)
        self.team = team

    def get_salary(self):
        total_salary = self.salary + self.team
        print(f"{self.name} получает зарплату {total_salary}")


class Engineer(Worker):
    def __init__(self, name, salary, system):
        super().__init__(name, salary)
        self.system = system

    def design_system(self):
        print(f"{self.name} is designing")


manager = Manager("Джо", 5000, 1000)
engineer = Engineer("Джим", 4000, 5)

manager.work()
manager.get_salary()

engineer.work()
engineer.get_salary()
