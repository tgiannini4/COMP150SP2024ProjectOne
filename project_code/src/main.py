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

def encounter_frantic_sheep(party):
    print("Encounter with the Frantic Sheep:")
    print("As your party is walking through Ewe-ok Village, you come across a sheep frantically running towards you.")
    print("It bleats desperately, catching your attention. As it approaches, you notice Scroll of Speak to Animals.")
    choice = input("Do you and your party activate this scroll? (Yes/No): ")
    if choice.lower() == "yes":
        revelation_of_finethir_shinebright(party)
    else:
        print("No, You and your party continue walking onwards and enjoy a nice evening at the local tavern and continue travelling to Baaaadmans Village. The end.")

def revelation_of_finethir_shinebright(party):
    print("Revelation of Finethir Shinebright's True Identity:")
    print("Upon activating the Scroll of Speak to Animals, the sheep reveals itself to be Finethir Shinebright, a renowned wizard of transmutation.")
    # Details of conversation with Finethir Shinebright
    # Implement choice for continuing conversation with Finethir Shinebright
    choice = input("Do you and your party still continue to converse with him? (Yes/No): ")
    if choice.lower() == "yes":
        learning_of_ahmed_nokes_betrayal(party)
    else:
        print("No, You and your party have had enough of this talking sheep and you continue walking onwards and enjoy a nice evening at the local tavern and continue travelling to the City of Mutton. The end.")

def learning_of_ahmed_nokes_betrayal(party):
    print("Learning of Ahmed Noke's Betrayal:")
    # Details of conversation with Finethir about Ahmed Noke's betrayal
    # Implement choice for agreeing to help Finethir
    choice = input("Do you agree to help Finethir retrieve the Wand of True Polymorph? (Yes/No): ")
    if choice.lower() == "yes":
        encounter_with_guz(party)
    else:
        print("No, You and your party decide to no longer entertain this talking sheep and you continue walking onwards and enjoy a nice evening at the local tavern. The end.")

def encounter_with_guz(party):
    print("Encounter with Guz:")
    # Details of encounter with Guz
    # Implement choice for engaging Guz or not
    choice = input("Do you engage with Guz? (Yes/No): ")
    if choice.lower() == "yes":
        # Implement skill check based on strength
        if skill_check(party[0], "strength", 15):
            print("You and your party defeat Guz. Seeing that Finehir is currently being targeted by assassins to turn him into a mutton dinner, you and your party decide to find Noke ASAP.")
        else:
            print("Guz defeats your party and turns Finehir into a mutton dinner. Although most of your party made it through with minor injuries, Guz seemed to particularly dislike you, and he kills you. The end.")
    else:
        # Implement choice for talking it out with Guz
        choice = input("Do you try to talk it out with him? (Yes/No): ")
        if choice.lower() == "yes":
            # Implement skill check based on intelligence
            if skill_check(party[0], "intelligence", 12):
                print("You and your party convince Guz not to attack and continue on your way.")
            else:
                print("Guz is enraged, particularly at you, and he kills you. The end.")
        else:
            # Implement skill check based on strength
            if skill_check(party[0], "strength", 15):
                print("You and your party defeat Guz. Seeing that Finehir is currently being targeted by assassins to turn him into a mutton dinner, you and your party decide to find Noke ASAP.")
            else:
                print("Guz defeats your party and turns Finehir into a mutton dinner. Although most of your party made it through with minor injuries, Guz seemed to particularly dislike you, and he kills you. The end.")

# Define other functions for remaining events

# # Define party members
# party_member_1 = PartyMember("Character 1", 14, 10)  # Example stats
# party_member_2 = PartyMember("Character 2", 12, 15)  # Example stats
# party = [party_member_1, party_member_2]  # Example party

# Start the game with the first event
encounter_frantic_sheep(party)
def navigating_through_ewe_ok_village(party):
    print("Navigating through Ewe-ok Village:")
    # Details of navigating through Ewe-ok Village
    # Implement choice for asking advice
    choice = input("Do you ask for advice at the Temple of the Sheep? (Yes/No): ")
    if choice.lower() == "yes":
        print("Yes, You and your party learn that the Wand of True Polymorph is suspected to be in poor condition.")
        print("In addition, you also learn that Noke has become a paranoid recluse, due to his fear meeting the same fate as Finehir.")
    else:
        print("No, You and your party receive no new information. You happen to see some shady individuals lurking around the main altar in the Temple of the Sheep. They seem to be following you and your party with their eyes.")

