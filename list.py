# Create an empty list called my_list.
my_list = []

# Append the following elements to my_list: 10, 20, 30, 40.

my_list.append (10)
print(my_list)

my_list.append (20)
print(my_list)

my_list.append (30)
print(my_list)

my_list.append (40)
print(my_list)

my_list.insert(2, 15)  # Insert 15 at index 2
print(my_list)

my_list.extend ([50, 60, 70]) # Extend my_list with another list: [50, 60, 70]
print(my_list)

my_list.pop (7) # Remove the last element from my_list.
print(my_list)

my_list.sort () # Sort my_list in ascending order.
print(my_list)

index_of_30 = my_list.index(30)  # Find and print the index of the value 30 in my_list.
print (index_of_30)
