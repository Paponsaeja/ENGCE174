name = [ "Alice", "Bob", "Charlie"]
ages = [25 , 30 ,35 ]
city = ["Newyork", "Los Angeles", "chicago"]

# using zip() for parallel interation 
for name, ages, city in zip( name, ages , city):
    print(f"{name} is {ages} years old and lives in {city}")