
"""
def check_odd(k):
    if k % 2 == 0:
        print("number is not odd", k)
        
    
check_odd(7)
"""

def prime(p):
    for i in range(2, p):
        baghimande = p % i
        if baghimande == 0:
            return "not prime"
    return "prime"    
prime(20)