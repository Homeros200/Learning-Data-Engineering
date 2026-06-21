# Keep only students with names starting with 'M'
students = [['Maria', 85],
            ['Kumar',90],
            ['Max',60]]

print(students[0][0][0] == 'M')

print(list(filter(lambda row : row[0][0] =='M',students)))


