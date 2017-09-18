# Create a method that decrypts reversed-lines.txt
def reversed(file_name):
    reverse = ""
    with open(file_name, "r") as f:
        text = f.read()
        reverse += (text[::-1])
        print(reverse)
reversed("reversed-lines.txt")