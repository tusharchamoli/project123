from sys import argv

script, from_file, to_file = argv

print(f"We have to copy contents from{from_file} to {to_file}")
print("""to do that we will make one file object and 
one in_file object to copy the contents from one filr in a temporary file""")
in_file=open(from_file)
in_data=in_file.read()

print(f"The size of the contents in first file is {len(in_data)}")

out_file=open(to_file, 'w')
out_file.write(in_data)

out_file.close()
in_file.close()
