# ex Working with dictionaries 

# creating a dictionary of student s grades 
grades = {'Alice': 85 , 'Bob' : 92 , 'Charie' : 88 , 'David': 95 }

#accessing value using keys 
print("Bob grades :", grades['Bob'])

# adding a new ebtry 
grades['Eve'] = 99 

# Iterating through keys values 
for student, grade in grades.items():
    print(f"{student}: {grade}")
    
# Using get() method to avoid keyError 
print("Frank's grade:", grades.get('Frank', 'Grades not found'))