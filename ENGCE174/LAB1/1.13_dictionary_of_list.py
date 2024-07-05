cities = {
    'Newyork': [32,25,30,28,35],
    'Los angeles': [75,68,72,70,80],
    'Chicago': [20,18,22,25,15]
}

#calculate average temperature for each city 
averages = {city:sum(temps) / len(temps) for city, temps in cities.items()}
print("Average temperature:", averages)

# Newyork : 30.0 , Los angeles : 73.0 , chicago : 20.0