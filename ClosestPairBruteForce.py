import math

def closest_pair_problem(Points): #points is a list of sets
    n = len(Points)
    dmin = 100000000000
    index1 = 0
    index2 = 1
    for i in range(n-2):
        for j in range(i+1, n-1):
            dist = math.sqrt(((Points[i][0]-Points[j][0])**2)+((Points[i][1]-Points[j][1])**2))
            if dist < dmin:
                dmin = dist
                index1 = i
                index2 = j
    return dmin, (index1, index2)


Points = [(1,2),(3,5),(5,5),(7,24),(9,11),(10,34),(1,1)]
closest_pair_problem(Points)

