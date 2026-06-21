#Copying
letters = ['a','b','c']
letters_copy = letters
letters.pop()
letters_copy.append('z')
print('Original:',letters)
print('Copy:',letters_copy)
print("Shellow copy")
letters = ['a','b','c']
letters_copy = letters.copy()
letters_copy.append('z')
letters.pop()
print('Original:',letters)
print('Copy:',letters_copy)
print('Deep Copy')



import copy


matrix = [
    ['a','b'],   # Row 0
    ['c','d'],   # Row 1
       ]
matrix_copy = copy.deepcopy(matrix)
matrix.pop()
matrix_copy[0].append('z')
print('Original:', matrix)
print('Copy:    ', matrix_copy)


import copy


original = [
    ['a','b'],   # Row 0
    ['c','d'],   # Row 1
       ]

#Assigment

copy1 = original
print(original is copy1)

#shallow copy

copy2 = original.copy()

print("Same object?", original is copy2, "\n")
print("Shared Lists?", original[0] is copy2[0], "\n")

#Deep Copy

copy3 = copy.deepcopy(original)

print("Same object?", original is copy3, "\n")
print("Shared Lists?", original[0] is copy3[0], "\n")





