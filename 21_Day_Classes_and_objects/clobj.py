# class person:
#     pass
# print(person)

# p = person
# print(p)


# Use the __int__ constructor
class person:
    def __init__(self, name):
        self.name = name

p = person('Andrew')
print(p.name)
print(p)


class person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

p = person ("Andrew", "kimani", 20, "Kenya", "Nairobi")
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)


class person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old.He lives in {self.city}, {self.country}'

    p = person ("Andrew", "Kimani", 20, "Kenya", "Nairobi")
    print(p)