def check(n_str, k): 
    if int(n_str) % 3 != 0: return False 
    
    count = 0
    for i in n_str:
        if int(i) % 2 == 0: count += 1 
    if count == k: return True 
    return False 
    
n_str = input(); n = int(n_str)
k = int(input()) 

cond = check(n_str, k) 
while not cond:
    n += abs((n % 3) - 3); n_str = str(n) 
    cond = check(n_str, k)
    
print(n)
