class Grade:
    def __init__(self, name, persons):
        self.name = name
        self.persons = persons

    def print_persons(self):  
        for i in self.persons:
            print(i.getFullName())  