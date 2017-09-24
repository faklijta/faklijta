# Crate a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
#
def chess_table():
    for lines in range(8):
        if lines %2 ==0:
            print("% % % %")
        else:
            print(" % % % %")

chess_table()