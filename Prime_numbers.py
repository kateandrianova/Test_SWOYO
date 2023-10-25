def prime_numbers(low, high):
    prime_numbers = []
    low = str(low)
    high = str(high)
    
    if (low.isdigit() or (low[:1] == '-' and low[1:].isdigit())) and (high.isdigit() or (high[:1] == '-' and high[1:].isdigit())):
        low = int(low)
        high = int(high)
        
        if low > high:
            low, high = high, low 
            
        for i in range(low, high + 1):
            k = 0     
            
            if i <= 1:
                k = 1
                
            for j in range(2, i):
                if i % j == 0:
                    k += 1
                    
                if k > 0:
                    break
                
            if k == 0:
                prime_numbers.append(i)
                
    return prime_numbers

