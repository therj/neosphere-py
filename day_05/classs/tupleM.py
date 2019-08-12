weekdays = tuple(["Mon", "Tue", "Wed", "Thu", "Fri"])
weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")
print(type(weekdays))
# parentheses optional for multiple values.
print(weekdays)

weekends = ("Sat", "Sun")

# Tuple containing a list, list can be modified.
# Concatenate:
t = weekdays + weekends
print(t)
del t  # delete t
print(t)
