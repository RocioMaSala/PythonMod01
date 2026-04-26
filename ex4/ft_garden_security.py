#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int, growth_type: str):
        self.name = name
        self._height = height
        self._age = age
        self.totalgrowth: float = 0
        self.growth_type = growth_type

    def show(self) -> None:
        h = round(self.get_height(), 2)
        print(f"Plant created: {self.name}: {h}cm, {self.get_age()} days old")

    def current_show(self) -> None:
        h = round(self.get_height(), 2)
        print(f"Current state: {self.name}: {h}cm, {self.get_age()} days old")

    def get_height(self) -> float:
        return self._height

    def set_height(self, value) -> None:
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            h = round(self._height, 2)
            print(f"Height updated: {h}cm")

    def get_age(self) -> int:
        return self._age

    def set_age(self, value) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value
            print(f"Age updated: {self._age} days")

    def grow(self) -> None:
        if self.growth_type == "fast":
            growth = .8
        elif self.growth_type == "medium":
            growth = .5
        elif self.growth_type == "slow":
            growth = .2
        else:
            growth = 0
        self.set_height(self.get_height() + growth)
        self.totalgrowth += growth

    def total_age(self) -> None:
        self.set_age(self.get_age() + 1)


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15, 10, "medium")
    plant.show()
    print()
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-15)
    plant.set_age(-5)
    print()
    plant.current_show()


if __name__ == "__main__":
    ft_garden_security()
