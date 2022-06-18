###### Set Operations

set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9, 11}

print("set_one: ", set_one)  
print("set_two: ", set_two)

print("intersection: ", set_one.intersection(set_two))  # {1, 3, 5}

print("union: {1, 2}.union({2, 3)", {1, 2}.union({2, 3}))  # {1, 2, 3}

print("difference: ", {1, 2, 3, 4}.difference({2, 4}))  # {1, 3}