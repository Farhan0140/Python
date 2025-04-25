
from abc import ABC

class Person( ABC ):
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


