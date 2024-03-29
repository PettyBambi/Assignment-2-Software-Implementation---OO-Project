from enum import Enum
# imports enum to create classes of enum of options

# Class to represent the scale of importance
class HistoricalSignificance(Enum):
    """Class to represent scale of importance"""
    Low_Importance = 1
    Medium_Importance = 2
    High_Importance = 3

# Class to represent the location of artwork
class ExhibitionLocation(Enum):
    """Class to represent artwork location"""
    Permanent_Gallery = 1
    Exhibition_Hall = 2
    Outdoor_Space = 3

# Class to represent gender
class Gender_f_m(Enum):
    """Class to represent gender"""
    Male = 1
    Female = 2

# Class to represent types of visitors
class Visitortype(Enum):
    """Class to represent types of visitors"""
    student=1
    teacher=2
    regular=3

