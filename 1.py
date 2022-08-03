x = 1
y = 2

#tuple
point = 1,2
print(point[0])
print(point[1])
print(point)

#list
cities = ['Wrocław', 'Warszawa', 'Poznań', 'Sopot']
print(cities[0])
print(cities[-1])

cities.append('Kraków')
cities.append('Katowice')
cities.append('Kołobrzeg')

print(cities)

cities.sort()

print(cities)

#dict

capitals = {
    'Poland': 'Warszawa',
    'Francja': 'Paris',
    'Germany': 'Berlin'
}

print(capitals['Germany'])
