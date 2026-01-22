# TASK 03:
# This task demonstrates the use of lists, tuples, and sets
# to store student marks. It also shows how to calculate
# total and average marks using a loop, check element existence,
# and modify a set.

# Student information
name = "Ubedullah"
roll_number = 592
percentage = 98.9

# Marks stored in different data structures
marks_list = [89, 67, 78, 69, 90]
marks_tuple = (89, 67, 78, 69, 90)
marks_set = set(marks_list)

# Calculating total and average marks
total_marks = 0
for mark in marks_list:
    total_marks += mark

average_marks = total_marks / len(marks_list)

print("Total marks:", total_marks)
print("Average marks:", average_marks)

# Checking if a specific value exists in the tuple
print("Is 85 present in tuple?", 85 in marks_tuple)

# Adding a new mark to the set
marks_set.add(99)

# Displaying marks from all data structures
print("Marks in list:", marks_list)
print("Marks in tuple:", marks_tuple)
print("Marks in set:", marks_set)
