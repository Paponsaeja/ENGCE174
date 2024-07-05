person = {'name' : 'Alice', 'age' : 30, 'city': 'Newyork'}

# accesssing value 
print("Name: ", person['name']) # Alice

#updating values 
person[ 'age'] = 31 
print("updated age:", person['age'])

# iteracting through keys and values
for key, value in person.items():
    print(f"{key}: {value}")
    
# Alice 31 Newyork
