
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1} and arg2:{arg2}")
    
 
def print_two_again(arg1, arg2):
    print(f"arg1:{arg1} and arg2:{arg2}")
    
    
def print_one(arg1):
    print(f"arg:{arg1}")
    
    
    
print_two("tushar","chamoli")
print_two_again("tushar", "chamoli")
print_one("Tushar")
    