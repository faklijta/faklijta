# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

my_file = str("my-file.txt")

def count_lines(name):
    try:
        fr = open(name, "r")
        text = fr.read()
        num_lines = sum(1 for line in open(name)) 
        print(num_lines)
        fr.close()
    except FileNotFoundError:
        return 0

count_lines(my_file)