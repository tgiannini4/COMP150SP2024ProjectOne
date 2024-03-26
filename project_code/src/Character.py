import random

# Importing the required classes from project_code.src.Statistic
from project_code.src.Statistic import Strength, Dexterity, Constitution, Vitality, Endurance, \
    Intelligence, Wisdom, Knowledge, Willpower, Spirit


class Character:
    def __init__(self, name: str):
        self.name = name
        self.strength: Strength = None
        self.dexterity: Dexterity = None
        self.constitution: Constitution = None
        self.vitality: Vitality = None
        self.endurance: Endurance = None
        self.intelligence: Intelligence = None
        self.wisdom: Wisdom = None
        self.knowledge: Knowledge = None
        self.willpower: Willpower = None
        self.spirit: Spirit = None
        self.generate_statistics()

class Statistic:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def increase(self, amount):
        self.value += amount

    def decrease(self, amount):
        self.value -= amount

def Strength(value):
    return Statistic(value)

def Dexterity(value):
    return Statistic(value)

def Constitution(value):
    return Statistic(value)

def Vitality(value):
    return Statistic(value)

def Endurance(value):
    return Statistic(value)

def Intelligence(value):
    return Statistic(value)

def Wisdom(value):
    return Statistic(value)

def Knowledge(value):
    return Statistic(value)

def Willpower(value):
    return Statistic(value)

def Spirit(value):
    return Statistic(value)

# Define the base statistics for each character
base_statistics = {
    "Maggie": (10, 9, 5, 6, 10, 8, 10, 3, 10, 9),
    "Owen": (9, 9, 5, 3, 9, 1, 9, 9, 2, 9),
    "Priscilla": (8, 7, 8, 8, 4, 8, 5, 8, 1, 8),
    "Grace": (7, 1, 7, 7, 5, 3, 7, 4, 7, 2),
    "Ashley": (6, 7, 8, 6, 6, 6, 7, 8, 6, 3),
    "Sydney": (5, 6, 7, 5, 5, 5, 3, 7, 5, 5),
    "Maya": (4, 5, 6, 4, 5, 6, 4, 4, 4, 4),
    "Marcus": (3, 5, 4, 3, 3, 6, 3, 4, 3, 5),
    "David": (1, 1, 2, 2, 2, 2, 1, 1, 2, 2)
}


# Define a subclass for each character
class Maggie(Character):
    def __init__(self):
        super().__init__("Maggie", *base_statistics["Maggie"])


class Owen(Character):
    def __init__(self):
        super().__init__("Owen", *base_statistics["Owen"])


class Priscilla(Character):
    def __init__(self):
        super().__init__("Priscilla", *base_statistics["Priscilla"])


class Grace(Character):
    def __init__(self):
        super().__init__("Grace", *base_statistics["Grace"])


class Ashley(Character):
    def __init__(self):
        super().__init__("Ashley", *base_statistics["Ashley"])


class Sydney(Character):
    def __init__(self):
        super().__init__("Sydney", *base_statistics["Sydney"])


class Maya(Character):
    def __init__(self):
        super().__init__("Maya", *base_statistics["Maya"])


class Marcus(Character):
    def __init__(self):
        super().__init__("Marcus", *base_statistics["Marcus"])


class David(Character):
    def __init__(self):
        super().__init__("David", *base_statistics["David"])


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

# Print out the statistics for each character
characters = [maggie, owen, priscilla, grace, ashley, sydney, maya, marcus, david]

for character in characters:
    print(f"{character.name}:")
    print(f"Strength: {character.strength.value}")
    print(f"Dexterity: {character.dexterity.value}")
    print(f"Constitution: {character.constitution.value}")
    print(f"Vitality: {character.vitality.value}")
    print(f"Endurance: {character.endurance.value}")
    print(f"Intelligence: {character.intelligence.value}")
    print(f"Wisdom: {character.wisdom.value}")
    print(f"Knowledge: {character.knowledge.value}")
    print(f"Willpower: {character.willpower.value}")
    print(f"Spirit: {character.spirit.value}")
    print()
