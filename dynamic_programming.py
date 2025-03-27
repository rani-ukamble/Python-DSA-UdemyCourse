# counter = 0

# def fib(n):
#     global counter 
#     counter+=1  #function calls calculated
#     if n==0 or n==1:
#         return n 
    
#     return fib(n-1) + fib(n-2) 


# ###############
# Iterative solution  : Bottom up

# counter = 0

# def fib(n):
#     global counter 
#     counter+=1 

#     fib_list = [0, 1]
#     for i in range(2, n+1):
#         next_fib = fib(i-1) + fib(i-2) 
#         fib_list.append(next_fib) 
#     return fib_list[n]



 


# ###############

# Memoization 


memo = [None]*100 
counter = 0 

def fib(n):
    global counter 
    counter+=1  #function calls calculated

    if memo[n] is not None:
        return memo[n]
    if n==0 or n==1:
        return n 

    memo[n] = fib(n-1) + fib(n-2)  

    return memo[n]  



n=7 

print(fib(n))
print(counter)

