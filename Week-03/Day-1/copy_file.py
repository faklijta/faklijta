# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful
import sys
file1 = (input("please add location what to copy: "))
file2 = (input("please add location where to copy: "))
def copy(file1,file2):
    try:
        with open(file1, "r") as f1:
            f1_text = f1.read()
        with open(file2, "w") as f2:
            f2.write(f1_text)
    except:
        return 0
copy(file1,file2)
