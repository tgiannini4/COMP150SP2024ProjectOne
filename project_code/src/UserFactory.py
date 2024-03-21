# # UserFactory.py
# from project_code.src.UserInputParser import UserInputParser
# from project_code.src.User import User


# class UserFactory:

#     @staticmethod
#     def create_user(parser: UserInputParser) -> User:
#         username = parser.parse("Enter a username: ")
#         password = parser.parse("Enter a password: ")
#         # Here you can add more logic as needed, e.g., validate input
#         return User(username, password)


# UserFactory.py
from project_code.src.UserInputParser import UserInputParser
from project_code.src.User import User

class UserFactory:

    @staticmethod
    def create_user(parser: UserInputParser) -> User:
        # Get username from user input using the parser
        username = ""
        while not username:  # Keep prompting until a non-empty username is provided
            username = parser.parse("Enter a username: ")
            if not username:
                print("Username cannot be empty.")
        
        # Get password from user input using the parser
        password = ""
        while not password:  # Keep prompting until a non-empty password is provided
            password = parser.parse("Enter a password: ")
            if not password:
                print("Password cannot be empty.")
        
        # Create and return a new User object with the obtained username and password
        return User(username, password)


