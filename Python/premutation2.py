
def permutations(item):
    if len(item) == 0:
         return [[]]
        
    result = []
    
    for i in range(len(item)):
        current = item[i]
                 
        remaining = item[:i] + item[i+1:]
        
        
        for p in permutations(remaining):
            
            result.append([current] + p)
            
  
    return result
    


print(permutations('ab'))
# Example usage
#item = 'abc'
#print(permutations(item))

#print(permutations('abc'))