# ex using sets for unique operations

# finding unique element from multiple lists 
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
list3 = [5,6,7,8,9]

unique_elements = set(list1).union(set(list2)).difference(set(list3))
print("Unique element:", unique_elements)