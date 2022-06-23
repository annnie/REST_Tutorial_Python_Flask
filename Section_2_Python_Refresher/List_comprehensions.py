# List comprehensions
numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]

print(numbers)
print(doubled)

friends = ["Alice", "Sal", "Sarah"]
starts_s = []

# for loop approach
for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)

# list comprehension list
starts_s_comp = [friend for friend in friends if friend.startswith("S")]

print(starts_s_comp)

# creates a new list
print(id(starts_s_comp), id(friends))