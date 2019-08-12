d = {"Key1": "Value1", "Key2": "Value2"}
d2 = {"Key1": "Value1"}

test = {"name": "Neosphere"}

print(test["name"])
print(test.get("name"))

print(d["Key1"])
planet_size = dict({"Earth": 40075, "Saturn": 378675, "Jupiter": 439264})


# Square brackets
print(planet_size["Earth"])


# get() function
print(planet_size.get("Saturn"))


# Create the dictionary and print
user = {"Name": "Christine", "Age": 23}
print(user)
# Update the user's age and print
user["Age"] = 24
print(user)
