
from enum import Enum 

class EventStatus(Enum):



class Event:
    def __init__(self, parser):
        self.parser = parser 
        self.fail = {
            ""
        }
        self.pass_ = {
            ""
        }
        self.partial_pass = {
            ""
        }
    self.prompt_text = "prompt"

    #self.primary: Stat
    pass

def execute(self, party):
    chosen_one = self.parser.select_party_member(party)
    chosen_skill = self.parser.select_skill(chosen_one)

    self.set_status(EventStatus.PASS)
    pass 



