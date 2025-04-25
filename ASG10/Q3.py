'''
3.A magic square is an N×N grid of numbers in which the entries in each row, column and
main diagonal sum to the same number (equal to N(N^2+1)/2). Create a magic square for
N=4, 5, 6, 7, 8
'''


import numpy as np



def magicSquare(n):
    if n%4==0:
        ms=np.arange(1,n*n+1).reshape(n,n)
        for i in range(n):
            for j in range(n):
                if i%4==j%4 or i%4+j%4==3:
                    continue
                else:
                    ms[i,j]=n*n+1-ms[i,j]

    elif n%4==2:
        half_n = n // 2
        sub_square_size = half_n * half_n
        sub_square = magicSquare(half_n)
        ms = np.zeros((n, n), dtype=int)
        
        for i in range(half_n):
            for j in range(half_n):
                ms[i, j] = sub_square[i, j]
                ms[i + half_n, j + half_n] = sub_square[i, j] + 3 * sub_square_size
                ms[i, j + half_n] = sub_square[i, j] + 2 * sub_square_size
                ms[i + half_n, j] = sub_square[i, j] + sub_square_size
        
        k = (n - 2) // 4
        for i in range(half_n):
            for j in range(k):
                ms[i, j], ms[i + half_n, j] = ms[i + half_n, j], ms[i, j]
                ms[i, j + half_n + k], ms[i + half_n, j + half_n + k] = ms[i + half_n, j + half_n + k], ms[i, j + half_n + k]


        
    else:
        #Siamese method
        ms=np.zeros((n,n))
        i,j=0,n//2
        for num in range (1,n*n+1):
            ms[i][j]=num

            iNew,jNew=(i-1)%n,(j+1)%n
            if ms[iNew][jNew]!=0:
                iNew,jNew=i+1,j
            
            i,j=iNew,jNew

    return ms


n=int(input("enter the order of magic square: "))
print(magicSquare(n))