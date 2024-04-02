import random
def print_ascii_art():
    art = '''

                          ____         ___
                         ,' __ ``.._..''   `.
                         `.`. ``-.___..-.    :
 ,---..____________________>/          _,'_  |
 `-:._,:_|_|_|_|_|_|_|_|_|_|_|.:SSt:.:|-|(/  |
                        _.' )   ____  '-'    ;
                       (    `-''  __``-'    /
                        ``-....-''  ``-..-''

        '''
    print(art)

class Band:
    def __init__(self):
        self.band_members = {
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
        
        self.band_members_stats = {
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

    def calculate_band_stats(self, user_band_members):
        total_performance = sum(self.band_members_stats[member]["performance"] for member in user_band_members)
        total_charisma = sum(self.band_members_stats[member]["charisma"] for member in user_band_members)
        total_luck = sum(self.band_members_stats[member]["luck"] for member in user_band_members)
        return total_performance, total_charisma, total_luck

class Game:
    def __init__(self):
        self.band = Band()
        self.rival_bands = ["Harmony Havoc", "Serenade Syndicate", "Voltage Vandals", "Sonic Surge", "Chord Chaos"]

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username and password:
            return True
        else:
            print("Invalid username or password. Please try again.")
            return False

    def generate_event(self, band_stats):
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
            if rival_band in self.rival_bands and condition:
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

        possible_events = [event[0] for event in events if event is not None]  # Filter out None values
        if possible_events:
            return random.choice(possible_events)
        else:
            return "No notable events occur during your performance."

    def generate_decision_event(self):
        decision_events = [
            ("A rival band, Harmony Havoc, has spread false rumors about your band, causing doubt among your fans. Do you:\n1. Ignore the rumors and focus on your performance.\n2. Address the rumors publicly to clear your band's name.", "Harmony Havoc")
            # Add more decision events here as needed
        ]
        return random.choice(decision_events)

    def play(self):
        if not self.login():
            return
        
        ans = input('Would you like to play Battle of the Bands? (yes/no)')
        if ans.lower() == 'yes':
            print('Welcome to Battle of the Bands!!')
            print_ascii_art()

            print("You have been chosen to be the manager of the next hottest band for Resonance Records!")
            band_name = input("Before we begin, please enter your band's name: ")

            print(f"Great choice! Your band {band_name} is about to rock the stage!")
            print("But before Resonance Records signs your band, you have to prove your band has what it takes in the Battle of the Bands competition!")
            print("To enter the Battle of the Bands competition, first you have to form a band. Select 4 musicians for your band:")

            user_band_members = []
            while len(user_band_members) < 4:
                print("\nAvailable band members:")
                for member, role in self.band.band_members.items():
                    print(f"{member} - {role}")
                choice = input("Enter the name of the musician you want to add to your band: ")
                if choice in self.band.band_members.keys():
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
            
            # Prompt the user to select a band venue
            print("\nPlease select a band venue from the following list:")
            band_venues = [
                "The Melody Mansion",
                "Tempo Terrace",
                "Crescendo Clubhouse",
                "Harmonic Hideaway",
                "Resonance Retreat"
            ]
            for venue in band_venues:
                print("-", venue)
            selected_venue = input("Enter the name of the band venue you want to perform at: ")

            # Validate the user's choice
            if selected_venue in band_venues:
                print(f"Great choice! Your band {band_name} will perform at {selected_venue}.")
            else:
                print("Invalid venue selection. Please choose from the available options.")

            # Calculate band stats
            band_stats = self.band.calculate_band_stats(user_band_members)

            # Generate and display events
            print("\nEvents during your performance:")
            print("-" * 30)
            for _ in range(3):  # Generate 3 events
                print(self.generate_event(band_stats))

            # Generate and display decision event
            print("\nDecision event:")
            print("-" * 30)
            decision_event, rival_band = self.generate_decision_event()
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

            # Display resolution event
            print("\nResolution event:")
            print("-" * 30)
            print("After a thrilling performance, your band awaits the judges' final decision.")

# Main function to start the game
def main():
    game_instance = Game()
    game_instance.play()

if __name__ == "__main__":
    main()


#tests
import unittest
from unittest.mock import patch
from io import StringIO
from game import Band, Game

class TestBand(unittest.TestCase):
    def setUp(self):
        self.band = Band()

    def test_calculate_band_stats(self):
        user_band_members = ["Beatrice Groove", "Harmony Heart", "Melody Muse", "Axel Blaze"]
        total_performance, total_charisma, total_luck = self.band.calculate_band_stats(user_band_members)
        self.assertEqual(total_performance, 30)
        self.assertEqual(total_charisma, 27)
        self.assertEqual(total_luck, 18)

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    @patch('builtins.input', side_effect=['yes', 'The Melody Mansion', 'Beatrice Groove', 'Harmony Heart', 'Melody Muse', 'Axel Blaze', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_play_game(self, mock_stdout, mock_input):
        self.game.play()
        output = mock_stdout.getvalue()
        self.assertIn('Welcome to Battle of the Bands!!', output)
        self.assertIn('Great choice! Your band will perform at The Melody Mansion.', output)
        self.assertIn('Events during your performance:', output)
        self.assertIn('Decision event:', output)
        self.assertIn('Enter your choice:', output)
        self.assertIn('Resolution event:', output)

if __name__ == '__main__':
    unittest.main()
