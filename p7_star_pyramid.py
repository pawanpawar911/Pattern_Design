def StarPyramid(N):
    for i in range(N):
        for j in range(N-i+1):
            print(" ", end ="")
        for j in range(2*i+1):
            print("*", end="")  
        for j in range(N-i+1):
            print(" ", end="")
        print()
print("---Brute-Force---")
StarPyramid(5)


def StarPyramid(N):
    for i in range(N):
        print((N-i+1) * " ", (2*i+1) * "*", (N-i+1) * " ")
print("---Optimal-Approach---")
StarPyramid(5)