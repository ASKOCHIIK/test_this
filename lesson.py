
class Beka2009:
    def __init__(self, name):
        self.name = name

    def name_bekzat(self):
        return f'меня зовут {self.name}'
      
class Bootcamp34:
    def __init__(self, *name):
        self.name = name

    def info(self):
        return self.name
