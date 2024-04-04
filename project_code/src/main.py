
import random
import unittest
from unittest.mock import patch
from io import StringIO
import json

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
        self.username = ""
        self.band_venue = ""
        self.band_members = []
        self.user_accounts = self.load_user_accounts()
        self.user_data = {}
        self.logged_in_user = None

    def load_user_data(self):
        """Load user data."""
        try:
            with open('user_data.json', 'r') as file:
                self.user_data = json.load(file)
        except FileNotFoundError:
            # Handle file not found error
            print("User data file not found. Initializing with empty data.")


    def load_user_accounts(self):
        """Load user accounts from JSON file."""
        try:
            with open('user_accounts.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}  # Return empty dictionary if file not found

    
    def save_user_accounts(self):
        """Save user accounts to JSON file."""
        with open('user_accounts.json', 'w') as file:
            json.dump(self.user_accounts, file, indent=4)

    def register_user(self, username, password):
        """Register a new user."""
        if username not in self.user_accounts:
            self.user_accounts[username] = {"password": password, "legacy_points": 0}
            print(f"User '{username}' registered successfully.")
            return True
        else:
            print("Username already exists. Please choose a different username.")
            return False

    def login(self, username, password):
        """Login an existing user."""
        if username in self.user_accounts and self.user_accounts[username]["password"] == password:
            print("Login successful!")
            self.logged_in_user = username
            self.check_legacy_points() 
            return True
        else:
            print("Invalid username or password. Please try again.")
            return False
    
    def earn_legacy_points(self, points: int):
        """Earn legacy points."""
        if self.logged_in_user in self.user_accounts:
            self.user_accounts[self.logged_in_user]["legacy_points"] += points
            self.save_user_accounts()  # Update JSON file after earning points


    def spend_legacy_points(self, points: int):
        """Spend legacy points if enough are available."""
        if self.logged_in_user in self.user_accounts:
            if self.user_accounts[self.logged_in_user]["legacy_points"] >= points:
                self.user_accounts[self.logged_in_user]["legacy_points"] -= points
                print(f"{self.logged_in_user} spent {points} legacy points.")
                self.save_user_accounts()  # Update JSON file after spending points
            else:
                print(f"{self.logged_in_user} does not have enough legacy points.")

    
 

    def check_legacy_points(self):
        """Check the current amount of legacy points for the logged-in user."""
        if self.logged_in_user in self.user_accounts:
            legacy_points = self.user_accounts[self.logged_in_user]['legacy_points']
            print(f"{self.logged_in_user} has {legacy_points} legacy points.")
        else:
            print("User not found.")  # Display error message if user not found



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
            ("A rival band, Harmony Havoc, has spread false rumors about your band, causing doubt among your fans. Do you:\n1. Ignore the rumors and focus on your performance.\n2. Address the rumors publicly to clear your band's name.", "Harmony Havoc"),
            ("Your band has been offered a last-minute opportunity to perform at a prestigious event, but it conflicts with a personal commitment of one of your band members. Do you:\n1. Decline the offer to honor the commitment.\n2. Accept the offer and find a replacement for the conflicted band member.", "Serenade Syndicate"),
            ("Your band has the chance to collaborate with a famous artist on a new song, but it requires changing your musical style. Do you:\n1. Stick to your current style and decline the collaboration.\n2. Embrace the opportunity to experiment with a new style and accept the collaboration.", "Chord Chaos"),
            ("Your band is invited to participate in a charity concert, but it falls on the same day as your biggest rival's comeback tour. Do you:\n1. Decline the invitation to avoid confrontation.\n2. Accept the invitation and use it as an opportunity to outshine your rival.", "Voltage Vandals"),
            ("Your band is offered a chance to headline a music festival, but it requires signing an exclusive contract that limits your creative freedom. Do you:\n1. Reject the offer to maintain artistic integrity.\n2. Accept the offer for the exposure and opportunity.", "Sonic Surge"),
            ("A music producer offers to sign your band, but it means replacing one of your current band members with their preferred choice. Do you:\n1. Decline the offer to stay loyal to your band members.\n2. Accept the offer for the chance at stardom.", "Resonance Records"),
            ("Your band is invited to play at a high-profile event, but it requires wearing costumes and performing a gimmicky routine. Do you:\n1. Decline the offer to preserve your band's image.\n2. Accept the offer for the exposure and opportunity.", "Starlight Showcase")
        ]
        return random.choice(decision_events)

    def play(self):
        """Main method to start the game."""
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        # Attempt to log in
        if not self.login(username, password):
            return

        # If login successful, prompt the user to start the game
        ans = input('Would you like to play Battle of the Bands? (yes/no)')
        if ans.lower() == 'yes':
            print('Welcome to Battle of the Bands!!')
            print_ascii_art()
            print(f"Hello, {username}!")

            # Continue with the game
            self.start_game(username)

    
   

    # def play(self):
    #     """Main method to start the game."""
    #     while True:
    #         username = input("Enter your username: ")
    #         password = input("Enter your password: ")
            
    #         # Attempt to log in
    #         if self.login(username, password):
    #             print("Welcome to Battle of the Bands!!")
    #             print_ascii_art()
    #             print(f"Hello, {username}!")
    #             break  # Exit the loop if login is successful

    #         # If login unsuccessful, prompt for registration
    #         ans = input("Would you like to register as a new user? (yes/no)")
    #         if ans.lower() == 'yes':
    #             if self.register_user(username, password):
    #                 # Log in the newly registered user
    #                 self.login(username, password)
    #                 print("Welcome to Battle of the Bands!!")
    #                 print_ascii_art()
    #                 print(f"Hello, {username}!")
    #                 break  # Exit the loop after successful registration and login
    #             else:
    #                 continue  # Retry registration if unsuccessful
    #         else:
    #             print("Please try again.")
    #             continue  # Retry login if unsuccessful

            
    def calculate_band_stats(self, user_band_members):
        # Calculate the band stats based on the user's band members
        total_performance = sum(self.band.band_members_stats[member]["performance"] for member in user_band_members)
        total_charisma = sum(self.band.band_members_stats[member]["charisma"] for member in user_band_members)
        total_luck = sum(self.band.band_members_stats[member]["luck"] for member in user_band_members)
        return total_performance, total_charisma, total_luck

    def start_game(self, username):
        """Start the game."""
        print("You have been chosen to be the manager of the next hottest band for Resonance Records!")
        band_name = input("Before we begin, please enter your band's name: ")

        print(f"Great choice! Your band {band_name} is about to rock the stage!")
        print("But before Resonance Records signs your band, you have to prove your band has what it takes in the Battle of the Bands competition!")
        print("To enter the Battle of the Bands competition, first you have to form a band. Select 4 musicians for your band:")

        # Select band members
        user_band_members = self.select_band_members()

        # Display selected band members
        self.display_selected_band_members(user_band_members)

        # Select band venue
        selected_venue = self.select_band_venue()
        if not selected_venue:
            return

    
    
        # Calculate band stats
        band_stats = self.calculate_band_stats(user_band_members)

        # Generate and display events during performance
        self.display_performance_events(band_stats)

        # Generate and display decision event
        decision_event, rival_band = self.generate_decision_event()
        print("\nDecision event:")
        print("-" * 30)
        print(decision_event)

        # Take action based on decision event
        self.take_decision_action()

        # Display resolution event
        print("\nResolution event:")
        print("-" * 30)
        print("After a thrilling performance, your band awaits the judges' final decision.")

        # Determine outcome of the competition
        self.determine_competition_outcome()

    def select_band_members(self):
        """Select band members for the user's band."""
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
        return user_band_members


    def display_selected_band_members(self, user_band_members):
        """Display the selected band members."""
        print("\nYour selected band members are:")
        for member in user_band_members:
            print(member)

    def select_band_venue(self):
        """Select a band venue for the performance."""
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
            print(f"Great choice! Your band will perform at {selected_venue}.")
            return selected_venue
        else:
            print("Invalid venue selection. Please choose from the available options.")
            return None

    def display_performance_events(self, band_stats):
        """Generate and display events during the band's performance."""
        print("\nEvents during your performance:")
        print("-" * 30)
        for _ in range(3):  # Generate 3 events
            print(self.generate_event(band_stats))

    def take_decision_action(self):
        """Take action based on the decision event."""
        action = input("Enter your choice: ")
        if action == "1":
            print("You chose to ignore the rumors and focus on your performance.")
            # Perform action 1
        elif action == "2":
            print("You chose to address the rumors publicly to clear your band's name.")
            # Perform action 2
        else:
            print("Invalid choice. Please choose either 1 or 2.")

    def determine_competition_outcome(self):
        """Determine the outcome of the competition."""
        print("\nResolution event:")
        print("-" * 30)
        # Simulate winning or losing based on random chance
        if random.random() < 0.75:  # 75% chance of winning
            print("Congratulations! Your band has won the Battle of the Bands competition!")
            self.earn_legacy_points(100)  # Earn 100 legacy points for winning
            print("You've earned 100 legacy points for winning the competition!")
        else:
            print("Unfortunately, your band didn't win the Battle of the Bands competition. Better luck next time!")
            self.spend_legacy_points(50)  # Spend 50 legacy points as a consolation for losing
            print("You've spent 50 legacy points as a consolation for losing.")

