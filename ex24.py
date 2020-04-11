
print("You\'d wonder what \\ this\'ll do")
print("\n new lines and \t tabs")


poem="""
 \tThe lovely world
 with logic so firmly planted 
 cannot discern \n the needs of love 
 nor comprehend passion from intuition 
 and requires an explanation
 \n\t\twhere there is none. 
"""
print("----------------------------")
print(poem)
print("----------------------------")

def secret_formula(started):
    jelly_beans=500*started
    toffess=100*started
    icecreams=10*started
    return jelly_beans, toffess, icecreams
    

start_point=1000
jelly_beans, toffess, icecreams= secret_formula(start_point)
# we can also store multiple values in multiple variables but the return values must be equal to the no. of variables

print(f"we have {jelly_beans} jelly_beans , {toffess} toffess and {icecreams} icecreams")

