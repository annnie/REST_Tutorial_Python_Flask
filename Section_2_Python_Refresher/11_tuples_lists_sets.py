# list can be modified, in order
my_list = ["Alice", "Bob", "Catherine"]

# tuple - can't be modified, in order
my_tuple = ("Alice", "Bob", "Catherine")

# set cannot have duplicate elements, unordered
my_set = {"Alice", "Bob", "Catherine"}

#subscript notation - used for lists and tuples, accesses elements
print(my_list[0])
print(my_list[1])
print(my_list[2])

my_list[0] = "Smith"
print(my_list[0])

# add elements to a list
my_list.append("Jane")
print(my_list)

# remove from a list
my_list.remove("Bob")
print(my_list)

# add to a set
