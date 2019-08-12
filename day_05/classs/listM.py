x = [1, [2, [8, 9], 3], "Abc"]
print(x[1][1][0])


# test = list(1, 2, 3)

x.append("NewVal")
print(x)

x.extend([1, 2, 3])
week = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekends = ["Sat", "Sun"]
week.extend(weekends)
print(week)
print(x)

x.insert(1, "Ok")
print(x)

x.remove("Ok")
x.pop()

print(x)
x.pop(2)
print(x)
x.append("Ok")
x.append("Ok")
x.append("Ok")
op = x.count("Ok")
print("***********")

print(op)


print("***********")
print(x)
x.reverse()
print(x)
