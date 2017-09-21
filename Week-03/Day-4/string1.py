# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def x_to_y(string,x,y):
    if x not in string:
        return string
    if string[0] == x:
        return y + x_to_y(string[1:],x,y)
    return string[0] + x_to_y(string[1:],x,y)

print(x_to_y("maximilian","x","y"))
