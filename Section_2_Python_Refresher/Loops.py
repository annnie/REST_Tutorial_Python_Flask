friends = ["Ann", "Alice", "Bobo"]

for friend in friends:
    print(f'{friend} is my friend!')

for friend in range(2):
    print(f'{friends[friend]} is my friend')


# grades
grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

# or use sum
total_sum = sum(grades)

print(total/amount)
print(total_sum/amount)
