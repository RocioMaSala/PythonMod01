class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.stats = self.statistics(self)

    def show(self) -> None:
        h = self.height
        print(f"{self.name}: {h:.1f}cm, {self.age} days old")
        self.stats.totalshow()

    class statistics:
        def __init__(self, plant) -> None:
            self.plant = plant
            self.growcalls = 0
            self.agecalls = 0
            self.showcalls = 0
            self.shadecalls = 0

        def totalgrowth(self) -> None:
            self.growcalls += 1

        def totalage(self) -> None:
            self.agecalls += 1

        def totalshow(self) -> None:
            self.showcalls += 1

        def totalshadecalls(self) -> None:
            self.shadecalls += 1

        def display_stats(self) -> None:
            print(f"[statistics for {self.plant.name}]")
            print(
                f"Stats: {self.growcalls} grow,"
                f"{self.agecalls} age, {self.showcalls} show"
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
        self.height = self.height + 7
        self.stats.totalgrowth()


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seednumber = 0

    def number_seeds(self) -> None:
        print(f"Seeds: {self.seednumber}")
        self.seednumber = self.seednumber + 42

    def bloomseed(self) -> None:
        print(f"[make {self.name.lower()} grow, age and bloom]")
        self.bloomed = True

    def growandage(self) -> None:
        self.height = self.height + 30
        self.age = self.age + 20
        self.stats.totalgrowth()
        self.stats.totalage()


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = 0
        self.stats = self.treestats(self)

    def show(self) -> None:
        super().show()

        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        self.stats.totalshadecalls()
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(
                f"Tree {self.name} now produces a shade of "
                f"{self.height:.1f}cm long and "
                f"{self.trunk_diameter:.1f}cm wide."
            )

    class treestats(Plant.statistics):
        def __init__(self, plant) -> None:
            super().__init__(plant)

        def display_stats(self) -> None:
            super().display_stats()
            print(f"{self.shadecalls} shade")


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
    flower.show()
    flower.grow()
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
