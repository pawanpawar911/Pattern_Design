def RightAngleNumberPyramid_BF(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")  
        print()
print("---Brute-Force---")
RightAngleNumberPyramid_BF(5)


def RightAngleNumberPyramid_OA(n):
    for i in range(1, n+1):
        mapp = " ".join(map(str, range(1, i+1)))
        print(mapp)
print("---Optimal-Approach---")
RightAngleNumberPyramid_OA(5)