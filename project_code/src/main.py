# to do:
# create login system
# create legacy system--maybe you can start w/ better stats or luck
# create events with rival bands 
# maybe create inventory system? (idk)
# add skills/stats 
# include concepts, functions, and classes as described in the project description

import random

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Here you can implement the logic to validate the username and password
    # For simplicity, let's assume any username and password combination is valid
    # You can replace this with your actual validation logic
    
    # For demonstration purposes, let's check if both fields are non-empty
    if username and password:
        return True
    else:
        return False

def calculate_band_stats(user_band_members, band_members_stats):
    total_performance = sum(band_members_stats[member]["performance"] for member in user_band_members)
    total_charisma = sum(band_members_stats[member]["charisma"] for member in user_band_members)
    total_luck = sum(band_members_stats[member]["luck"] for member in user_band_members)
    return total_performance, total_charisma, total_luck

def generate_event(band_stats, rival_bands):
    total_performance, total_charisma, total_luck = band_stats

    rival_band_events = {
        "Harmony Havoc": ("Harmony Havoc's stunning performance threatens to overshadow your band's efforts!", total_performance < 10),
        "Serenade Syndicate": ("Serenade Syndicate's smooth melodies impress the judges, putting pressure on your band!", total_charisma < 15),
        "Voltage Vandals": ("Voltage Vandals' electrifying stage presence energizes the audience, making it challenging for your band to stand out!", total_luck < 10),
        "Sonic Surge": ("Sonic Surge's high-energy performance sets the bar high for your band!", total_performance < 12),
        "Chord Chaos": ("Chord Chaos's chaotic performance causes a stir among the audience, making it difficult for your band to maintain focus!", total_luck < 12)
    }

    rival_band_event = None
    for rival_band, (description, condition) in rival_band_events.items():
        if rival_band in rival_bands and condition:
            rival_band_event = description
            break

    events = [
        ("Your band's exceptional performance wows the audience, earning you extra points!", total_performance > 25),
        ("Your band's charismatic stage presence captivates the judges, earning you bonus points!", total_charisma > 20),
        ("Luck is on your side as a fortunate turn of events boosts your band's performance!", total_luck > 15),
        ("Your band's lackluster performance disappoints the audience.", total_performance < 15),
        ("Technical difficulties hinder your band's performance, but your quick thinking saves the show.", total_luck > 20),
        rival_band_event
    ]

    possible_events = [event[0] for event in events if event[1] is not None]
    if possible_events:
        return random.choice(possible_events)
    else:
        return "No notable events occur during your performance."

def generate_decision_event():
    decision_events = [
        ("A rival band, Harmony Havoc, has spread false rumors about your band, causing doubt among your fans. Do you:\n1. Ignore the rumors and focus on your performance.\n2. Address the rumors publicly to clear your band's name.", "Harmony Havoc")
        # Add more decision events here as needed
    ]
    return random.choice(decision_events)

