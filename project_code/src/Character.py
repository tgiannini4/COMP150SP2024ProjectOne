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



import random

class RivalBand:
    def __init__(self, location_name, band_name):
        self.location_name = location_name
        self.band_name = band_name
        self.characters = self.generate_characters()
    
    def generate_characters(self):
        characters = []
        num_characters = random.randint(3, 5)  # Randomly choose the number of characters in the rival band
        
        for _ in range(num_characters):
            character_name = self.generate_character_name()
            legacy_points = random.randint(100, 1000)  # Randomly assign legacy points to each character
            characters.append((character_name, legacy_points))
        
        return characters
    
    def generate_character_name(self):
        prefixes = ["The", "The Legendary", "The Fabulous", "The Sensational", "The Epic"]
        suffixes = ["Rockers", "Legends", "Band", "Musicians", "Ensemble"]
        name = f"{random.choice(prefixes)} {random.choice(suffixes)}"
        return name

# List of location names and rival band names
location_names = [
    "The Melody Mansion",
    "Tempo Terrace",
    "Crescendo Clubhouse",
    "Harmonic Hideaway",
    "Resonance Retreat"
]

rival_band_names = [
    "Harmony Warriors",
    "Beat Breakers",
    "Melodic Masters",
    "Rhythm Rebels",
    "Symphony Seekers"
]

# Generate rival bands at each location with different names
rival_bands = {location: RivalBand(location, band_name) for location, band_name in zip(location_names, rival_band_names)}

# Print rival bands
for location, rival_band in rival_bands.items():
    print(f"Rival Band at {location}: {rival_band.band_name}")
    for character_name, legacy_points in rival_band.characters:
        print(f"- {character_name}: {legacy_points} legacy points")
