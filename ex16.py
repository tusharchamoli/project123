from sys import argv
script, filename=argv

print(f"We are going to delete this {filename}")
print(f" if you don't want it press ctrl+c")
print(f"If you don't want that press enter")

prompt=input("?")
print("Opening the file")
print("We are making file object")
target=open(filename, 'w')

print("We are truncating the file")
target.truncate()

print("we are going to write into tis file")
print("Give three lines for input")

line1=input("Enter first line")
line2=input("Enter second line")
line3=input("Enter third line")

print("Writing in to this file")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print("and we close this")

target.close()


