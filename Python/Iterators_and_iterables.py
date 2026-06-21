letters = ['a','b','c','d']
new_list = []
for l in letters:
    new_list.append(l.upper())
    print(new_list)



letters = ['a','b','c']
print(enumerate(letters))

letters = ['a','b','c']

print(list(enumerate(letters,start= 1)))

for index, value in enumerate(letters):
    print(index,value)


letters = ['a','b','c']
print(list(reversed(letters)))
for l in reversed(letters):
    print(l)
