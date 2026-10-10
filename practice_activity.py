class human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age 
        self.gender = gender
ob = human("Nehul",13,"Boy")
print("Human name is",ob.name)
print("Human age is",ob.age)
print("Human gender is {}".format(ob.gender))


