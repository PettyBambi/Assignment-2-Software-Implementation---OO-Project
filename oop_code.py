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

