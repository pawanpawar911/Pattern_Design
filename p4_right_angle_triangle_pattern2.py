def RightAngleNumberPyramid2_BF(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end=" ")  
        print()
print("---Brute-Force---")
RightAngleNumberPyramid2_BF(5)


def RightAngleNumberPyramid2_OA(n):
    for i in range(1, n+1):
        mapp = " ".join([str(i)]*i)
        #mapp = " ".join([str(i) for j in range(1, i+1)])
        print(mapp)
print("---Optimal-Approach---")
RightAngleNumberPyramid2_OA(5)