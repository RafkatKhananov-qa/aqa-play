class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print("Working...")


class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def work(self):
        super().work()
        print(f"Coding in {self.language}")


dev = Developer("Rafkat", "Python")
dev.work()
