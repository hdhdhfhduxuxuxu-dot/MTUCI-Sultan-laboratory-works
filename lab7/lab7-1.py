class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f"{self.name}, id: {self.id}"


class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def manage_project(self):
        return f"{self.name} курирует работу отдела {self.department}"


class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"{self.name} выполняет задачи по профилю: {self.specialization}"


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.human = []

    def add_employee(self, employee):
        self.human.append(employee)

    def get_team_info(self):
        info = f"Состав команды {self.name}:\n"
        if not self.human:
            info += "сотрудников нет"
        else:
            for emp in self.human:
                info += emp.get_info() + "\n"
        return info


# Демонстрация работы системы

employee1 = Employee("Данил Корнеев", 1)
manager1 = Manager("Артём Лебедев", 2, "Поддержка")
technician1 = Technician("Влад Миронов", 3, "DevOps инженер")
techmanager1 = TechManager("Сергей Фомин", 4, "IT-отдел", "Системный администратор")

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



