inputstring = input("Enter a string:")
outputstring = ''
for i in inputstring:
    if i.isupper():
        o = i.lower()
    elif i.islower():
        o = i.upper()
    else:
        o = i
    outputstring = outputstring + o
    
print(outputstring)
    
