def ft_garden_security_system():
    class Plant:
        def __init__(self, name, height, age):
            self.name = name
            self._height = height
            self._age = age

        def show(self):
            h = round(self.get_height(), 1)
            print(f"Plant created: {self.name}: {h}cm, {self.get_age} days old")
    
    
    class flower(Plant):
        def __init__(self, name, height, age, color):
            super().__init__(name, height, age)
            self_color = color
        
        def bloom():
            print(f"[asking the {self.name} to bloom]")

    
    class tree(Plant):
        def __init__(self, name, height, age, trunk_diameter):
            super().__init__(name, height, age)
            self_trunk_diameter = trunk_diameter
        def produce_shade():
            print(f"[asking the {self.name} to produce shade]")

    class Vegetable(Plant):
        def __init__(self, name, height, age, harvest_season, nutritional_value):
            super().__init__(name, height, age)
            self_harvest_season = harvest_season
            self_nutritional_value = nutritional_value
        
            

    print("=== Garden Plant Types ===")
    
    type = Plant("Rose", 15, 10)

    for type in range [Type1, Type2, Type3]:




    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-15)
    plant.set_age(-5)
    print()
    plant.current_show()


ft_plant_types()