def confrontation_with_nokes_bodyguards(party):
    print("Confrontation with Noke's Bodyguards:")
    # Details of confrontation with Noke's bodyguards
    # Implement choice for engaging or bypassing/negotiating with the bodyguards
    choice = input("Do you engage in a confrontation with Noke's bodyguards? (Yes/No): ")
    if choice.lower() == "yes":
        # Implement skill check for confrontation
        if skill_check(party[0], "strength", 15):
            print("You and your party defeat the bodyguards. Noke seems to have disappeared into his bedroom.")
        else:
            print("You and your party die along with Finethir. The end.")
    else:
        # Implement skill check for bypassing/negotiating
        if skill_check(party[0], "stealth", 15):  # Assuming stealth skill for simplicity
            print("You and your party were able to sneak past the guards without them noticing you. Noke seems to have disappeared into his bedroom.")
        else:
            print("As you and your party are sneaking around, you knock over a test tube and it shatters, creating a noise that draws the attention of the bodyguards. They attack before you and your party are prepared, killing you and your party. The end.")

def battle_with_nokes_bed_dragon_wyrmling(party):
    print("Battle with Noke's Bed Dragon Wyrmling:")
    # Details of battle with Noke's bed dragon wyrmling
    # Implement choice for engaging or bypassing/neutralizing the dragon
    choice = input("Do you engage with Noke's peculiar pet dragon? (Yes/No): ")
    if choice.lower() == "yes":
        # Implement skill check for battle
        if skill_check(party[0], "strength", 15):
            print("You and your party successfully slay the dragon, and you notice the Wand of True Polymorph laying on the ground. You continue on to face Noke.")
        else:
            print("The dragon absolutely destroys you and your party. You die. The end.")
    else:
        # Implement skill check for bypassing/neutralizing the dragon
        if skill_check(party[0], "dexterity", 15):  # Assuming dexterity skill for simplicity
            print("You and your party successfully dodge all of the dragon's splinter attacks, and you notice the Wand of True Polymorph laying on the ground. You continue on to face Noke.")
        else:
            print("You are extremely wounded, and you see the Wand of True Polymorph laying on the ground. You use the last bit of strength to reach for it. So close, yet so far. Noke grabs it before you and he transforms you into a Gibbering Mouther, and you die. The end.")

def retrieve_the_wand_of_true_polymorph(party):
    print("Retrieve the Wand of True Polymorph:")
    # Details of retrieving the Wand of True Polymorph
    # Implement choice for using the wand to cast a spell on Noke
    choice = input("Do you use it to cast a spell on Noke? (Yes/No): ")
    if choice.lower() == "yes":
        # Implement luck check for using the wand
        if random.random() < 0.5:  # 50% chance of success
            print("Although your luck should allow you to transform Noke into a sheep (as you intended), the wand malfunctions due to its poor condition and Noke is transformed into a Gibbering Mouther. He dies shortly after.")
        else:
            print("Due to your inexperience with the wand, Noke is transformed into a Gibbering Mouther. He dies.")
    else:
        print("No, Noke grabs it from your hand and he transforms you into a Gibbering Mouther. You die. The end.")

def restoration_of_finethir_shinebright(party):
    print("Restoration of Finethir Shinebright:")
    # Details of restoring Finethir Shinebright
    # Implement choice for reversing the spell
    choice = input("Do you reverse the spell to restore Finethir Shinebright? (Yes/No): ")
    if choice.lower() == "yes":
        # Implement chance check for successful restoration
        if random.random() < 0.8:  # 80% chance of success
            print("You use it to reverse the polymorph spell, restoring him to his true form as a wizard.")
            resolution_and_future_plans(party)
        else:
            print("Shinebright dies. Does your party honor his dying wish to leave the tower more-or-less intact?")
            # Implement further choices based on the above outcome
            # Define further actions based on player's choice
    else:
        print("Shinebright accepts your decision but will not give up his hope entirely.")
        print("He takes back his old home in the tower and works towards a way to remove his curse (despite not having opposable thumbs).")
        print("He is upset, but still recognizes he is in debt to your party for your help. The end.")

def resolution_and_future_plans(party):
    print("Resolution and Future Plans:")
    # Details of resolution and future plans
    # Implement further dialogue or actions for the party's reflection and discussion
