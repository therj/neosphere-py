from collections import namedtuple
individual = namedtuple("ndividual", "name age height")
user = individual(name="Homer", age=37, height=178)
print(user)
# print(user[name])
