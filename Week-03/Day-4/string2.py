# Given a string, compute recursively a new string where all the 'x' chars have been removed.

def x_to_none(string,x):
    if x not in string:
        return string
    if string[0] == x:
        return "" + x_to_none(string[1:],x)
    return string[0] + x_to_none(string[1:],x)

print(x_to_none("alex","x"))