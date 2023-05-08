countries = ['United Kingdom', 'Ghana', 'Nigeria', 2, True, 'Congo']
print(countries)
print(countries[2][1])
print(countries[1:]) #removes first
print(countries[2:])
print(countries[1:3])
name = 12
print(type(countries))
print(type(name))
countries[0] = 'US'
print(countries)
print(countries[-1])
print(len(countries))

# list constructor
fruits = list(('Apple', 23, False))
print(fruits)