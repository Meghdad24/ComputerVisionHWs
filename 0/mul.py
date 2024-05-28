def mul(A,B):
    A_iSize = len(A)
    A_jSize = len(A[0])
    B_iSize = len(B)
    B_jSize = len(B[0])
    
    if A_jSize!= B_iSize:
        return []

    output = []
    for Ai in range(A_iSize):
        row = []
        for Bj in range(B_jSize):
            element = 0
            for sharedIndex in range(A_jSize):
                element += A[Ai][sharedIndex] * B[sharedIndex][Bj]
            row.append(element)
        output.append(row)
            
    return output





# A = [[1,2,3],
# [4, 5, 6],
# [7, 8, 9]]

# B = [[1, 2],
# [3, 4],
# [5, 1/3.0]]

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

