class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def get_info(self):
        return f"Имя - {self.name}, id - {self.id}"
    
class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department
    
    def manage_project(self):
        return f"{self.name} руководит проектом в департаменте {self.department}"

class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization
    
    def perform_maintenance(self):
        return f"{self.name} {self.specialization} выполняет техническое обслуживание"

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.human = []
    
    def manage_project(self):
        return f"{self.name} руководит проектом в департаменте {self.department}"

    def perform_maintenance(self):
        return f"{self.name} {self.specialization} выполняет техническое обслуживание"
    
    def add_employee(self, employee):
        self.human.append(employee)

    def get_team_info(self):
        info = f"Команда {self.name}:\n"
        if not self.human:
            info += "Нет сотрудников"
        else:
            for emp in self.human:
                info += f"{emp.get_info()}\n"
        return info

employee1 = Employee("Иван Петров", "1")
manager1 = Manager("Мария Сидорова", "2", "Разработка")
technician1 = Technician("Алексей Козлов", "3", "IT")
techmanager1 = TechManager("Дмитрий Волков", "4", "Сети", "Разработка")

print(employee1.get_info())
print(manager1.manage_project())
print(technician1.perform_maintenance())

print(techmanager1.get_info())
print(techmanager1.manage_project())
print(techmanager1.perform_maintenance())

techmanager1.add_employee(employee1)
techmanager1.add_employee(manager1)
techmanager1.add_employee(technician1)
print(techmanager1.get_team_info())
