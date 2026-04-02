
def ft_plant_growth():
    class Plant:
        def __init__(self, name, height, age, growth_type):
            self.name = name
            self.height = height
            self.strtage = age
            self.totalgrowth = 0
            self.growth_type = growth_type

        def show(self):
            print(f"{self.name}: {self.height:.2f}cm, {self.strtage} days old")

        def grow(self):
            if self.growth_type == "fast":
                growth = .8
            elif self.growth_type == "medium":
                growth = .5
            elif self.growth_type == "slow":
                growth = .2
            else:
                growth = 0
            self.height += growth
            self.totalgrowth += growth

        def age(self):
            self.strtage += 1

    plant1 = Plant("Rose", 25, 30, "fast")
# plant2 = Plant("Sunflower", 5, 10, "medium")
# plant3 = Plant ("Cactus", 3, 45, "slow")

    print("=== Garden Plant Registry ===")

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        for plant in [plant1]:
            plant.show()
            plant.grow()
            plant.age()

    for plant in [plant1]:
        print(f"Growth this week: {round(plant.totalgrowth, 2)}cm")


ft_plant_growth()
