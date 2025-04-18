# read only --> you can not set the value. value can not be changed
# getter --> get a value of a property through a method. Most of the time, you will get the value of a private attribute.
# setter --> set a value of a property through a method. Most of the time, you will set the value of a private property.



class User:

    def __init__(self, name, age, balance):

        self._name = name
        self._age = age
        self.__balance = balance


    # Method
    """
    def get_bal(self):      
        return self.__balance
    """
    

    # Attribute
    # Getter
    # Getter without any setter is readonly attribute

    @property
    def get_bal(self):
        return self.__balance
    
    def set_bal(self, val):
        self.__balance += val
    
    
    @property
    def salary(self):
        return self.__balance
    

    # Setter
    @salary.setter
    def salary(self, val):

        if val < 0:
            val = abs(val)

        self.__balance += val
    
    


n = User('Nadim', 23, 5000)



# Calling Method
# print( n.get_bal() )    #   5000



# Calling Attribute
# print( n.get_bal )    #   5000



n.salary = 150
print( n.salary )


# If we don't use the getter and setter
# n.set_bal(100)
# print(n.get_bal())




# 