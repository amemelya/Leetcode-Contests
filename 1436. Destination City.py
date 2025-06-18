class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = {}

        for a,b in paths:
            cities[a] = b
        city = paths[0][0]
        while cities.get(city,0):
            city = cities.get(city,0)  
        return city
        
