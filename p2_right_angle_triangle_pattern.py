def RightAngleTrianglePattern_BF(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end=" ")  
        print()
print("---Brute-Force---")
RightAngleTrianglePattern_BF(5)


def RightAngleTrianglePattern_OA(n):
    for i in range(1, n+1):
        print(i * "* ")  
print("---Optimal-Approach---")
RightAngleTrianglePattern_OA(5)