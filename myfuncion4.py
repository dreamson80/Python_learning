def string_length(mystring):
    if type(mystring) == int:
        return "Sorry, integers don't have length"
    elif type(mystring) == float:
        return "Sorry, floats don't have length"
    else:
        return len(mystring)
mystring =  input("Enter your word: ")
print(string_length(mystring))
