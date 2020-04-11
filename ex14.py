from sys import argv
script, user_name= argv
prompt= ">"

print(f" Hi {user_name} I am {script}")
print(f"I want to ask you saome questions")
print(f"Do you like me {user_name}?")
likes=input(prompt)
print(f" what kind of computer do you have")
computer=input(prompt)
print(f"""
Alright, so you are {user_name} and you {likes}.
and you have {computer}.
OK thank you.
""")