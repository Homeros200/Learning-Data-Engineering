import json

with open("classes/data/egypt.json") as country_file:
    file_data = json.load(country_file)


#print(file_data["max_temp"])


class CountryData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_data = self.read_data()
        self.country = self.file_data["Country"]
        self.max_temp = self.file_data["max_temp"]
        self.min_temp = self.file_data["min_temp"]

    def read_data(self):
        with open(self.file_path, "r") as country_file:
            return json.load(country_file)
        
    def is_comfortable(self):
        return self.max_temp - self.min_temp > 10
        
class CountryDataWithSunDays(CountryData):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.sunny_days = self.file_data["sunny_days"]

    def is_comfortable(self):
        return self.max_temp - self.min_temp + self.sunny_days > 10

class one_new_parameter(CountryDataWithSunDays):
    
    def __init__ (self, file_path):
        super().__init__(file_path)
        self.nice_bitches = self.file_data["nice_bitches"]



    def is_comfortable(self):
        return self.max_temp - self.min_temp + self.sunny_days + self.nice_bitches> 19




  


egypt = CountryData("classes/data/egypt.json")
sweden = CountryDataWithSunDays("classes/data/sweden.json")
germany = one_new_parameter("classes/data/germany.json")
#print(egypt.file_data)
#print(egypt.max_temp)
#print(egypt.min_temp)
#print(egypt.country)

#print(sweden.file_data)
#print(sweden.max_temp)
#print(sweden.min_temp)
#print(sweden.country)
#print(sweden.sunny_days)

print(germany.nice_bitches)

