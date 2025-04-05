#create an empty list called my_list

my_list = []
print(f"my_list = {my_list}")

#2. Append the following elements to my_list: 10, 20, 30, 40. 

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"my_list = {my_list}")

#3. Insert the value 15 at the second position in the list.

my_list.insert(1, 15)
print(f"my_list = {my_list}")

#4. Extend my_list with another list: [50, 60, 70]
another_list = [50, 60, 70]
my_list.extend(another_list)
print(f"my_list = {my_list}")

#5. Remove the last element from the my_list.
my_list.pop()
print(f"my_list = {my_list}")

#6. sort my_list in ascending order.
my_list.sort()
print(f"my_list = {my_list}")

#7 find and print the indexof the value 30 in my_list.
try:
    index_of_30 = my_list.index(30)
    print(f"The index of 30 in my_list is: {index_of_30}")
except ValueError:
    print("The value 30 is not found in my_list")
