def selection_sort(list1):
    n = len(list1)
    for i in range(n-2):
        min_idx = i
        for j in range(n-1):
            if list1[j] < list1[i]:
                min_idx = j
            temp = list1[min_idx]
            list1[min_idx] = list1[i]
            list1[i] = temp
    return list1
    
