class Shape():
    test = []
    def set_edge(self , m):
       self.m = m
       self.test = [[ "*" for i in range(m)] for j in range(m)]
    
    def set_pattern(self , x):
        print int(((self.m-1)/2-x)*3)
        self.test[int((self.m-1)/2-x)][int((self.m-1)/2-x)] = 0
        self.test[int((self.m-1)/2-x)][int(((self.m-1)/2-x)+1)] = 0
        self.test[int((self.m-1)/2-x)][int(((self.m-1)/2-x)*2)] = 0
        self.test[int(((self.m-1)/2-x)+1)][int((self.m-1)/2-x)] = 0
        self.test[int(((self.m-1)/2-x)*2)][int(((self.m-1)/2-x)+1)] = 0

        
    def display(self):
        for i in range (len(self.test)):
           for j in range (len(self.test[i])):
               print "%s" % self.test[i][j],
           print ""
    
    


A = Shape()
A.set_edge(7)
A.set_pattern(1)
A.display()