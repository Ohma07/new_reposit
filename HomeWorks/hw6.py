class Robot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Привет, я робот {self.name}!")

class Mechanism:
    def __init__(self, model):
        self.model = model

    def display_model(self):
        print(f"Модель робота: {self.model}")

class RoboMechanism(Robot, Mechanism):
    def __init__(self, name, model):
        Robot.__init__(self, name)
        Mechanism.__init__(self, model)

    def perform_task(self):
        print(f"Робот {self.name} выполняет задачу!")


robot = RoboMechanism("Robo-X", "RX100")
robot.greet()
robot.display_model()
robot.perform_task()