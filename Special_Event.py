from Enum_classes import ExhibitionLocation
# import enum class for location to be selected

# creating  class for special event
class Special_Event:
    """Class to represent a special event in a museum"""

    # constructor to initialize attributes
    def __init__(self, name, date, location, duration, description):
        self._name = name
        self._date = date
        self._duration = duration
        self._location = (ExhibitionLocation(location).name).replace("_", " ")
        self._description = description

    # Setters and getters
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name

    def set_date(self, date):
        self._date = date
    def get_date(self):
        return self._date

    def set_description(self, description):
        self._description = description
    def get_description(self):
        return self._description

    # method to display string attributes of the special event
    def __str__(self):
        return "Special Event: " + self._name + "\nDate: " + self._date + "\nLocation: " + self._location + "\nDuration: " + self._duration + "\nDescription: " + self._description


