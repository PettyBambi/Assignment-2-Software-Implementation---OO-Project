# imports ENUM class
from Enum_classes import HistoricalSignificance, ExhibitionLocation

# Creating a class for Artwork
class Artwork:
    """Class to represent artwork in a museum"""
    all_artworks = [] # To store all artworks

    # constructor to initialize attributes for the class artwork
    def __init__(self, title, artist, date_of_creation, historical_significance, exhibition_location,description):
        self._title = title
        self._artist = artist
        self._date_of_creation = date_of_creation
        self._description = description
        self._historical_significance = (HistoricalSignificance(historical_significance).name).replace("_", " ")
        self._exhibition_location = (ExhibitionLocation(exhibition_location).name).replace("_", " ")
        Artwork.all_artworks.append(self)

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
        self._historical_significance = historical_significance

    def get_historical_significance(self):
        return self._historical_significance

    def set_exhibition_location(self, exhibition_location):
        self._exhibition_location = exhibition_location

    def get_exhibition_location(self):
        return self._exhibition_location

    def set_description(self, description):
        self._description = description
    def get_description(self):
        return self._description

    # Displays the attributes if executed into print as string
    def __str__(self):
        return "Title: " + str(self._title) + "\nArtist: " + str(self._artist) + "\nDate of Creation: " + str(self._date_of_creation) + "\nDescription: " + self._description + "\nHistorical Significance: " + self._historical_significance + "\nExhibition Location: " + self._exhibition_location

