#Incomplete
def string_match(P,T):
    n = len(T)-1
    m = len(P)-1
    match = []
    
    for i in range(n-m):
        j = 0
        while (j<m) and (P[j]==T[i+j]):
            j = j+1
        if j==m:
            match.append(i)
    return -1