def resolution_and_future_plans(party):
    print("Resolution and Future Plans:")
    print("With Finethir's gratitude and promises of rewards, your party reflects on the adventure and discusses potential future endeavors with their newly restored ally.")
    print("Perhaps there are still mysteries to uncover in Ewe-ok Village or beyond.")
    choice = input("Do you wish to discuss further plans with Finethir? (Yes/No): ")
    if choice.lower() == "yes":
        print("You and your party spend hours discussing potential future quests, adventures, and alliances.")
        print("Finethir shares some insights about ancient ruins rumored to hold powerful artifacts, as well as possible threats lurking in nearby forests.")
        print("With renewed determination, your party sets forth on a new journey, ready to face whatever challenges lie ahead.")
    else:
        print("Deciding to rest and recuperate for a while, your party bids farewell to Finethir and sets up camp for the night.")
        print("As the fire crackles and stars twinkle above, you share stories of past adventures and dreams of future conquests.")
        print("Tomorrow is another day, and you're ready to face it head-on.")
    print("The end.")


#Encounter with the Frantic Sheep: As your party is walking through Ewe-ok Village, you come across a sheep frantically running towards you. It bleats desperately, catching your attention. As it approaches, you notice Scroll of Speak to Animals. Do you and your party activate this scroll?
            #No, You and your party continue walking onwards and enjoy a nice evening at the local tavern and continue travelling to Baaaadmans Village. The end.
            #Yes, continue. 

#Revelation of Finethir Shinebright's True Identity: Upon activating the Scroll of Speak to Animals, the sheep reveals itself to be Finethir Shinebright, a renowned wizard of transmutation who has been transformed into this helpless state by his apprentice, Ahmed Noke. With Finethir now able to communicate, he explains his situation in detail. He's both frustrated and humiliated by his current form but maintains his characteristic arrogance and intelligence. Do you and your party still continue to converse with him?
            #No, You and your party have had enough of this talking sheep and you continue walking onwards and enjoy a nice evening at the local tavern and continue travelling to the City of Mutton. The end.
            #Yes, continue. 

#Learning of Ahmed Noke's Betrayal: Finethir explains how Ahmed Noke, once his apprentice, grew resentful of his mentor's superiority and stole the Wand of True Polymorph, transforming Finethir into a sheep and declaring himself a master wizard. He needs you and your party to retrive this wand. Do you agree?
            #No, You and your party decide to no longer entertain this talking sheep and you continue walking onwards and enjoy a nice evening at the local tavern. The end.
            #Yes, continue.

#Encounter with Guz: While discussing their plan to retrieve the wand, your party is ambushed by Guz, a half-orc assassin loyal to Ahmed Noke. Guz, believing violence is the best solution, attacks without hesitation. Do you engage?
            #Yes, you and your party decide to fight back against Guz. (If strength is higher, then you win. If strength is lower then you lose.)
                #Higher Strength: You and your party defeat Guz. Seeing that Finehir is currently being targeted by assassins to turn him into a mutton dinner, you and your party decide to find Noke ASAP.
                #Lower Strength: Guz defeats your party and turns Finehir into a mutton dinner. Although most of your party made it through with minor injuries, Guz seemed to particularly dislike you, and he kills you. The end.
            #No,
                #Do you try to talk it out with him?
                    #Yes (if intelligence score is higher, then it is possible to persuade him to not fight and he walks away. If not, then he is enraged and more aggressive.)
                        #Higher Intelligence: You and your party convice Guz not to attack and continue on your way. 
                        #Lower Intelligence: Guz is enraged, particularly at you and he kills you. The end. 
                    #No, He still attacks anyway.
                        #Higher Strength: You and your party defeat Guz. Seeing that Finehir is currently being targeted by assassins to turn him into a mutton dinner, you and your party decide to find Noke ASAP.
                        #Lower Strength: Guz defeats your party and turns Finehir into a mutton dinner. Although most of your party made it through with minor injuries, Guz seemed to particularly dislike you, and he kills you. The end.

#Navigating through Ewe-ok Village: As you make your way through the village, you encounter various locations, including the Temple of the Sheep, where you may find clues or assistance from the locals familiar with transmutation magic. Do you ask for advice?
            #Yes, You and your party learn that the Wand of True Polymorph is suspected to be in poor condition. In addition, you also learn that Noke has become a paranoid recluse, due to his fear meeting the same fate as Finehir.
            #No, You and your party recieve no new information. You happen to see some shady individuals lurking around the main altar in the Temple of the Sheep. They seem to be following your and your party with their eyes. 

