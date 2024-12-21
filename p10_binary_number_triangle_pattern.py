def BinaryNumberTrianglePattern_BF(N):
    #toggle 1 and 0
    for i in range(N):
        if i%2 == 0:
            start = 1
        else:
            stop = 0
        for j in range(i+1):
            print(start, end=" ")
            start = 1 - start
        print()
print("---Brute-Force---")
print(BinaryNumberTrianglePattern_BF(5))



def BinaryNumberTrianglePattern_OA(N):
    #toggle 1 and 0
    for i in range(1,N+1):
        row = []
        for j in range(i):
            row.append(str((i+j)%2))
        print(" ".join(row))
print("---Optimal-Approach---")
BinaryNumberTrianglePattern_OA(5)