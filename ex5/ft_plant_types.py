#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        h = self._height
        print(f"{self._name}: {h:.1f}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!\n")
        else:
            print(f"{self._name} has not bloomed yet")

    def bloom(self) -> None:
        print(f"[asking the {self._name.lower()} to bloom]")
        self._bloomed = True


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._shade = False

    def show(self) -> None:
        if self._shade is False:
            super().show()
            print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")
        else:
            print(
                f"Tree {self._name} now produces a shade of "
                f"{self._height:.1f}cm long and "
                f"{self._trunk_diameter:.1f}cm wide."
            )

    def produce_shade(self) -> None:
        print(f"[asking the {self._name.lower()} to produce shade]")
        self._shade = True


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def vage(self, growth: int) -> None:
        self._age = self._age + growth

    def grow(self, cm: float, growth: int) -> None:
        self._height = self._height + cm
        self._nutritional_value = self._nutritional_value + growth
        print(f"[make {self._name.lower()} grow and age for {growth} days]")


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
