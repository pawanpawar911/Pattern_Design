def RecStarPattern_BF(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")  
        print()
print("---Brute-Force---")
RecStarPattern_BF(5)

def RecStarPattern_OA(n):
    for i in range(n):
        print(n * "* ")  
print("---Optimal-Approach---")
RecStarPattern_OA(5)