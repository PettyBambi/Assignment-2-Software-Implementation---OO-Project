from Artwork import Artwork
from Artifact import Artifact
from Enum_classes import ExhibitionLocation
from Visitor import Visitor
# imports classes to be used in this class


# created class for exhibition
class Exhibition:
    """Class to represent an exhibition in a museum"""

    # constructor to initialize attributes for future use
    def __init__(self, name, location, theme, duration,artworks,artifacts):
        self._name = name
        self._location = (ExhibitionLocation(location).name).replace("_", " ")
        self._theme = theme
        self._duration = duration
        self._artworks = artworks
        self._artifacts = artifacts

    # setters and getters
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name

    def set_location(self, location):
        self._location = location
    def get_location(self):
        return self._location

    def set_theme(self, theme):
        self._theme = theme
    def get_theme(self):
        return self._theme

    def set_duration(self, duration):
        self._duration = duration
    def get_duration(self):
        return self._duration

    def add_artwork(self, artworks):
        if self._artworks is not []:
            self._artworks.append(artwork)
    def get_all_artworks(self):
        return self._artworks

    def add_artifact(self, artifacts):
        if self._artifacts is not []:
            self._artifacts.append(artifact)
    def get_all_artifacts(self):
        return self._artifacts

    # display the attributes that may be present in the exhibition
    def __str__(self):
        if self._artworks is not []:
            artworks_info = "\nAll Artworks in the Exhibition:\n"
            for artwork in self._artworks:
                artworks_info += str(artwork) + "\n"+ "\n"
        else:
            artworks_info=" "
        if self._artifacts is not []:
            artifacts_info = "\nAll Artifacts in the Exhibition:\n"
            for artifact in self._artifacts:
                artifacts_info += str(artifact) + "\n"+ "\n"
        else:
            artifacts_info=" "
        return "Exhibition: " + self._name + "\n"+"Location: " + self._location + "\n"+"Theme: " + self._theme + "\n"+"Duration: " + self._duration+ "\n"+ artworks_info + artifacts_info



