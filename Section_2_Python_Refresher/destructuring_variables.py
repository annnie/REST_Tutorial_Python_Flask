# destructuring variables
t = 5, 11  # this is a tuple, no brackes needed
x, y = t

print(x, y)

# students example
student_attendance = {"Rolf": 90, "Adam": 66, "Ann": 100}
print(student_attendance.items())
print(list(student_attendance.items()))  # list of tuples

# destructuring a in a for loop
for student, attendance in student_attendance.items():
    print(student, attendance)


# people example
# list of people, each entry is a tuple of 3 values
people = [("Rolf", 45, "Mechanic"), ("Adam", 66,
                                     "Artist"), ("Ann", 26, "Engineer")]

for name, age, career in people:
    print(name, age, career)