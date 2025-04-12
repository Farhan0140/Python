# base class, parent class, common attribute + functionality class

class Base_Class:
    pass
    

    

# derived class, child class, uncommon attribute + functionality class

class Derived_Class( Base_Class ):
    pass


class Derived_Class( Base_Class ):
    def __init__(self):
        super().__init__()

        
"""

1. simple inheritance: parent class --> child class 


2. Multi-level inheritance: Granpa --> Parent --> child

"""

