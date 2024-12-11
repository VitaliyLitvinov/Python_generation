city_1 = input()
city_2 = input()
city_3 = input()
city = [city_1, city_2, city_3]
#print(min(city))
print(max(city, key=len))