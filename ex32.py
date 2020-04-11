count=[1,2,3,4,5,6]
fruits=["orange", "apple", "mango", "pears", "apricots"]
change=[1,"pennies",2, "dimes", 3, "quarters"]

for numbers in count:
    print(f"This is count {numbers}")
    
for fruit in fruits:
    print(f"This is {fruit}")
    
for i in change:
    print(f"I got {i}")
    
elements=[]

for i in range(0, 6):
    print(f"adding {i} to the list")
    elements.append(i)
    
for i in elements:
    print(f"I got {i}")

# 2 D list

couts= [[1,2,3], [2,3,7], [4,3,1]]

for i in couts[1]:
    print(f"I got {i}")