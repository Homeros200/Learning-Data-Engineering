# 1020
# Goal 1525


n = 1020
goal = 0
position = 1

while n > 0:

    digit = n % 10 
    if digit == 0:
        digit = 5
    
    
    goal += digit * position
    position *= 10
    n //= 10
print(goal)



