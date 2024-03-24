# main.py
import sys
from project_code.src.UserInputParser import UserInputParser
from project_code.src.InstanceCreator import InstanceCreator
from project_code.src.UserFactory import UserFactory

def start_game():
    parser = UserInputParser()
    user_factory = UserFactory()
    instance_creator = InstanceCreator(user_factory, parser)

    response = parser.parse("Would you like to start a new game? (yes/no)")
    print(f"Response: {response}")
    user = instance_creator.get_user_info(response)
    if user is not None:
        game_instance = user.current_game
        if game_instance is not None:
            response = game_instance.start_game()
            if response == "Save and quit":
                user.save_game()
                print("Game saved. Goodbye!")
                sys.exit()
            elif response:
                print("Goodbye!")
                sys.exit()
    else:
        print("See you next time!")
        sys.exit()

if __name__ == '__main__':
    start_game()

    import json
import sys
from project_code.src.UserInputParser import UserInputParser
from project_code.src.InstanceCreator import InstanceCreator
from project_code.src.UserFactory import UserFactory
from typing import List
import random


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






from enum import Enum


class EventStatus(Enum):
    UNKNOWN = "unknown"
    PASS = "pass"
    FAIL = "fail"
    PARTIAL_PASS = "partial_pass"


class Event:

        def __init__(self, parser, data: dict = None):



            self.parser = parser
            # parse json file
            self.primary = data['primary_attribute']
            self.secondary = data['secondary_attribute']
            self.prompt_text = data['prompt_text']
            self.pass_ = data['pass']
            self.fail = data['fail']
            self.partial_pass = data['partial_pass']


            self.status = EventStatus.UNKNOWN
            self.fail = {
                "message": "You failed."
            }
            self.pass_ = {
                "message": "You passed."
            }
            self.partial_pass = {
                "message": "You partially passed."
            }
            self.prompt_text = "A dragon appears, what will you do?"

            self.primary: Statistic = Strength()
            self.secondary: Statistic = Dexterity()

        def execute(self, party):
            chosed_one = self.parser.select_party_member(party)
            chosen_skill = self.parser.select_skill(chosed_one)

            self.set_status(EventStatus.PASS)
            pass

        def set_status(self, status: EventStatus = EventStatus.UNKNOWN):
            self.status = status

        def resolve_choice(self, party, character, chosen_skill):
            # check if the skill attributes overlap with the event attributes
            # if they don't overlap, the character fails
            # if one overlap, the character partially passes
            # if they do overlap, the character passes



from project_code.src.Statistic import *


from project_code.src.Statistic import *


class Character:
    def __init__(self, name: str, strength: int, dexterity: int, constitution: int,
                 vitality: int, endurance: int, intelligence: int, wisdom: int,
                 knowledge: int, willpower: int, spirit: int):
        self.name = name
        self.strength: Strength = Strength(self, strength)
        self.dexterity: Dexterity = Dexterity(self, dexterity)
        self.constitution: Constitution = Constitution(self, constitution)
        self.vitality: Vitality = Vitality(self, vitality)
        self.endurance: Endurance = Endurance(self, endurance)
        self.intelligence: Intelligence = Intelligence(self, intelligence)
        self.wisdom: Wisdom = Wisdom(self, wisdom)
        self.knowledge: Knowledge = Knowledge(self, knowledge)
        self.willpower: Willpower = Willpower(self, willpower)
        self.spirit: Spirit = Spirit(self, spirit)


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


class Game:

    def __init__(self, parser):
        self.parser = parser
        self.characters: List[Character] = []
        self.locations: List[Location] = []
        self.events: List[Event] = []
        self.party: List[Character] = []
        self.current_location = None
        self.current_event = None
        self.continue_playing = True

        self._initialize_game()

    def add_character(self, character: Character):
        """Add a character to the game."""
        self.characters.append(character)

    def add_location(self, location: Location):
        """Add a location to the game."""
        self.locations.append(location)

    def add_event(self, event: Event):
        """Add an event to the game."""
        self.events.append(event)

    def _initialize_game(self):
        """Initialize the game with characters, locations, and events based on the user's properties."""
        character_list = [Character() for _ in range(10)]
        location_list = [Location(self.parser) for _ in range(2)]

        for character in character_list:
            self.add_character(character)

        for location in location_list:
            self.add_location(location)

    def start_game(self):
        return self._main_game_loop()

    def _main_game_loop(self):
        """The main game loop."""
        while self.continue_playing:
            self.current_location = self.locations[0]
            self.current_event = self.current_location.getEvent()

            self.current_event.execute()

            if self.party is None:
                # award legacy points
                self.continue_playing = False
                return "Save and quit"
            else:
                continue
        if self.continue_playing is False:
            return True
        elif self.continue_playing == "Save and quit":
            return "Save and quit"
        else:
            return False


class User:

    def __init__(self, parser, username: str, password: str, legacy_points: int = 0):
        self.username = username
        self.password = password
        self.legacy_points = legacy_points
        self.current_game = self._get_retrieve_saved_game_state_or_create_new_game()
        self.parser = parser

    def _get_retrieve_saved_game_state_or_create_new_game(self) -> Game:
        new_game = Game(self.parser)
        return new_game

    def save_game(self):
        pass


class UserInputParser:

    def __init__(self):
        self.style = "console"

    def parse(self, prompt) -> str:
        response: str = input(prompt)
        return response


class UserFactory:

    @staticmethod
    def create_user(parser: UserInputParser) -> User:
        username = parser.parse("Enter a username: ")
        password = parser.parse("Enter a password: ")
        # Here you can add more logic as needed, e.g., validate input
        return User(parser, username=username, password=password)


class InstanceCreator:

    def __init__(self, user_factory: UserFactory, parser: UserInputParser):
        self.user_factory = user_factory
        self.parser = parser

    def _new_user_or_login(self) -> User:
        response = self.parser.parse("Create a new username or login to an existing account?")
        if "login" in response:
            return self._load_user()
        else:
            return self.user_factory.create_user(self.parser)

    def get_user_info(self, response: str) -> User | None:
        if "yes" in response:
            return self._new_user_or_login()
        else:
            return None

    def _load_user(self) -> User:
        pass





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


class User:

    def __init__(self, parser, username: str, password: str, legacy_points: int = 0):
        self.username = username
        self.password = password
        self.legacy_points = legacy_points
        self.parser = parser
        self.current_game = self._get_retrieve_saved_game_state_or_create_new_game()

    def _get_retrieve_saved_game_state_or_create_new_game(self) -> Game:
        new_game = Game(self.parser)
        return new_game

    def save_game(self):
        pass
