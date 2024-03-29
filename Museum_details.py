# creating a class for information of the museum to be stored.
class Museum_details:
    """Class to represent Museum"""

    # Constructor to initialize attributes
    def __init__(self, name, location, museum_hours):
        self._name = name
        self._location = location
        self._museum_hours = museum_hours
        self._artworks = []
        self._exhibitions = []
        self._artifacts=[]
        self._special_events=[]
        self._tours = []


    # Setters and getters
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name

    def set_location(self, location):
        self._location = location
    def get_location(self):
        return self._location

    def set_museum_hours(self, museum_hours):
        self._museum_hours = museum_hours
    def get_museum_hours(self):
        return self._museum_hours

    def set_artifacts(self, artifacts):
        for artifact in artifacts:
            self._artifacts.append(artifact)
    def get_artifacts(self):
        return self._artifacts

    def set_exhibitions(self, exhibitions):
        for exhibition in exhibitions:
            self._exhibitions.append(exhibition)
    def get_exhibitions(self):
        return self._exhibitions

    def set_artworks(self, artworks):
        for artwork in artworks:
            self._artworks.append(artwork)
    def get_artworks(self):
        return self._artworks

    def set_special_events(self, special_events):
        for event in special_events:
            self._special_events.append(event)
    def get_special_events(self):
        return self._special_events

    def set_tours(self, tours):
        for tour in tours:
            self._tours.append(tour)
    def get_tours(self):
        return self._tours

    def list_exhibitions(self):
        print("All exhibitions in the Museum:")
        for exhibitions in self._exhibitions:

            print(exhibitions,"\n")
    def list_artifacts(self):
        print("All artifacts in the Museum:")
        for artifacts in self._artifacts:
            print(artifacts,"\n")

    def list_artworks(self):
        print("All Artworks in the Museum:")
        for artwork in self._artworks:
            print(artwork,"\n")

    def list_special_events(self):
        print("All special events in the Museum:")
        for artwork in self._artworks:
            print(artwork,"\n")

    def list_tours(self):
        print("All tours in the Museum:")
        for tour in self._tours:
            print(tour)

    # method to display string details of the museum
    def __str__(self):
        return "Name: " + str(self._name) + '\n' + "Location: " + str(self._location) + '\n' + "Museum Hours: " + str(self._museum_hours) + '\n' + "Number of Artworks: " + str( len(self._artworks)) + '\n' + "Number of Exhibitions: " + str(len(self._exhibitions)) + '\n' + "Number of Artifacts: " + str(len(self._artifacts)) + '\n' + "Number of Special Events: " + str(len(self._special_events)) + '\n' + "Number of Tours: " + str(len(self._tours))
