import json

cities = {
  "Agra": 50000,
  "Chennai": 110000,
  "Mumbai": 200000
}

with open("cities.json", "w") as f:
  json.dump(cities, f, indent=4, sort_keys=True)
  
with open("cities.json", "r") as f:
  data = json.load(f)
  print(type(data), data)  
  
new_city = input("Enter a city: ")    
new_population = int(input("Enter its population: "))   

data[new_city] = new_population

with open("cities.json", "w") as f:

  json.dump(data, f, indent=5, sort_keys=True) 



