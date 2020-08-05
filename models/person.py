class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def getFullName(self):
        return self.username+" "+self.password    