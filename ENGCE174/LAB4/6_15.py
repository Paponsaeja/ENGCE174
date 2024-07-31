set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

#adding elemnent to set 
set1.add(5)

# removing element from a set 
set2.discard(6)

print("is set1 subset of set2?:", set1.issubset(set2))
print("is set2 a subset of set1 :", set2.issubset(set1))

