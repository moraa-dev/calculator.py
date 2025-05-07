my_list = []  # Initializing my_list

my_list.append(10) #appending value 10 to my_list
my_list.append(20) #appending value 20 to my_list
my_list.append(30) #appending value 30 to my_list
my_list.append(40) #appending value 40 to my_list

my_list.insert(2, 15)  #inserting value 15 at index 2
my_list.extend([50, 60, 70]) #extending my_list with elements 50, 60, 70
my_list.pop(7) #removing element at index 7
my_list.sort() #sorting the my_list in ascending order

print(my_list) #displaying the results

my_list_30 = my_list.index(30) #finding element 30 via index
print (my_list_30) #displaying the value of element in index 
