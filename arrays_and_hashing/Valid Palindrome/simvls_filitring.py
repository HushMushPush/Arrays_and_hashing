#simb = chr(97) # символ a
#num = ord(simb) # число 97

def filitr(word):
    simvls = []

    for i in word:
        if 97 <= ord(i) <= 122:
            simvls.append(i)
        elif 65 <= ord(i) <= 90:
            simvls.append(chr(ord(i)+32))
    
    return simvls

print(filitr(input()))
