import random


class Statistic:
    def __init__(self, legacy_points: int):
        self.value = self._generate_starting_value(legacy_points)
        self.description = None
        self.min_value = 0
        self.max_value = 100

    def __str__(self):
        return f"{self.value}"

    def increase(self, amount):
        self.value += amount
        if self.value > self.max_value:
            self.value = self.max_value

    def decrease(self, amount):
        self.value -= amount
        if self.value < self.min_value:
            self.value = self.min_value

    def _generate_starting_value(self, legacy_points: int):
        """Generate a starting value for the statistic based on random number and user properties."""
        """This is just a placeholder for now. Perhaps some statistics will be based on user properties, and others 
        will be random"""
        return legacy_points % 100 + random.randint(1, 3)


class Strength(Statistic):
    def __init__(self, value):
        super().__init__(value)
        self.description = "Strength is a measure of physical power."

# Define classes for each character
class Maggie:
    def __init__(self):
        self.strength = Strength(100)
        self.dexterity = Strength(90)
        self.constitution = Strength(50)
        self.vitality = Strength(60)
        self.endurance = Strength(100)
        self.intelligence = Strength(80)
        self.wisdom = Strength(100)
        self.knowledge = Strength(30)
        self.willpower = Strength(100)
        self.spirit = Strength(90)


class Owen:
    def __init__(self):
        self.strength = Strength(90)
        self.dexterity = Strength(90)
        self.constitution = Strength(50)
        self.vitality = Strength(30)
        self.endurance = Strength(90)
        self.intelligence = Strength(10)
        self.wisdom = Strength(90)
        self.knowledge = Strength(90)
        self.willpower = Strength(20)
        self.spirit = Strength(90)


class Priscilla:
    def __init__(self):
        self.strength = Strength(80)
        self.dexterity = Strength(70)
        self.constitution = Strength(80)
        self.vitality = Strength(80)
        self.endurance = Strength(40)
        self.intelligence = Strength(80)
        self.wisdom = Strength(50)
        self.knowledge = Strength(80)
        self.willpower = Strength(10)
        self.spirit = Strength(80)


class Grace:
    def __init__(self):
        self.strength = Strength(70)
        self.dexterity = Strength(10)
        self.constitution = Strength(70)
        self.vitality = Strength(70)
        self.endurance = Strength(50)
        self.intelligence = Strength(30)
        self.wisdom = Strength(70)
        self.knowledge = Strength(40)
        self.willpower = Strength(70)
        self.spirit = Strength(20)


class Ashley:
    def __init__(self):
        self.strength = Strength(60)
        self.dexterity = Strength(70)
        self.constitution = Strength(80)
        self.vitality = Strength(60)
        self.endurance = Strength(60)
        self.intelligence = Strength(60)
        self.wisdom = Strength(70)
        self.knowledge = Strength(80)
        self.willpower = Strength(60)
        self.spirit = Strength(30)


class Sydney:
    def __init__(self):
        self.strength = Strength(50)
        self.dexterity = Strength(60)
        self.constitution = Strength(70)
        self.vitality = Strength(50)
        self.endurance = Strength(50)
        self.intelligence = Strength(50)
        self.wisdom = Strength(30)
        self.knowledge = Strength(70)
        self.willpower = Strength(50)
        self.spirit = Strength(50)


class Maya:
    def __init__(self):
        self.strength = Strength(40)
        self.dexterity = Strength(50)
        self.constitution = Strength(60)
        self.vitality = Strength(40)
        self.endurance = Strength(50)
        self.intelligence = Strength(60)
        self.wisdom = Strength(40)
        self.knowledge = Strength(40)
        self.willpower = Strength(40)
        self.spirit = Strength(40)


class Marcus:
    def __init__(self):
        self.strength = Strength(30)
        self.dexterity = Strength(50)
        self.constitution = Strength(40)
        self.vitality = Strength(30)
        self.endurance = Strength(30)
        self.intelligence = Strength(60)
        self.wisdom = Strength(30)
        self.knowledge = Strength(40)
        self.willpower = Strength(30)
        self.spirit = Strength(50)


class David:
    def __init__(self):
        self.strength = Strength(10)
        self.dexterity = Strength(10)
        self.constitution = Strength(20)
        self.vitality = Strength(20)
        self.endurance = Strength(20)
        self.intelligence = Strength(20)
        self.wisdom = Strength(10)
        self.knowledge = Strength(10)
        self.willpower = Strength(20)
        self.spirit = Strength(20)


# Create instances of each character class
maggie = Maggie()
owen = Owen()
priscilla = Priscilla()
grace = Grace()
ashley = Ashley()
sydney = Sydney()
maya = Maya()
marcus = Marcus()
david = David()

# Example of accessing the strength attribute for each character
print("Strength of Maggie:", maggie.strength.value)
print("Strength of Owen:", owen.strength.value)
print("Strength of Priscilla:", priscilla.strength.value)
print("Strength of Grace:", grace.strength.value)
print("Strength of Ashley:", ashley.strength.value)
print("Strength of Sydney:", sydney.strength.value)
print("Strength of Maya:", maya.strength.value)
print("Strength of Marcus:", marcus.strength.value)
print("Strength of David:", david.strength.value)