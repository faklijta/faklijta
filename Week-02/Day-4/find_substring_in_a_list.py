# Find the substring in the list

# Create a function that takes a string and a list of string as a parameter
# Returns the index of the string in the list where the first string is part of
# Returns -1 if the string is not part any of the strings in the list
string_list = ["this", "is", "what", "I'm", "searching", "in"]
text = "rching" 

def finder(text, string_list):
    text_index = []
    for i in range(len(string_list)):
        if text in string_list[i]:
            text_index.append(i)
    return text_index

print(finder(text, string_list))
