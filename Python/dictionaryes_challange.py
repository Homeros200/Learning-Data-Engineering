# Create New Dict
#Keep only Pairs with string Values
#Convert Values to Uppercase
#Elegant and sort solution!

user = {'id': 1, 'name': 'John', 'age': 30, 'city': 'Berlin'}

# Create a new dictionary with uppercase keys and string values


user_str = {
    k.upper(): v.lower()
    for k ,v in user.items()
    if isinstance(v,str)
}


print(user_str)
