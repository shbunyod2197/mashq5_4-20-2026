# 1
class Loptop:
    def __init__(self, model, ram):
        self.model = model
        self.ram = ram

    def show_specs(self):
        print(f"{self.model} {self.ram} Ram")

a = Loptop("HP",166)
a.show_specs()

# 2
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        print(f'{self.name} {self.subject} o\'qituvchi')

a = Teacher("Azamat", "IT")
a.teach()