def game():
    if not login():
        return
    
    ans = input('Would you like to play Battle of the Bands? (yes/no)')
    if ans.lower() == 'yes':
        print('Welcome to Battle of the Bands!!')
        start = True 
        inventory = []

        print("You have been chosen to be the manager of the next hottest band for Resonance Records!")
        band_name = input("Before we begin, please enter your band's name: ")

        rival_bands = ["Harmony Havoc", "Serenade Syndicate", "Voltage Vandals", "Sonic Surge", "Chord Chaos"]

        # List of potential band members with their roles
        band_members = {
            "Beatrice Groove": "Percussionist",
            "Harmony Heart": "Vocalist",
            "Melody Muse": "Pianist",
            "Axel Blaze": "Lead Guitarist",
            "Harmony Harmonica": "Harmonica Player",
            "Quinn Quintet": "Multi-Instrumentalist",
            "Felix Bassline": "Bassist",
            "Echo Eden": "Vocalist",
            "Amber Strings": "Violinist"
        }
        
        band_members_stats = {
            "Beatrice Groove": {"role": "Percussionist", "performance": 8, "charisma": 5, "luck": 3},
            "Harmony Heart": {"role": "Vocalist", "performance": 7, "charisma": 9, "luck": 4},
            "Melody Muse": {"role": "Pianist", "performance": 6, "charisma": 6, "luck": 6},
            "Axel Blaze": {"role": "Lead Guitarist", "performance": 9, "charisma": 7, "luck": 5},
            "Harmony Harmonica": {"role": "Harmonica Player", "performance": 5, "charisma": 4, "luck": 7},
            "Quinn Quintet": {"role": "Multi-Instrumentalist", "performance": 7, "charisma": 6, "luck": 5},
            "Felix Bassline": {"role": "Bassist", "performance": 6, "charisma": 5, "luck": 4},
            "Echo Eden": {"role": "Vocalist", "performance": 7, "charisma": 8, "luck": 6},
            "Amber Strings": {"role": "Violinist", "performance": 6, "charisma": 5, "luck": 5}
            
        }

        print(f"Great choice! Your band {band_name} is about to rock the stage!")
        print("But before Resonance Records signs your band, you have to prove your band has what it takes in the Battle of the Bands competition!")
        print("To enter the Battle of the Bands competition, first you have to form a band. Select 4 musicians for your band:")

        user_band_members = []

        while len(user_band_members) < 4:
            print("\nAvailable band members:")
            for member, role in band_members.items():
                print(f"{member} - {role}")
            choice = input("Enter the name of the musician you want to add to your band: ")
            if choice in band_members.keys():
                if choice not in user_band_members:
                    user_band_members.append(choice)
                    print(f"{choice} has been added to your band.")
                else:
                    print(f"{choice} is already in your band.")
            else:
                print("Invalid musician. Please select from the available options.")

        # Display selected band members
        print("\nYour selected band members are:")
        for member in user_band_members:
            print(member)
        
        band_venues = [
            "The Melody Mansion",
            "Tempo Terrace",
            "Crescendo Clubhouse",
            "Harmonic Hideaway",
            "Resonance Retreat"
        ]

        # Prompt the user to select a band venue
        print("Please select a band venue from the following list:")
        for venue in band_venues:
            print("-", venue)
        selected_venue = input("Enter the name of the band venue you want to perform at: ")

        # Validate the user's choice
        if selected_venue in band_venues:
            print(f"Great choice! Your band {band_name} will perform at {selected_venue}.")
        else:
            print("Invalid venue selection. Please choose from the available options.")

        # Calculate band stats
        band_stats = calculate_band_stats(user_band_members, band_members_stats)

        # Generate and display events
        print("\nEvents during your performance:")
        print("-" * 30)
        for _ in range(3):  # Generate 3 events
            print(generate_event(band_stats, rival_bands))

        # Generate and display decision event
        print("\nDecision event:")
        print("-" * 30)
        decision_event, rival_band = generate_decision_event()
        print(decision_event)

        # Take action based on decision event
        action = input("Enter your choice: ")
        if action == "1":
            print("You chose to ignore the rumors and focus on your performance.")
            # Perform action 1
        elif action == "2":
            print("You chose to address the rumors publicly to clear your band's name.")
            # Perform action 2
        else:
            print("Invalid choice. Please choose either 1 or 2.")

        # Generate and display resolution event
        print("\nResolution event:")
        print("-" * 30)
        print("After a thrilling performance, your band awaits the judges' final decision.")

game()
     














#old game below

def parse_user_input():
    """
    Parse user input and return the parsed data.
    """
    user_input = input("Enter your input: ")
    # Perform parsing logic here
    parsed_data = user_input.split()  # Example parsing logic (split input by whitespace)
    return parsed_data

# Example usage:
if __name__ == "__main__":
    parsed_input = parse_user_input()
    print("Parsed input:", parsed_input)

def create_parser():
    return UserInputParser()

def start_game():
    parser = create_parser()
    user_factory = UserFactory()
    instance_creator = InstanceCreator(user_factory, parser)

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



class Location:

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

import random

