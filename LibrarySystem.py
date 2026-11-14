class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def introduce(self):
        print(f"Hello! I am {self.name}, a {self.model} model.")

bot1 = Robot("Robo", "V2")
bot1.introduce()


