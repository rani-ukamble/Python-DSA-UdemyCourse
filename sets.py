my_set = {11, 2, 3, 4, 5}

s1 = set([1,2,3,4,5])

my_set.add(6)

my_set.update([7,8,9]) #add multiple elements simultaneously

print(my_set)

my_set.remove(11)

print(my_set)

s2 = {3, 4, 5, 6}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.union(s2))


if 2 in s1:
    print("found")  



def longest_consecutive_sequence(lst):
    if not lst:
        return 0 
        
    lst = list(set(lst))
    lst = sorted(lst)
    curr_streak = 1 
    longest_streak = 1 
    
    for i in range(1, len(lst)):
        # if lst[i]!=lst[i-1]:
        if lst[i]==lst[i-1]+1:
            curr_streak+=1
        else:
            longest_streak = max(longest_streak, curr_streak)
            curr_streak = 1
    return max(longest_streak, curr_streak)
            



print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""