
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

# from enum import Enum


# class EventStatus(Enum):
#     UNKNOWN = "unknown"
#     PASS = "pass"
#     FAIL = "fail"
#     PARTIAL_PASS = "partial_pass"


# class Event:

#         def __init__(self, parser, data: dict = None):



#             self.parser = parser
#             # parse json file
#             self.primary = data['primary_attribute']
#             self.secondary = data['secondary_attribute']
#             self.prompt_text = data['prompt_text']
#             self.pass_ = data['pass']
#             self.fail = data['fail']
#             self.partial_pass = data['partial_pass']


#             self.status = EventStatus.UNKNOWN
#             self.fail = {
#                 "message": "You failed."
#             }
#             self.pass_ = {
#                 "message": "You passed."
#             }
#             self.partial_pass = {
#                 "message": "You partially passed."
#             }
#             self.prompt_text = "A dragon appears, what will you do?"

#             self.primary: Statistic = Strength()
#             self.secondary: Statistic = Dexterity()

#         def execute(self, party):
#             chosed_one = self.parser.select_party_member(party)
#             chosen_skill = self.parser.select_skill(chosed_one)

#             self.set_status(EventStatus.PASS)
#             pass

#         def set_status(self, status: EventStatus = EventStatus.UNKNOWN):
#             self.status = status

#         def resolve_choice(self, party, character, chosen_skill):
#             # check if the skill attributes overlap with the event attributes
#             # if they don't overlap, the character fails
#             # if one overlap, the character partially passes
#             # if they do overlap, the character passes

#need a second type of parser method that handles certain number of choices to check if input is a choice and then do the choice (while loop)
#reask the question and not get broken code is the goal 

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

