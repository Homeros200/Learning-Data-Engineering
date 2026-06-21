def permute(lst):
    if len(lst) == 1:
        return [lst]

    result = []
    for i in range(len(lst)):
        current = lst[i]
        remaining = lst[:i] + lst[i+1:]

        for p in permute(remaining):
            result.append([current] + p)

    return result


lst = ['a', 'b', 'c']
perms = permute(lst)

print(perms)
    
    

