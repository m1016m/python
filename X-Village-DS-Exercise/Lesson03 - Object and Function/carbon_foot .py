def carbon_foot(km) :
    def bus(rate) :
        return rate * km
    return bus

km = 100
way = carbon_foot(km)
print ("公車碳足跡排放量 : " , way(0.03), " (kg/km) ")
print ("汽車碳足跡排放量 : " , way(0.24), " (kg/km) ")
print ("機車碳足跡排放量 : " , way(0.06), " (kg/km) ")