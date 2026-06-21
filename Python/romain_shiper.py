alphabet = "abcdefghijklmnopqrstuvwxyz"






def encript(message,number):
    result = []
    
    for i in message :
        
        if i in " ,.!?0123456789":
            result.append(i)
        else:
            i = i.lower()
            calculate = (alphabet.find(i)-number)%26
            calculate = alphabet[calculate] 
            result.append(calculate)
     
    return "".join(result)


print(encript('Hello69',20))





#nkrrump

def decript(message,number):
    result = []
    
    for i in message :
        
        if i in " ,.!?0123456789":
            result.append(i)
        else:
            i = i.lower()
            calculate = (alphabet.find(i)+number)%26
            calculate = alphabet[calculate] 
            result.append(calculate)
     
    return "".join(result)

nick = ('nkrru69',20)

print(nick)

