person = {'name': 'Alice', 'age' : 30}

#using get() method to handle missing keys 
city = person.get('city', 'Unknow')
print("city:",city) # unknow