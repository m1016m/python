import random

from copy import deepcopy
   
class Matrix:
    X = []
    Y = []
    n = []


    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.X = nrows
        self.Y = ncols
        

    def add(self, m):
        """return a new Matrix object after summation"""
        for self.nrows in range(len(m)):
           for self.ncols in range(len(m[0])):
             result[self.nrows][self.ncols] = X[self.nrows][self.ncols] + Y[self.nrows][self.ncols]
 
        for r in result:
           print r
        print "======A+B======"
        print ""
    def sub(self, m):
        """return a new Matrix object after substraction"""
        for self.nrows in range(len(m)):
           for self.ncols in range(len(m[0])):
             result[self.nrows][self.ncols] = X[self.nrows][self.ncols] - Y[self.nrows][self.ncols]
 
        for r in result:
           print r
        print "======A-B======"
        print ""
    def mul(self):
        """return a new Matrix object after multiplication"""
        
        for  self.y in range(len(X)):
            for self.x in range(len(Y)):
                for self.i in range(len(result)):  
                      result[self.y][self.x] += (X[self.y][self.i]*Y[self.i][self.x]) 
            
        for r in result:
           print r
        print "======A*B======"
        print ""    
    def transpose(self):
        """return a new Matrix object after transpose"""
        self.n = len(result)
        result.reverse()
        
        for self.nrows in xrange(self.n):
            for self.ncols in xrange(self.nrows, self.n):
                result[self.nrows][self.ncols], result[self.ncols][self.nrows] = result[self.ncols][self.nrows], result[self.nrows][self.ncols]
        for r in result:
           print r     
    def display(self):
        """Display the content in the matrix"""
        pass

X = [[1,9,3],
    [4 ,7,6],
    [3 ,7,1]]

Y = [[9,0,6],
    [7,7,0],
    [2,5,5]]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
A = Matrix(X,Y)
A.add(X)
A.sub(X)
A.mul()
A.transpose()


