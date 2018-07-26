class Animal():
    
    def __init__(self):
        self.feet_number = 4
    def shout(self):
        print("I'm a Car!")



class Dog(Animal):
    pass

dog = Dog()
print(dog.feet_number) 
dog.shout()