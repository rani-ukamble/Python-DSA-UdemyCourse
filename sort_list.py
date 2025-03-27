def bubble_sort(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst 

def selection_sort(lst):
    for i in range(len(lst)-1):
        mini_index = i
        for j in range(i+1, len(lst)):
            if lst[mini_index] > lst[j]:
                mini_index = j 
        if i!=mini_index:
            temp = lst[i]
            lst[i] = lst[mini_index]
            lst[mini_index] = temp 
    return lst

def insertion_sort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i-1
        while temp < lst[j] and j>-1:
            lst[j+1] = lst[j]
            lst[j] = temp
            j -= 1
    return lst

lst = [4, 2, 6, 5, 1, 3]
print(insertion_sort(lst))