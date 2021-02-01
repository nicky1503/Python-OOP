class Car:
    def __init__(self, name, model, engine):
        self.model = model
        self.engine = engine
        self.name = name

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"


