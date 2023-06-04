from subsisa import SubSystemClassA
from subsisb import SubSystemClassB
from subsisc import SubSystemClassC
from subsisd import SubSystemClassD

class Facade:
    def __init__(self):
        self.sub_system_class_a = SubSystemClassA()
        self.sub_system_class_b = SubSystemClassB()
        self.sub_system_class_c = SubSystemClassC()
        self.sub_system_class_d = SubSystemClassD()

    def create(self):
        result = self.sub_system_class_a.method()
        result += self.sub_system_class_b.method()
        result += self.sub_system_class_c.method()
        result += self.sub_system_class_d.method()
        return result
    
FACADE = Facade()
RESULT = FACADE.create()
print("The result = %s" % RESULT)