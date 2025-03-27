def remove_element(nums, val):
    i = 0
    while i<len(nums):
        if nums[i]==val:
            nums.pop(i)
        else:
            i+=1
    return len(nums) 


def remove_duplicates(lst):
    if not lst:
        return 0 
    k = 1 
    for i in range(1, len(lst)):
        if lst[i]!= lst[i-1]:
            lst[k]=lst[i]
            k+=1 
    return k 


def max_profit(prices):
    max_profit = 0 
    min_profit = float('inf')
    
    for price in prices:
        if price<min_profit:
            min_profit = price
        elif price - min_profit > max_profit:
            max_profit = price - min_profit 
    return max_profit
                    
            
        
        
        
    
    


prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Test with mixed prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------") 




def rotate(nums, k):
    while k:
        ele = nums.pop()
        nums.insert(0, ele)
        k-=1 
    return nums
    
    


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)


"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""


# Kadane's algorithm
def max_subarray(lst):
    if not lst:
        return 0
    max_curr = lst[0]
    max_global = lst[0] 
    
    for i in range(1, len(lst)):
        max_curr = max(lst[i], lst[i]+max_curr)
        max_global = max(max_global, max_curr) 
    return max_global