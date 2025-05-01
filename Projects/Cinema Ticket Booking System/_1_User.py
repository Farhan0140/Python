
from abc import ABC


class User( ABC ):
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.__pass = password

    
    @property
    def password(self):
        return self.__pass
    

    @password.setter
    def password(self, new_password):
        self.__pass = new_password


