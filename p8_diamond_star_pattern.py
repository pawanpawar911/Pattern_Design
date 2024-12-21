def DiamondStarPyramid_BF(N):
    for i in range(N):
        for j in range(N-i-1):
            print(" ", end ="")
        for j in range(2*i+1):
            print("*", end="")  
        for j in range(N-i-1):
            print(" ", end="")
        print()
    for i in range(N, 0, -1):
        for j in range(N-i):
            print(" ", end ="")
        for j in range(2*i-1):
            print("*", end="")  
        for j in range(N-i):
            print(" ", end="")
        print()
print("---Brute-Force---")
DiamondStarPyramid_BF(5)

def StarPyramid_OA(N):
    #use concatation(+) to avoid the extra space between space (" ") and ("*")
    for i in range(N):
        print((N-i-1) * " " + (2*i+1) * "*" + (N-i-1) * " ")
    for i in range(N, 0, -1):
        print((N-i) * " " + (2*i-1) * "*" + (N-i) * " ")
print("---Optimal-Approach---")
StarPyramid_OA(5)