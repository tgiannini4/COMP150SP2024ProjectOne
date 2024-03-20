from typing import List

from project_code.src.Character import Character
from project_code.src.Event import Event
from project_code.src.Location import Location


class Game:

    def __init__(self):
        self.characters: List[Character] = []
        self.locations: List[Location] = []
        self.events: List[Event] = []
        self.party: List[Character] = []
        self.current_location = None
        self.current_event = None
        self._initialize_game()
        self.continue_playing = True

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
        pass

    def start_game(self):
        return self._main_game_loop()

    # def _main_game_loop(self):
    #     """The main game loop."""
    #     while self.continue_playing:
    #         pass
    #         # ask for user input
    #         # parse user input
    #         # update game state
    #         # check if party is all dead
    #         # if part is dead, award legacy points and end instance of game
    #         # if party is not dead, continue game
    #     if self.continue_playing is False:
    #         return True
    #     elif self.continue_playing == "Save and quit":
    #         return "Save and quit"
    #     else:
    #         return False
        
    def _main_game_loop(self):
        """The main game loop."""
        while self.continue_playing:
            # Ask for user input
            user_input = input("What do you want to do? ")
        
            # Parse user input
            parsed_input = self.parse_user_input(user_input)
        
            # Update game state based on parsed input
            self.update_game_state(parsed_input)
        
            # Check if party is all dead
            if self.is_party_dead():
                # Award legacy points
                self.award_legacy_points()
                # End instance of game
                self.continue_playing = False
                print("Your party has been defeated. Game over.")
                break  # Exit the loop
            
            # Check if user wants to save and quit
            if self.continue_playing == "Save and quit":
                print("Saving game...")
                self.save_game_state()
                print("Game saved. Goodbye!")
                return "Save and quit"  # Exit the loop
        
            # Continue game
            # Implement the rest of the game logic here

    # Handle game ending conditions
        if self.continue_playing is False:
            return True
        elif self.continue_playing == "Save and quit":
            return "Save and quit"
        else:
            return False









