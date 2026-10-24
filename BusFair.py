class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        final_fare = base_fare + (base_fare * 0.10)
        return final_fare

school_bus = Bus("School Bus", 12, 50)
print("Total Bus fare is:", school_bus.fare())
