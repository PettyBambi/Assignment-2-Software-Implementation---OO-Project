from enum import Enum

class HistoricalSignificance(Enum):
    """Class to represent scale of importance"""
    MIN = "Minimal importance"
    MEDIUM = "Medium importance"
    HIGH = "High importance"

class ExhibitionLocation(Enum):
    """Class to represent artwork location"""
    PERMANENT_GALLERY = "Permanent Gallery"
    EXHIBITION_HALL = "Exhibition Hall"
    OUTDOOR_SPACE = "Outdoor Space"

class Museum_details:
    """Class to represent Museum"""
    def __init__(self, name, location, Museum_hours,artworks,exhibitions,pricing):
        self._name=name
        self._location = location
        self._Museum_hours = Museum_hours
        self._artworks = artworks
        self._exhibitions = exhibitions
        self._pricing = pricing

# Setters and getters
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name

    def set_location(self, location):
        self._location = location
    def get_location(self):
        return self._location

    def set_Museum_hours(self, Museum_hours):
        self._Museum_hours = Museum_hours
    def get_Museum_hours(self):
        return self._Museum_hours

    def set_artworks(self, artworks):
        self._artworks = artworks
    def get_artworks(self):
        return self._artworks

    def set_exhibitions(self, exhibitions):
        self._exhibitions = exhibitions
    def get_exhibitions(self):
        return self._exhibitions

    def set_pricing(self, pricing):
        self._pricing = pricing
    def get_pricing(self):
        return self._pricing

    def __str__(self):
        return "Name: " + str(self._name) +'\n'+"Location: " + str(self._location) + '\n'+"Museum Hours: " + str(self._Museum_hours) + '\n'+"Artworks: " + str(self._artworks) + '\n'+"Exhibitions: " + str(self._exhibitions) + '\n'+"Pricing: " + str(self._pricing)
class Artwork:
    """Class to represent artwork in a museum"""
    def __init__(self,title, artist, date_of_creation, historical_significance, exhibition_location):
        self._title= title
        self._artist = artist
        self._date_of_creation = date_of_creation
        self._historical_significance = historical_significance
        self._exhibition_location = exhibition_location

    # Setters and getters
    def set_title(self, title):
        self._title = title
    def get_title(self):
        return self._title

    def set_artist(self, artist):
        self._artist = artist
    def get_artist(self):
        return self._artist

    def set_date_of_creation(self, date_of_creation):
        self._date_of_creation = date_of_creation
    def get_date_of_creation(self):
        return self._date_of_creation

    def set_historical_significance(self, historical_significance):
        if historical_significance == historical_significance.MIN.value:
            self._exhibition_location=historical_significance.MIN.value
        elif historical_significance == historical_significance.MEDIUM.value:
            self._historical_significance = historical_significance.MEDIUM.value
        else:
            self._historical_significance = historical_significance.HiGH.value
    def get_historical_significance(self):
        return self._historical_significance

    def set_exhibition_location(self, exhibition_location):
        if exhibition_location == ExhibitionLocation.EXHIBITION_HALL.value:
            self._exhibition_location=ExhibitionLocation.EXHIBITION_HALL.value
        elif exhibition_location == ExhibitionLocation.OUTDOOR_SPACE.value:
            self._exhibition_location = ExhibitionLocation.OUTDOOR_SPACE.value
        else:
            self._exhibition_location = ExhibitionLocation.PERMANENT_GALLERY.value
    def get_exhibition_location(self):
        return self._exhibition_location

    def __str__(self):
        return "Title: " + str(self._title) + ", Artist: " + str(self._artist) + ", Date of Creation: " + str(self._date_of_creation) + ", Historical Significance: " + str(self._historical_significance.value) + ", Exhibition Location: " + str(self._exhibition_location.value)