def main():
    """Main function to start the game."""
    game_instance = Game()
    game_instance.play()

if __name__ == "__main__":
    main()

#unit tests 
    
# class TestGame(unittest.TestCase):

#     def setUp(self):
#         # Initialize a Game instance
#         self.game = Game()

#     def test_register_user(self):
#         # Test registering a new user
#         username = "test_user"
#         password = "test_password"
#         self.assertTrue(self.game.register_user(username, password))
        
#         # Test registering an existing user
#         self.assertFalse(self.game.register_user(username, password))

#     def test_login(self):
#         # Test logging in with correct credentials
#         username = "test_user"
#         password = "test_password"
#         self.game.register_user(username, password)
#         self.assertTrue(self.game.login(username, password))

#         # Test logging in with incorrect credentials
#         self.assertFalse(self.game.login(username, "wrong_password"))
#         self.assertFalse(self.game.login("wrong_username", password))

#     def test_earn_legacy_points(self):
#         # Test earning legacy points
#         initial_points = self.game.user_accounts.get(self.game.logged_in_user, {}).get("legacy_points", 0)
#         self.game.earn_legacy_points(50)
#         updated_points = self.game.user_accounts.get(self.game.logged_in_user, {}).get("legacy_points", 0)
#         self.assertEqual(updated_points, initial_points + 50)

