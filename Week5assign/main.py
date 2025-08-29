
# ================================
# Activity 1: Design Your Own Class
# ================================

# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        """Return device details."""
        return f"{self.brand} {self.model}"

# Child class inheriting Device
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)   # Inherit from Device
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        """Simulate making a phone call."""
        return f"📞 Calling {number} from {self.model}..."

    def charge(self, percent):
        """Increase battery level by given percentage."""
        self.battery += percent
        if self.battery > 100:
            self.battery = 100
        return f"🔋 Battery charged to {self.battery}%"

# Test Activity 1
print("=== Activity 1: Smartphone Class ===")
phone1 = Smartphone("Samsung", "Galaxy S24", "256GB", 80)
phone2 = Smartphone("Apple", "iPhone 15", "128GB", 50)

print(phone1.device_info())      
print(phone1.make_call("0712345678"))
print(phone2.charge(30))
print()  # spacing


# ====================================
# Activity 2: Polymorphism Challenge
# ====================================

class Vehicle:
    def move(self):
        """Base method to be overridden."""
        pass

class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"

class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky"

class Boat(Vehicle):
    def move(self):
        return "⛵ Sailing on water"

# Test Activity 2
print("=== Activity 2: Polymorphism with Vehicles ===")
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
