filename = "test_file.txt"

fh = open(filename, "r")
print(dir(fh))

for line in fh.readlines():
 	print(line, end="")