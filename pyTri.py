import math

def firstVersion(row):

    print("\n\nThis is the first Version (the dirty one")
    triangle = []

    for n in range(row):
        triangle.append([])
        triangle[n].append(1)

        for r in range(n+1):

            try:
                triangle[n].append(triangle[n-1][r]+triangle[n-1][r+1])
        
            except IndexError:
                pass

            #print(str(n) + " " + str(r))
            #triangle[n][r] = triangle[n][r] = triangle[n-1][r-1]+triangle[n-1][r]
        

        triangle[n].append(1)


    triangle.insert(0,[1])

    for i in range(row):
        print(triangle[i])

def combVersion(row):
    
    print("\n\nThis is the Combinations Version")
    triangle = []

    for n in range(row):
        triangle.append([])
        for r in range(n+1):
            triangle[n].append(int(math.factorial(n)/(math.factorial(n-r)*(math.factorial(r)))))
        
    for i in range(row):
        print(triangle[i])

def secondVersion(row):

    print("\n\nThis is the second Version (our actual intention at the first attempt!)")

    triangle = []
    
    for n in range(row):
        triangle.append([])
        for r in range(n+1):
            if n-1>=0 and r-1>=0:
                triangle.insert(n, triangle[n-1][r-1]+triangle[n-1][r])
            else:
                triangle.insert(n, 1)
            
        
    for i in range(row):
        print(triangle[i])


row = int(input("How many rows? : "))
firstVersion(row)
combVersion(row)
secondVersion(row)


