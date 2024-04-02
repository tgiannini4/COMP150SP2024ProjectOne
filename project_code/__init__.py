import random
import unittest
from unittest.mock import patch
from io import StringIO
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
        self.user_accounts = {}
        self.legacy_points = 0
        self.username = ""
        self.band_venue = ""
        self.band_members = []

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
            self.logged_in_user = username  # Set the logged-in user
            return True
        else:
            print("Invalid username or password. Please try again.")
            return False

    def earn_legacy_points(self, points: int):
        """Earn legacy points."""
        self.user_accounts[self.logged_in_user]["legacy_points"] += points

    def spend_legacy_points(self, points: int):
        """Spend legacy points if enough are available."""
        if self.user_accounts[self.logged_in_user]["legacy_points"] >= points:
            self.user_accounts[self.logged_in_user]["legacy_points"] -= points
            print(f"{self.logged_in_user} spent {points} legacy points.")
        else:
            print(f"{self.logged_in_user} does not have enough legacy points.")
    
    def check_legacy_points(self):
        """Check the current amount of legacy points for the logged-in user."""
        print(f"{self.logged_in_user} has {self.user_accounts[self.logged_in_user]['legacy_points']} legacy points.")

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
            ("Your band has the chance to collaborate with a famous artist on a new song, but it requires changing your musical style. Do you:\n1. Stick to your current style and decline the collaboration.\n2. Embrace the opportunity to experiment with a new style and accept the collaboration.", "Chord Chaos")
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
        if random.random() < 0.5:  # 50% chance of winning
            print("Congratulations! Your band has won the Battle of the Bands competition!")
            self.earn_legacy_points(100)  # Example: Award legacy points for winning
            print("You've earned 100 legacy points for winning the competition!")
        else:
            print("Unfortunately, your band didn't win the Battle of the Bands competition. Better luck next time!")
            self.spend_legacy_points(50)  # Example: Deduct legacy points for losing
            print("You've spent 50 legacy points as a consolation for losing.")

def main():
    """Main function to start the game."""
    game_instance = Game()
    while True:
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        if game_instance.register_user(username, password):
            break  # Break the loop if registration is successful
    game_instance.play()

if __name__ == "__main__":
    main()



