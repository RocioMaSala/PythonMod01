def ft_plant_factory():
    class Plant:
        def __init__(self, name, height, age, growth_type):
            self.name = name
            self.height = height
            self.strtage = age
            self.totalgrowth = 0
            self.growth_type = growth_type

        def show(self):
            h = round(self.height, 2)
            print(f"Created: {self.name}: {h}cm, {self.strtage} days old")

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

    plant1 = Plant("Rose", 25, 30, "medium")
    plant2 = Plant("Oak", 200, 365, "fast")
    plant3 = Plant("Cactus", 5, 90, "slow")
    plant4 = Plant("Sunflower", 80, 45, "fast")
    plant5 = Plant("Fern", 15, 120, "medium")

    print("=== Plant Factory Output ===")

    for plant in [plant1, plant2, plant3, plant4, plant5]:
        plant.show()


ft_plant_factory()
