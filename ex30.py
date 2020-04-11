people=30
cars=40
trucks=15

if people<cars:
    print("maybe we should take the cars")
elif people>cars:
    print("We should not take the cars")
else:
    print("we cant decide")
    
if trucks>cars:
    print("There are too many trucks")
elif trucks<cars:
    print("May be we could take the trucks")
else:
    print("We still can't decide")
    
if people>trucks:
    print("Alright, let's just take the trucks")
else:
    print(" Fine let's stay at home then")
    