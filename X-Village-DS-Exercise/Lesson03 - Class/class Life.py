class L():
    def set_map(self,n):
        self.list=[["*" for i in range(n)]for j in range(n)]
        
    def display(self):
        for i in range(len(self.list)):
            for j in range(len(self.list)):
                print (self.list[i][j],"\t", end = " ")
            print ("")
        print ("")
        
    def set_pattern(self,n):
        a=len(self.list)//2
        if n==1 and a>=1:
            if len(self.list)%2!=0:
                self.list[a-1][a-1:a+1]=[0,0,0]
                self.list[a][a-1]=0
                self.list[a+1][a]=0
        else:
            self.set_map(len(self.list))
            

#===============================
a=L()
a.set_map(7)
a.display()
a.set_pattern(1)
a.display()