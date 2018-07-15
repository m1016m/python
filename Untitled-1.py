class Shape():
    x = 5
    y = 5
    test = []
    def set_edge(self , m):
       self.test = [[0 for i in range(m)] for j in range(m)]
       
    
    def display(self):
        for i in range (len(self.test)):
           for j in range (len(self.test[i])):
               print self.test[i][j],
           print ""


A = Shape()
A.set_edge(5)
A.display()