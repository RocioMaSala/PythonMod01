#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        h = self.height
        print(f"{self.name}: {h:.1f}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!\n")
        else:
            print(f"{self.name} has not bloomed yet")

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to bloom]")
        self.bloomed = True


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = False

    def show(self) -> None:
        if self.shade is False:
            super().show()
            print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")
        else:
            print(
                f"Tree {self.name} now produces a shade of "
                f"{self.height:.1f}cm long and "
                f"{self.trunk_diameter:.1f}cm wide."
            )

    def produce_shade(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        self.shade = True


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def vage(self, growth) -> None:
        self.age = self.age + growth

    def grow(self, cm, growth) -> None:
        self.height = self.height + cm
        self.nutritional_value = self.nutritional_value + growth
        print(f"[make tomato grow and age for {growth} days]")


def ft_plant_types() -> None:

    flower = Flower("Rose", 15, 10, "red")
    tree = Tree("Oak", 200, 365, 5)
    vegetable = Vegetable("Tomato", 5, 10, "April")

    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower.show()
    flower.bloom()
    flower.show()
    print()

    print("=== Tree")
    tree.show()
    tree.produce_shade()
    tree.show()
    print()

    print("=== Vegetable")
    vegetable.show()
    vegetable.vage(20)
    vegetable.grow(42, 20)
    vegetable.show()


if __name__ == "__main__":
    ft_plant_types()
