#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._stats = self.Statistics(self)

    def show(self) -> None:
        h = self._height
        print(f"{self._name}: {h:.1f}cm, {self._age} days old")
        self._stats.total_show()

    class Statistics:
        def __init__(self, plant) -> None:
            self._plant = plant
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0
            self._shade_calls = 0

        def total_growth(self) -> None:
            self._grow_calls += 1

        def total_age(self) -> None:
            self._age_calls += 1

        def total_show(self) -> None:
            self._show_calls += 1

        def total_shade_calls(self) -> None:
            self._shade_calls += 1

        def display_stats(self) -> None:
            print(f"[statistics for {self._plant._name}]")
            print(
                f"Stats: {self._grow_calls} grow,"
                f" {self._age_calls} age, {self._show_calls} show"
            )

    @staticmethod
    def age_greater_than_1(days) -> None:
        if days > 365:
            print(f"Is {days} days more than a year? -> True")
        else:
            print(f"Is {days} days more than a year? -> False")

    @classmethod
    def anonymous_plant(cls):
        return cls(name="Unknown plant", height=0, age=0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def bloom(self) -> None:
        print(f"[asking the {self._name.lower()} to grow and bloom]")
        self._bloomed = True

    def grow(self) -> None:
        self._height = self._height + 8
        self._stats.total_growth()


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seed_number = 0

    def number_seeds(self) -> None:
        print(f"Seeds: {self._seed_number}")
        self._seed_number = self._seed_number + 42

    def bloomseed(self) -> None:
        print(f"[make {self._name.lower()} grow, age and bloom]")
        self._bloomed = True

    def growandage(self) -> None:
        self._height = self._height + 30
        self._age = self._age + 20
        self._stats.total_growth()
        self._stats.total_age()


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._shade = 0
        self._stats = self.Treestats(self)

    def show(self) -> None:
        super().show()

        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        self._stats.total_shade_calls()
        print(f"[asking the {self._name.lower()} to produce shade]")
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self._trunk_diameter:.1f}cm wide."
        )

    class Treestats(Plant.Statistics):
        def __init__(self, plant) -> None:
            super().__init__(plant)

        def display_stats(self) -> None:
            super().display_stats()
            print(f"{self._shade_calls} shade")


def disp_statistics(plant) -> None:
    plant._stats.display_stats()


def ft_garden_analytics() -> None:

    flower = Flower("Rose", 15, 10, "red")
    tree = Tree("Oak", 200, 365, 5)
    seed = Seed("Sunflower", 80, 45, "yellow")
    anonymous = Plant.anonymous_plant()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.age_greater_than_1(30)
    Plant.age_greater_than_1(400)
    print()

    print("=== Flower")
    flower.show()
    disp_statistics(flower)
    flower.bloom()
    flower.grow()
    flower.show()
    disp_statistics(flower)
    print()

    print("=== Tree")
    tree.show()
    disp_statistics(tree)
    tree.produce_shade()
    disp_statistics(tree)
    print()

    print("=== Seed")
    seed.show()
    seed.number_seeds()
    seed.bloomseed()
    seed.growandage()
    seed.show()
    seed.number_seeds()
    disp_statistics(seed)
    print()

    print("=== Anonymous")
    anonymous.show()
    disp_statistics(anonymous)


if __name__ == "__main__":
    ft_garden_analytics()
