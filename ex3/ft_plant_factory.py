class Plant:
    def __init__(self, name: str, height: float, age: int, growth_type: str) -> None:
        self.name = name
        self.height = height
        self.strtage = age
        self.totalgrowth: float = 0
        self.growth_type = growth_type

    def show(self)-> None:
        h = self.height
        print(f"Created: {self.name}: {h:.1f}cm, {self.strtage} days old")

    def grow(self)-> None:
        if self.growth_type == "fast":
            growth = 0.8
        elif self.growth_type == "medium":
            growth = 0.5
        elif self.growth_type == "slow":
            growth = 0.2
        else:
            growth = 0
        self.height += growth
        self.totalgrowth += growth

    def age(self) -> None:
        self.strtage += 1


def ft_plant_factory() -> None:
    plant1 = Plant("Rose", 25, 30, "medium")
    plant2 = Plant("Oak", 200, 365, "fast")
    plant3 = Plant("Cactus", 5, 90, "slow")
    plant4 = Plant("Sunflower", 80, 45, "fast")
    plant5 = Plant("Fern", 15, 120, "medium")

    print("=== Plant Factory Output ===")

    for plant in [plant1, plant2, plant3, plant4, plant5]:
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
