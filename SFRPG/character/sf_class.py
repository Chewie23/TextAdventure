class SFGenericClass():
    def __init__(self):
        self.sp = 6
        self.hp = 6
 
class Envoy(SFGenericClass):
    def __init__(self):
        self.proficiencies = {
            "armor": "light", 
            "weapon": ["basic melee", "grenades", "small arms"]
            }
        self.class_skills = [
            "Acrobatics",
            "Athletics",
            "Bluff",
            "Computers",
            "Culture",
            "Diplomacy",
            "Disguise",
            "Engineering",
            "Intimidate",
            "Medicine",
            "Perception",
            "Piloting",
            "Profession",
            "Sense Motive",
            "Sleight of Hand",
            "Stealth"
            ]
        self.class_feats = {"Envoy Improvisation": []}
        
                                                            
    