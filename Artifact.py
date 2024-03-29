from Enum_classes import HistoricalSignificance, ExhibitionLocation
# imports ENUM class

# Created class for Artifact
class Artifact:
    """Class to represent artifacts in a museum"""

    # Constructor to initialize attributes for the class artifact
    def __init__(self, name, creator, year, historical_significance, exhibition_location,description):
        self._name = name
        self._creator = creator
        self._year = year
        self._description = description
        self._historical_significance = (HistoricalSignificance(historical_significance).name).replace("_", " ")
        self._exhibition_location = (ExhibitionLocation(exhibition_location).name).replace("_", " ")

    # Setters and getters
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name

    def set_creator(self, creator):
        self._creator = creator
    def get_creator(self):
        return self._creator

    def set_year(self, year):
        self._year = year
    def get_year(self):
        return self._year

    def set_description(self, description):
        self._description = description
    def get_description(self):
        return self._description

    def set_historical_significance(self, historical_significance):
        self._historical_significance = historical_significance
    def get_historical_significance(self):
        return self._historical_significance

    def set_exhibition_location(self, exhibition_location):
        self._exhibition_location = exhibition_location
    def get_exhibition_location(self):
        return self._exhibition_location

    # Displays the attributes if executed into print as string
    def __str__(self):
        return "Artifact: " + str(self._name) + "\nCreator: " + str(self._creator) + "\nYear: " + str(self._year)+"\nExhibition Location: "+self._exhibition_location + "\nDescription: " + self._description
