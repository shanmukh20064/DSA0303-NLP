import string
text="hello! i am shanmukh"
result=""
for ch in text:
    if ch not in string.punctuation:
        result=result+ch
print(result)