#Confrontation with Noke's Bodyguards: Upon reaching Ahmed Noke's hideout in the Palace of Dolly, your party faces off against his hired bodyguards, who are determined to protect their master at all costs.
    #Yes, Your party engages in a confrontation with Noke's bodyguards.
        #Check: to determine the outcome of the confrontation.
            #Success, You and your party defeat the bodyguards. Noke seems to have disappeared into his bedroom.
            #Fail, You and your party die along with Finethir. The end.
    #No, Your party tries to find a way to bypass or negotiate with the bodyguards.
        #Check: Roll for persuasion/stealth
            #Success, You and your party were able to sneak past the guards without them noticing you. Noke seems to have disappeared into his bedroom.
            #Fail, As you and your party are sneaking around, you knock over a test tube and it shatters, creating a noise that draws the attention of the bodyguards. They attack before you and your party are prepared, killing you and your party. The end.

#Battle with Noke's Bed Dragon Wyrmling: Inside the hideout, your party encounters Noke's peculiar pet dragon, a young wyrmling that resembles a bed. It attacks with "Splinter Breath," adding another layer of challenge to the confrontation. Do you engage?
            #Yes, Your party decides to confront Noke's peculiar pet dragon.
                #Check: Roll strength.
                     #Success: You and your party successfully slay the dragon, and you notice the Wand of True Polymorph laying on the ground. You continue on to face Noke.
                    #Fail: The dragon absolutely destroys you and your party. You die. The end.
            #No, Your party attempts to find a way to bypass or neutralize the dragon without engaging in direct combat.
                #Check: Roll for stealth/dexterity
                    #Success: You and your party successfully dodge all of the dragons splinter attacks, and you notice the Wand of True Polymorph laying on the ground. You continue on to face Noke.
                    #Fail: You are extremely wounded, and you see the Wand of True Polymorph laying on the ground. You use the the last bit of strength to reach for it. So close, yet so far. Noke grabs it before you and he transforms you into a Gibbering Mouther, and you die. The end.  

#Retrieve the Wand of True Polymorph: After overcoming the obstacles, your party finally retrieves the Wand of True Polymorph, though not without difficulty and risk. Do you use it to cast a spell on Noke?
            #Yes, luck check. 
                #Success: Although your luck should allow you to transform Noke into a sheep (as you intended), the wand malfunctions due to its poor condition and Noke is transformed into a Gibbering Mouther. He dies shortly after.  
                #Fail: Due to your inexperience with the wand, Noke is transformed into a Gibbering Mouther. He dies.  
            #No, Noke grabs it from your hand and he transforms you into a Gibbering Mouther. You die. The end.

#Restoration of Finethir Shinebright: With the wand in hand, your party returns to Finethir. Do you reverse the spell? 
            #Yes, chance check.
                #Success, You use it to reverse the polymorph spell, restoring him to his true form as a wizard. (only continue here)
                #Fail, Shinebright dies. Does your party honor his dying wish to leave the tower more-or-less intact?
                    #No, You and your party loot to your hearts' content. The tower is pretty empty to anything of benefit to non-transmuters, how ever expensive lab equipment and arcane paraphernalia are estimated to be worth around 1,000 gold pieces. Your party can also decide to take over the tower for yourselves. Do you?
                        #Yes, You take over the tower and live happily ever after (despite some disagreements from the locals). You decide to study transmutation magic and become the new master wizard of Ewe-ok Village. The end. 
                        #No, You leave the tower in the same condition as it was and flee, since the townfolk are not very pleased that you have killed both of their master wizards. You continue on to the City of Mutton. The end.
                    #Yes, You and your party respect his wishes and turn over his tower to other local transmutation wizards. You give Finehir a proper burial in the Lost Valley. The end. 
            #No, Shinebright accepts your decision but will not give up his hope entirely. He takes back his old home in the tower and works towards a way to remove his curse (despite not having opposable thumbs). He heads to his bedroom and slips on an old robe, which he will wear until he returns back to his original form. He is upset, but still recognizes he is in debt to your party for your help. The end.  

#Resolution and Future Plans: With Finethir's gratitude and promises of rewards, your party reflects on the adventure and discusses potential future endeavors with their newly restored ally. Perhaps there are still mysteries to uncover in Ewe-ok Village or beyond. The end. 

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
