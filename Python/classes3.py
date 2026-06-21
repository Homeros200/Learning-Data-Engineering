class kid:
    
    def __init__(self, hight, weight, gender, collor):
        self.hight = hight
        self.weight = weight
        self.gender = gender
        self.collor = collor


class kid_add(kid):

    def __init__(self, hight, weight, gender, collor, country):
        super().__init__(hight, weight, gender, collor)
        self.country = country


alex = kid_add(5.0, 47, "male", "black", "Georgia")

print(alex.weight)
