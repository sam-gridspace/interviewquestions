import numpy as np 

class matrix(object):
    def __init__(self, values, M, N):
        self.matrix = values
        self.M = M
        self.N = N

        self.l = M * N

    def insert_and_push_values(self, position, value, check):
        check[position] = 1

        row = position/self.M
        col = position%self.M

        row_new = col
        col_new = row

        position_new = row_new * self.N + col_new
        pushed_value = self.matrix[position_new]
        self.matrix[position_new] = value
        if check[position_new] == 0:
            self.insert_and_push_values(position_new, pushed_value, check)

        

    def transpose(self):
        check = np.array([0]*self.l)
        for i in range(self.l):
            if check[i] == 0:                
                self.insert_and_push_values(i, self.matrix[i], check)

        Mtmp = self.M
        self.M = self.N
        self.N = Mtmp

    def __str__(self):
        s = ''
        print "row=", self.M, "column=", self.N
        for i in range(self.N):
            for j in range(self.M):
                s += str(self.matrix[i*self.M+j])+' '
            s += '\n'
        return s
                

if __name__=="__main__":
    m=matrix([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 4, 5)
    print m
    m.transpose()
    print m
    