# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def add_star(string):
    if len(str(string)) == 1:
        return string
    if string[0]:
        return string[:1] + "*" + add_star(string[1:])

print(add_star("attila"))