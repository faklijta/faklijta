# Open a file called "my-file.txt"
# Write your name in it as a single line
# If the program is unable to write the file,
# then it should print an error message like: "Unable to write file: my-file.txt"

my_file = "my-file.txt"

def write_name(source):
    try:
        my_file = open(source, "a")
        my_file.write("Tania")
        
    except FileNotFoundError:
        print("Unable to write this file: " + the_file_source)


write_name(my_file)