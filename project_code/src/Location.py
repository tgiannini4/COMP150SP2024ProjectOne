#parserGlobal = UserInputParser
class Location:

import json

# List of location names
location_names = [
    "Temple of the Sheep",
    "Baaaadmans Village",
    "Sheep Desert",
    "Tomb of Lambs",
    "Ewe-ok Village",
    "The Lost Valley",
    "The Palace of Dolly",
    "Enchanted Woods",
    "Mary's Dreamy Wonderland",
    "City of Mutton"
]

# Writing the location names to a JSON file
with open("location_names.json", "w") as file:
    json.dump(location_names, file)

import random

    def __init__(self, name, parser, number_of_events: int = 1):
        self.name = name
        self.parser = parser
        self.events = [Event(self.parser) for _ in range(number_of_events)]

    def create_custom_event_from_static_text_file(self, file_path):
        # load json file from path
        with open(file_path, "r") as file:
            data = json.load(file)

        return Event(self.parser, data)

# List of location names
location_names = [
    "Temple of the Sheep",
    "Baaaadmans Village",
    "Sheep Desert",
    "Tomb of Lambs",
    "Ewe-ok Village",
    "The Lost Valley",
    "The Palace of Dolly",
    "Enchanted Woods",
    "Mary's Dreamy Wonderland",
    "City of Mutton"
]

locations = [Location(name, parser) for name in random.sample(location_names, 10)]


    def __init__(self, parser, number_of_events: int = 1):
        self.parser = parser
        self.events = [Event(self.parser) for _ in range(number_of_events)]
    pass