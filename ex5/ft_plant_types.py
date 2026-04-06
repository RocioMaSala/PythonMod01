class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        h = self.height
        print(f"{self.name}: {h:.1f}cm, {self.age} days old")         
    

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str)-> None:
        super().__init__(name, height, age)
        self.color = color
    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
    def bloom (self) -> None:
        print (f"{self.name} has not bloomed yet")
        print ("[asking the rose to bloom]")
        super().show()
        print(f"Color: {self.color}")
        print (f"{self.name} is blooming beautifully!\n")

    
class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float)-> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}")
    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self.height:.1f}cm long and {self.trunk_diameter}cm wide.")

class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str)-> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0
    def show(self)-> None:
        super().show()
       
        
def ft_plant_types()-> None:

    flower = Flower("Rose", 15, 10, "red")
    tree = Tree("Oak", 200, 365, 5)
    vegetable = Vegetable("Tomato", 5, 10, "April")

    print("=== Garden Plant Types ===")
    print("=== Flower") 
    flower.show()
    flower.bloom()
    print()

    print("=== Tree")
    tree.show()
    tree.produce_shade()
    print()

    

#

if __name__ == "__main__":
    ft_plant_types()