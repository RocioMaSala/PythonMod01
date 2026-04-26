#!/usr/bin/env python3

class Plant:
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            growth_type: str) -> None:
        self.name = name
        self.height = height
        self.strtage = age
        self.totalgrowth: float = 0
        self.growth_type = growth_type

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.strtage} days old")

    def grow(self) -> None:
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

    def age(self) -> None:
        self.strtage += 1


def ft_plant_growth() -> None:
    plant1 = Plant("Rose", 25, 30, "fast")

    print("=== Garden Plant Registry ===")

    for i in range(1, 8):
        for plant in [plant1]:
            plant.show()
            print(f"=== Day {i} ===")
            plant.grow()
            plant.age()
    plant.show()
    for plant in [plant1]:
        print(f"Growth this week: {round(plant.totalgrowth, 2)}cm")


if __name__ == "__main__":
    ft_plant_growth()
