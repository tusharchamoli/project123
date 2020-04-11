def add(n1, n2):
    return n1+n2

def sub(n2,n1):
    return n2-n1
    
def mul(n1, n2):
    return n1*n2/2
    
def div(n2,n1):
    return n2/n1


num1=int(input("Enter first numbers"))
num2=int(input("Enter second number"))

age=add(num1,num2)
height=sub(num2,num1)
weight=mul(num1, num2)
iq= div(num2,num1)

print(f"Your age is {age} and height is {height} your weight is {weight} and your iq level is{iq}")
print("here's a puzzle")

that= add(age, sub(height,mul(weight,div(iq,num1))))
print(that)
