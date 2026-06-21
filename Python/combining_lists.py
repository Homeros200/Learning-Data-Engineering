#Combining

letters = ["a",'b','c']
numbers = [1,2,3]
comb = letters + numbers 
print(comb)
print(letters * 2 )
comb = [letters,numbers]
print(comb)
numbers.extend(letters)
print(letters)
print(numbers)
#Combining
letters = ['a','b','c']
numbers = [1,2,3,4]
comb = list(zip(letters,numbers,"Hi"))
print(comb)
id= [101,102,103]
names = ['Ali','Sara','John',]
print(list(zip(id,names)))