from sys import argv
script, filename=argv

#file_open=open(filename)

print("Your file name is", filename)
print(filename.read())

print("Type the filename again")
file_gain=input(">")
txt_again=open(file_gain)
print(txt_again.read())