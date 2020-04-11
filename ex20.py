from sys import argv

script, input_file= argv

# to print what's written in the file on the console we can use filename.read()
def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print(line_count, f.readline()) #readline – Reads just one line of a text file. 
# this method is useful because after each iteration f.readline is bringing the head to the end of iterated line

current_file = open(input_file)
print("Print the whole file first")
print_all(current_file)
print("Now let's rewind and reach at the start")
rewind(current_file)
print("Now let's print the three lines along with the line numbers")
current_line=1
print_a_line(current_line, current_file)
current_line=2
print_a_line(current_line, current_file)
current_line=3
print_a_line(current_line, current_file)



