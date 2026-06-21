#given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
# in other words, one of the first string's permutations is the substring of the second string.
#'ab' vs 'edghbaoi'


s1 = "ab"

s2 = "adghbaoi"

def premutation(s1,s2):
   
    perm = {}
    window = {}
    if s1 == s2 :
        return True
   
    # Compare first two letters

    for i in s1:
        perm[i] = perm.get(i,0) +1
    
    for i in s2[:len(s1)]:
        window[i] = window.get(i,0) + 1

    
  
    
    for i in range(len(s1),len(s2)):
        new = s2[i]
        old = s2[i - len(s1)]

        window[new] = window.get(new,0) + 1
        window[old] -=1
        if window[old] == 0 : 
            del window[old]
    
        if window == perm :
            return True 
    
    return False

     
    


print(premutation(s1,s2))