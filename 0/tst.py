def mul(A,B):
    A_columnSize = len(A(0))
    B_rowSize = len(B)
    
    if A_columnSize!= B_rowSize:
        return []

    # output = [len(A):len(B(0))]
    output = []
    for i in range(len(A)):
        for j in range(len(A(0))):
            for y in range(len(B(0))):
                for x in range(len(B)):
                    output[i,y] = A[i,j]*B[x,y]

    return output





A = [[1, 0, 0],
[0, 0, 3],
[0, 2, 0]]

B = [[1, 1],
[0, .5],
[2, 1/3.0]]

C = [[ 1, 0, 0 ],
[ 0, 0, 0.5],
[ 0, 1/3.0, 0]]

print(mul(A,B))
print(mul(B,A))
print(mul(A,C))