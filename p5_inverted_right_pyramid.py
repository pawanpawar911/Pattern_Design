def InvertedRightPyramid_BF(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()
print("---Brute-Force---")
InvertedRightPyramid_BF(5)


def InvertedRightPyramid_OA(n):
    for i in range(n, 0, -1):
        print(i* "* ")
print("---Optimal-Approach---")
InvertedRightPyramid_OA(5)