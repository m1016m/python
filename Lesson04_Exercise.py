class Car():
    color = "Red"
    __speed = 0
    def set_speed(self,speed):
        #self.color = color
        self.__speed = speed
    def boest(self , speed):
        if self.__speed >= 100:
           self.__speed += speed
        print "現在時速:",self.get_speed()

    def step_break(self , speed):
       if self.__speed <= 90:
           self.__speed -= speed
       print "現在時速:",self.get_speed()
    def get_speed(self):
        return self.__speed

piliCar = Car()
BMWCar = Car()
#piliCar.boest(150)
#BMWCar.step_break(80)
piliCar.set_speed(180)
print piliCar.get_speed()