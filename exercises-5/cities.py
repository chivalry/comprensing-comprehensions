cities = {'Israel': ['Jerusalem', 'Tel Aviv'],
		  'USA': ['Boston', 'New York', 'Chicago'],
		  'China': ['Beijing', 'Shanghai']}
print([(city, country)
	  for country, cities in cities.items()
	  for city in cities])