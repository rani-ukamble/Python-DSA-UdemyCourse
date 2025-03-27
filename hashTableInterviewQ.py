def item_in_common(list1, list2):
    # for i in list1:
    #     for j in list2:
    #         if i==j:
    #             return True
    # return False

    mydict = {}
    for i in list1:
        mydict[i] = True
    for j in list2:
        if j in mydict:
            return True
    return False

# list1 = [1, 2, 3]
# list2 = [4, 5, 3]
# print(item_in_common(list1, list2)) 


def find_duplicates(nums):
    ans = []
    dicti = {}
    for num in nums:
        if num in dicti:
            dicti[num]+=1 
        else:
            dicti[num] = 1 
        
    for j in dicti:
        if dicti[j]>1:
            ans.append(j)
    return ans

# print ( find_duplicates([1, 2, 3, 4, 5]) )
# print ( find_duplicates([1, 1, 2, 2, 3]) )
# print ( find_duplicates([1, 1, 1, 1, 1]) )
# print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
# print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
# print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
# print ( find_duplicates([]) )

"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""


def first_non_repeating_char(str):
    d = {}
    ans = ""
    for i in str:
        if i in d:
            d[i]+=1 
        else:
            d[i] = 1
    for key in d:
        if d[key]==1:
            return key
        
# print( first_non_repeating_char('leetcode') )
# print( first_non_repeating_char('hello') )
# print( first_non_repeating_char('aabbcc') )

"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

""" 


def group_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word))
        # print(f"Word: {word}, Sorted: {sorted_word}")  # Debugging print statement
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
        # print(f"Anagrams so far: {anagrams}")  # Debugging print statement
    return list(anagrams.values())

# print("1st set:")
# print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# print("\n2nd set:")
# print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

# print("\n3rd set:")
# print(group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]))

""" 
Expected Output:
1st set:
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

2nd set:
[['abc', 'cba', 'bac'], ['foo'], ['bar']]

3rd set:
[['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]
"""



def two_sum(nums, target):
    # for i in range(len(nums)):
    #     for j in range(1, len(nums)):
    #         if nums[i]+nums[j]==target:
    #             return [i, j]
    # return []
    nums_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_to_index:
            return [nums_to_index[complement], i]
        else:
            nums_to_index[num] = i
    return []        

print("\n\n")      
# print(two_sum([5, 1, 7, 2, 9, 3], 10))  
# print(two_sum([4, 2, 11, 7, 6, 3], 9))  
# print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
# print(two_sum([1, 3, 5, 7, 9], 10))  
# print ( two_sum([1, 2, 3, 4, 5], 10) )
# print ( two_sum([1, 2, 3, 4, 5], 7) )
# print ( two_sum([1, 2, 3, 4, 5], 3) )
# print ( two_sum([], 0) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 4]
    [1, 3]
    [0, 3]
    [1, 3]
    []
    [2, 3]
    [0, 1]
    []

"""





def subarray_sum(nums, target):
    # for i in range(len(nums)):
    #     sum = 0
    #     for j in range(i, len(nums)):
    #         sum+=nums[j]
    #         if sum == target:
    #             return [i, j]
    # return []

    commulative_sum = 0
    sum_to_index_dict = {0: -1}  # at -1 index , commulative sum = 0
    for i, num in enumerate(nums):
        commulative_sum += num 
        if (commulative_sum-target) in sum_to_index_dict:
            return [sum_to_index_dict[commulative_sum- target]+1, i]
        sum_to_index_dict[commulative_sum] = i
    return []



# nums = [1, 2, 3, 4, 5]
# target = 9
# print ( subarray_sum(nums, target) )

# nums = [-1, 2, 3, -4, 5]
# target = 0
# print ( subarray_sum(nums, target) )

# nums = [2, 3, 4, 5, 6]
# target = 3
# print ( subarray_sum(nums, target) )

# nums = []
# target = 0
# print ( subarray_sum(nums, target) )

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""





def subarray_sum(nums, target):
    # for i in range(len(nums)):
    #     sum = 0
    #     for j in range(i, len(nums)):
    #         sum+=nums[j]
    #         if sum == target:
    #             return [i, j]
    # return []
    
    commulative_sum = 0
    csum_to_index= {0:-1} #at -1 index , commulative sum = 0
    for i, num in enumerate(nums):
        commulative_sum += num 
        if (commulative_sum - target) in csum_to_index:
            return [csum_to_index[commulative_sum-target]+1, i]
        csum_to_index[commulative_sum] = i
    return []
    
    
            
    
            
        




nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""


