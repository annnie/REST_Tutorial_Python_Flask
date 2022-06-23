friend_ages = {"Rolf": 24, "Adam": 50, "Ann": 26}  # any hashable type as key

print(friend_ages["Adam"])
print(friend_ages.keys())
print(friend_ages.values())

# List of Dictionaries
friends = [
    {"name": "Alice", "age": 24},
    {"name": "Sal",  "age": 50},
    {"name": "Sarah", "age": 27}
]

print(friends)

# student name to attendance percentage

student_attendance = {"Rolf": 90, "Adam": 66, "Ann": 100}

for student, attendance in student_attendance.items():
    print(f'{student}: {attendance}')

if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("Bob is not in this class")

attendance_values = student_attendance.values()
print(attendance_values)
print(sum(attendance_values) / len(attendance_values))