cities={"hubli":1100000,"bangalore":1200000,"mysore":900000,"belgaum":800000}
for key,value in cities.items():
    print(key+":"+str(value) if value>1000000 else None)
    
    #filtered_cities = {key: value for key, value in cities.items() if value >= 1000000}
    #print(filtered_cities)