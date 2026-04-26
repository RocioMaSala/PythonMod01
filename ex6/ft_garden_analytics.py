#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.stats = self.Statistics(self)

    def show(self) -> None:
        h = self.height
        print(f"{self.name}: {h:.1f}cm, {self.age} days old")
        self.stats.total_show()

    class Statistics:
        def __init__(self, plant) -> None:
            self.plant = plant
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0
            self.shade_calls = 0

        def total_growth(self) -> None:
            self.grow_calls += 1

        def total_age(self) -> None:
            self.age_calls += 1

        def total_show(self) -> None:
            self.show_calls += 1

        def total_shade_calls(self) -> None:
            self.shade_calls += 1

        def display_stats(self) -> None:
            print(f"[statistics for {self.plant.name}]")
            print(
                f"Stats: {self.grow_calls} grow,"
                f" {self.age_calls} age, {self.show_calls} show"
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
        self.color = color
        self.bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to grow and bloom]")
        self.bloomed = True

    def grow(self) -> None:
        self.height = self.height + 8
        self.stats.total_growth()


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seed_number = 0

    def number_seeds(self) -> None:
        print(f"Seeds: {self.seed_number}")
        self.seed_number = self.seed_number + 42

    def bloomseed(self) -> None:
        print(f"[make {self.name.lower()} grow, age and bloom]")
        self.bloomed = True

    def growandage(self) -> None:
        self.height = self.height + 30
        self.age = self.age + 20
        self.stats.total_growth()
        self.stats.total_age()


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = 0
        self.stats = self.Treestats(self)

    def show(self) -> None:
        super().show()

        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        self.stats.total_shade_calls()
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height:.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide."
        )

    class Treestats(Plant.Statistics):
        def __init__(self, plant) -> None:
            super().__init__(plant)

        def display_stats(self) -> None:
            super().display_stats()
            print(f"{self.shade_calls} shade")


def disp_statistics(plant) -> None:
    plant.stats.display_stats()


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
