
all = []

for name in dir(__builtins__):
    if "Error" not in name:
        obj = getattr(__builtins__, name)
        print(name, type(obj))
        all.append(help(obj))

print(all)