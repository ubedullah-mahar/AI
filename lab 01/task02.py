# TASK 02:
# This task demonstrates the creation and manipulation of
# different data structures in Python: list, tuple, and set.
# It also shows how to convert between these data structures.

# Creating a list of city names
cities_list = ["sukkur", "ghotki", "karachi", "larkana", "khairpur"]

# Creating a tuple of country names
countries_tuple = ("pakistan", "india", "england", "england", "spain")

# Creating a set of language names
languages_set = {"sindhi", "urdu", "punjabi", "balochi", "pashto"}

# Adding an element to the list
cities_list.append("karachi")

# Accessing an element from the tuple using index
print("Element at index 3 in tuple:", countries_tuple[3])

# Adding a new element to the set
languages_set.add("english")

# Converting list to set (removes duplicate values)
cities_set = set(cities_list)
print("Converted list to set:", cities_set)

# Converting set to list
languages_list = list(languages_set)
print("Converted set to list:", languages_list)

# Printing all data structures
print("Cities List:", cities_list)
print("Countries Tuple:", countries_tuple)
print("Languages Set:", languages_set)
