input_str = "this is what I'm searching in","searching"
haystack = input_str[0]
needle = input_str[1]

def string_finder(haystack,needle):
    if needle in haystack:
        return haystack.find(needle)
    else:
        return "-1"

string_finder(haystack,needle)
print(string_finder(haystack,needle))