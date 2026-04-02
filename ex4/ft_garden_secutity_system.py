def ft_garden_security_system():
    class Plant:
        def __init__(self, name, height, age, growth_type):
            self.name = name
            self._height = height
            self._age = age
            self.totalgrowth = 0
            self.growth_type = growth_type
            self.show()

        def show(self):
            h = round(self.get_height(), 1)
            print(f"Plant created: {self.name}: {h}cm, {self.get_age} days old")
            
        def current_show(self):
            h = round(self.get_height(), 1)
            print(f"Current state: {self.name}: {h}cm, {self.get_age()} days old")
        
        def get_height(self):
            return self._height
        
        def set_height(self, value):
            if value < 0:
                print(f"{self.name}: Error, height can't be negative")
                print("Height update rejected")
            else:
                self._height = value
                h = round(self._height, 2)
                print(f"Height updated: {h}cm")

        def get_age(self):
            return self._age
        
        def set_age(self, value):
            if value < 0:
                print(f"{self.name}: Error, age can't be negative")
                print("Age update rejected")
            else:
                self._age = value
                print(f"Age updated: {self._age} days")
        
        def grow(self):
            if self.growth_type == "fast":
                growth = .8
            elif self.growth_type == "medium":
                growth = .5
            elif self.growth_type == "slow":
                growth = .2
            else:
                growth = 0
            self.set_height(self.set_height() + growth)
            self.totalgrowth += growth

        def total_age(self):
            self.set_age (self.get_age() + 1)

    print("=== Garden Security System ===")
    
    plant = Plant("Rose", 15, 10, "medium")

    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-15)
    plant.set_age(-5)
    print()
    plant.current_show()


ft_garden_security_system()