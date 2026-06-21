letters = ['a','b','c']
letters.append('x')
letters.append('y')
print(letters)

letters.insert(1,'f')

print(letters)

letters.clear()
print(letters) 


letters = ['a','b','c','b']

letters.remove('b')
letters.remove('b')
print(letters)

letters = ['a','b','c','b']
removed = letters.pop()

print(letters)

print(removed)

letters = ['a','b','c']

letters[0] = 'x'
letters[1] = 'y'

letters = 'z'

print(letters)

print(type(letters))

