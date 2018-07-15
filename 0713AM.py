class Animal:
    name = "LCC"
    def __init__(self,name):
        self.name = name

    def move(self):
        print "移動"
class Cat(Animal):
    def move(self):
        print "貓咪移動"
    def skill(self):
        print "貓咪skill"
class Tiger(Cat):
    def skill(self):
        print "Tigerskill"

A = Cat("LCC")
A.move()
A.skill()
B = Tiger ("LCC")
B.move()
B.skill()
print A.name



