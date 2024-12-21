def HalfDiamondStarPyramid_BF(N):
    for i in range(N):
        for j in range(N):
            print(" ", end ="")
        for j in range(i+1):
            print("*", end="")  
        for j in range(N):
            print(" ", end="")
        print()
    for i in range(N-1, 0, -1):
        for j in range(N):
            print(" ", end ="")
        for j in range(i):
            print("*", end="")  
        for j in range(N):
            print(" ", end="")
        print()
print("---Brute-Force---")
HalfDiamondStarPyramid_BF(5)

def HalfDiamondStarPyramid_OA(N):
    #use concatation(+) to avoid the extra space between space (" ") and ("*")
    for i in range(N):
        print((N) * " " + (i+1) * "*" + (N) * " ")
    for i in range(N-1, 0, -1):
        print((N) * " " + (i) * "*" + (N) * " ")
print("---Optimal-Approach---")
HalfDiamondStarPyramid_OA(5)