def InvertedNumberRightPyramid_BF(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print(j+1, end=" ")
        print()
print("---Brute-Force---")
InvertedNumberRightPyramid_BF(5)


def InvertedNumberRightPyramid_OA(n):
    for i in range(n, 0, -1):
        mapp = " ".join(map(str, range(1, i+1)))
        print(mapp)
print("---Optimal-Approach---")
InvertedNumberRightPyramid_OA(5)

"""
s = 1,2,3,4
res = map(int, s)
print(list(res))

def double(val):
    return val*2

res = list(map(double, s))
print(res)
"""