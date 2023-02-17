# class person:
#     pass
# print(person)

# p = person
# print(p)


# Use the __int__ constructor
class person:
    def __init__(self, name):
        self.name = name

# p = person('Andrew')
# print(p.name)
# print(p)


# class person:
#     def __init__(self, firstname, lastname, age, country, city):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.country = country
#         self.city = city

# p = person ("Andrew", "kimani", 20, "Kenya", "Nairobi")
# print(p.firstname)
# print(p.lastname)
# print(p.age)
# print(p.country)
# print(p.city)


# class person:
#     def __init__(self, firstname, lastname, age, country, city):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.country = country
#         self.city = city

#     def person_info(self):
#         return f'{self.firstname} {self.lastname} is {self.age} years old.He lives in {self.city}, {self.country}'

#     p = person ("Andrew", "Kimani", 20, "Kenya", "Nairobi")
#     print(p)


# class student(person):
#     pass

# s1 = student("Andrew", "kimani", 20, "Nairobi", "Kenya")
# s2 = student("Owen", "kamodho", 21, "Kiambu", "THika")
# print(s1.person_info())
# s1.add_skill('Javascript')
# s1.add_skill('Python')
# s1.add_skill('React')
# print(s1.skills)

# print(s2.person_info())
# s2.add_skill('Organizing')
# s2.add_skill('Marketing')
# s2.add_skill('Digital Marketing')
# print(s2.skills)

class Student(person):
    def __init__(self, firstname = "Andrew", lastname = "kimani", age = 20, country = "Kenya", city = "Nairobi", gender = "male"):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'she'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)
