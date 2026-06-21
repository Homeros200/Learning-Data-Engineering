#given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
# in other words, one of the first string's permutations is the substring of the second string.
#'ab' vs 'edghbaoi'


s1 = "ab"
s2 = "edghbaoi"


def contains_permutation(s1, s2):
    if len(s1) > len(s2):
        return False

    count1 = {}
    window = {}
    
    # build frequency for s1
    for c in s1:
        count1[c] = count1.get(c, 0) + 1
    
    # build first window
    for c in s2[:len(s1)]:
        window[c] = window.get(c, 0) + 1
        
    if window == count1:
        return True
    
    # slide window
    for i in range(len(s1), len(s2)):
        new_char = s2[i]
        old_char = s2[i - len(s1)]
        
        window[new_char] = window.get(new_char, 0) + 1
        window[old_char] -= 1
        
       
        if window[old_char] == 0:
            del window[old_char]

        if window == count1:
            return True
        
    return False


print(contains_permutation(s1, s2))
    


