def data(self, file_path):
    # Example data dictionary
    data = {
        "event_name": "Example Event",
        "event_description": "This is an example event description.",
        "event_location": "Example Location",
        # Add more key-value pairs as needed
    }

    # Now you can use the 'data' variable to create an Event object
    return Event(self.parser, data)


def __init__(self, name, parser, number_of_events: int = 1):
        self.name = name
        self.parser = parser
        self.events = [Event(self.parser) for _ in range(number_of_events)]

def create_custom_event_from_static_text_file(self, file_path):

        return Event(self.parser, data)

# List of location names
location_names = [
    "The Melody Mansion",
    "Tempo Terrace",
    "Crescendo Clubhouse",
    "Harmonic Hideaway",
    "Resonance Retreat"
    ]

import random

# Assuming you have a function create_parser() that creates the parser
parser = create_parser()

# Assuming location_names is already defined
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
        if data:
            self.primary = data['primary_attribute']
            self.secondary = data['secondary_attribute']
            self.prompt_text = data['prompt_text']
            self.pass_message = data['pass_message']
            self.fail_message = data['fail_message']
            self.partial_pass_message = data['partial_pass_message']
        else:
            # Default values
            self.primary = None
            self.secondary = None
            self.prompt_text = "A challenge appears, how do you respond?"
            self.pass_message = "You successfully overcome the challenge."
            self.fail_message = "You failed to overcome the challenge."
            self.partial_pass_message = "You partially succeeded in overcoming the challenge."

        self.status = EventStatus.UNKNOWN

    def execute(self):
        choice = self.parser.parse(self.prompt_text)
        if choice.lower() == "yes":
            self.set_status(EventStatus.PASS)
        elif choice.lower() == "no":
            self.set_status(EventStatus.FAIL)
        else:
            self.set_status(EventStatus.PARTIAL_PASS)

    def set_status(self, status: EventStatus = EventStatus.UNKNOWN):
        self.status = status

    def resolve_choice(self, party, character, chosen_skill):
        # Placeholder for resolving the choice based on party's attributes and chosen skill
        pass




#### Events:
import random

class PartyMember:
    def __init__(self, name, strength, intelligence):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence

def skill_check(character, skill, difficulty):
    if skill == "strength":
        attribute = character.strength
    elif skill == "intelligence":
        attribute = character.intelligence
    else:
        attribute = 0  # Placeholder for other skills
    
    roll = random.randint(1, 20)  # Assuming d20 roll for simplicity
    if roll + attribute >= difficulty:
        return True
    else:
        return False

def create_party():
    character_list = {"Maggie": (10, 9, 5, 6, 10, 8, 10, 3, 10, 9),
    "Owen": (9, 9, 5, 3, 9, 1, 9, 9, 2, 9),
    "Priscilla": (8, 7, 8, 8, 4, 8, 5, 8, 1, 8),
    "Grace": (7, 1, 7, 7, 5, 3, 7, 4, 7, 2),
    "Ashley": (6, 7, 8, 6, 6, 6, 7, 8, 6, 3),
    "Sydney": (5, 6, 7, 5, 5, 5, 3, 7, 5, 5),
    "Maya": (4, 5, 6, 4, 5, 6, 4, 4, 4, 4),
    "Marcus": (3, 5, 4, 3, 3, 6, 3, 4, 3, 5),
    "David": (1, 1, 2, 2, 2, 2, 1, 1, 2, 2)}

    return character_list



class Party:
    def __init__(self, members):
        self.members = members

    def perform_action(self, action):
        # Placeholder for performing an action with the party
        pass

    def encounter_event(self, event):
        for member in self.members:
            event.resolve_choice(self, member, None)


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

    def earn_legacy_points(self, points: int):
        """Earn legacy points."""
        self.legacy_points += points

    def spend_legacy_points(self, points: int):
        """Spend legacy points if enough are available."""
        if self.legacy_points >= points:
            self.legacy_points -= points
            print(f"{self.username} spent {points} legacy points.")
        else:
            print(f"{self.username} does not have enough legacy points.")

    def check_legacy_points(self):
        """Check the current amount of legacy points."""
        print(f"{self.username} has {self.legacy_points} legacy points.")


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
