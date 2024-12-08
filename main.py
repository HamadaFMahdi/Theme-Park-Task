class Attraction:
    def __init__(self, name, capacity):
        self.__name = name  
        self.__capacity = capacity 

    def get_details(self):
        return f"Attraction: {self.__name}, Capacity: {self.__capacity}"

    def start(self):
        return "The attraction is starting."

 class ThrillRide(Attraction):
    def __init__(self, name, capacity, min_height):
        super().__init__(name, capacity)
        self.__min_height = min_height  

    def start(self):
        return f"Thrill Ride {self.get_details().split(',')[0].split(': ')[1]} is now starting. Hold on tight!"

    def is_eligible(self, height):
        return height >= self.__min_height

    class FamilyRide(Attraction):
    def __init__(self, name, capacity, min_age):
        super().__init__(name, capacity)
        self.__min_age = min_age  

    def start(self):
        return f"Family Ride {self.get_details().split(',')[0].split(': ')[1]} is now starting. Enjoy the fun!"

    def is_eligible(self, age):
        return age >= self.__min_age

class Staff:
    def __init__(self, name, role):
        self.__name = name  
        self.__role = role  

    def work(self):
        return f"Staff {self.__name} is performing their role: {self.__role}."

class Visitor:
    def __init__(self, name, age, height):
        self.__name = name  
        self.__age = age  
        self.__height = height  

    def ride(self, attraction):
        if isinstance(attraction, ThrillRide):
            eligible = attraction.is_eligible(self.__height)
        elif isinstance(attraction, FamilyRide):
            eligible = attraction.is_eligible(self.__age)
        else:
            eligible = False

        if eligible:
            return f"Visitor {self.__name} is eligible for the ride."
        else:
            return f"Visitor {self.__name} is not eligible for the ride."


dragon_coaster = ThrillRide("Dragon Coaster", 20, 140)
merry_go_round = FamilyRide("Merry-Go-Round", 30, 4)
visitor1 = Visitor("Alice", 5, 130)


print(visitor1.ride(dragon_coaster))  
print(visitor1.ride(merry_go_round))  


dragon_coaster = ThrillRide("Dragon Coaster", 20, 140)
merry_go_round = FamilyRide("Merry-Go-Round", 30, 4)
visitor1 = Visitor("Alice", 5, 130)


print(visitor1.ride(dragon_coaster))  
print(visitor1.ride(merry_go_round))  