#     def test_spend_legacy_points(self):
#         # Test spending legacy points
#         self.game.user_accounts[self.game.logged_in_user]["legacy_points"] = 100
#         initial_points = self.game.user_accounts.get(self.game.logged_in_user, {}).get("legacy_points", 0)
#         self.game.spend_legacy_points(50)
#         updated_points = self.game.user_accounts.get(self.game.logged_in_user, {}).get("legacy_points", 0)
#         self.assertEqual(updated_points, initial_points - 50)

#     def test_load_user_data(self):
#         # Test loading user data from file
#         self.game.load_user_data()
#         self.assertIsInstance(self.game.user_data, dict)

#     def test_load_user_accounts(self):
#         # Test loading user accounts from file
#         self.assertIsInstance(self.game.load_user_accounts(), dict)

#     def test_save_user_accounts(self):
#         # Test saving user accounts to file
#         self.game.user_accounts = {"test_user": {"password": "test_password", "legacy_points": 0}}
#         self.game.save_user_accounts()
#         with open('user_accounts.json', 'r') as file:
#             saved_data = json.load(file)
#             self.assertEqual(saved_data, {"test_user": {"password": "test_password", "legacy_points": 0}})

#     def test_check_legacy_points(self):
#         # Test checking legacy points for a user
#         self.game.user_accounts["test_user"] = {"password": "test_password", "legacy_points": 50}
#         with patch('sys.stdout', new=StringIO()) as fake_out:
#             self.game.logged_in_user = "test_user"
#             self.game.check_legacy_points()
#             self.assertIn("50", fake_out.getvalue())

#     def test_generate_event(self):
#         # Test generating an event
#         band_stats = (20, 15, 10)  # Placeholder band stats
#         event = self.game.generate_event(band_stats)
#         self.assertIsInstance(event, str)

#     def test_generate_decision_event(self):
#         # Test generating a decision event
#         decision_event, rival_band = self.game.generate_decision_event()
#         self.assertIsInstance(decision_event, str)
#         self.assertIsInstance(rival_band, str)

#     def test_select_band_members(self):
#         # Test selecting band members
#         with patch('builtins.input', side_effect=["Beatrice Groove", "Harmony Heart", "Melody Muse", "Axel Blaze"]):
#             band_members = self.game.select_band_members()
#             self.assertEqual(len(band_members), 4)

#     def test_select_band_venue(self):
#         # Test selecting a band venue
#         with patch('builtins.input', return_value="The Melody Mansion"):
#             selected_venue = self.game.select_band_venue()
#             self.assertEqual(selected_venue, "The Melody Mansion")

#     def test_start_game(self):
#         # Test starting the game
#         with patch('builtins.input', side_effect=["TestUser", "TestPassword", "yes", "TestBand", "1"]):
#             self.game.play()
#             self.assertEqual(self.game.band_venue, "The Melody Mansion")  # Assuming the user selects the first venue


# if __name__ == '__main__':
#     unittest.main()