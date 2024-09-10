
def my_sum(*args):
    total = 0 
    
    
    for arg in args:
        if isinstance(arg, list):  
            total += my_sum(*arg)  
        else:
            total += arg 
    return total

