from enum import Enum


class HistoricalSignificance(Enum):
    """Class to represent scale of importance"""
    Low_Importance = "L"
    Medium_Importance = "M"
    High_Importance = "H"


class ExhibitionLocation(Enum):
    """Class to represent artwork location"""
    Permanent_Gallery = "PG"
    Exhibition_Hall = "EH"
    Outdoor_Space = "OS"


class Gender_f_m(Enum):
    """Class to represent gender"""
    Male = "M"
    Female = "F"


class Museum_details:
    """Class to represent Museum"""

    def __init__(self, name, location, Museum_hours, artworks, exhibitions, pricing):
        self._name = name
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
        return "Name: " + str(self._name) + '\n' + "Location: " + str(self._location) + '\n' + "Museum Hours: " + str(
            self._Museum_hours) + '\n' + "Artworks: " + str(self._artworks) + '\n' + "Exhibitions: " + str(
            self._exhibitions) + '\n' + "Pricing: " + str(self._pricing)


class Artwork:
    """Class to represent artwork in a museum"""
    all_artworks = []

    def __init__(self, title, artist, date_of_creation, historical_significance, exhibition_location):
        self._title = title
        self._artist = artist
        self._date_of_creation = date_of_creation
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

    def __str__(self):
        return "Title: " + str(self._title) + ", Artist: " + str(self._artist) + ", Date of Creation: " + str(
            self._date_of_creation) + ", Historical Significance: " + self._historical_significance + ", Exhibition Location: " + self._exhibition_location


class Visitor:
    """Class to represent a visitor"""

    def __init__(self, first_name, last_name, age, nationality, gender, visitor_type):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._nationality = nationality
        self._gender = Gender_f_m(gender).name
        self._visitor_type = visitor_type

    # Setters and getters
    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_last_name(self):
        return self._last_name

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_nationality(self, nationality):
        self._nationality = nationality

    def get_nationality(self):
        return self._nationality

    def set_gender(self, gender):
        self._gender = gender

    def get_gender(self):
        return self._gender

    def set_visitor_type(self, visitor_type):
        self._visitor_type = visitor_type

    def get_visitor_type(self):
        return self._visitor_type

    def __str__(self):
        return "Name: " + str(self._first_name) + " " + str(self._last_name) + ", Age: " + str(
            self._age) + ", Nationality: " + str(self._nationality) + ", Gender: " + self._gender


class Ticket:
    """Class to represents a ticket"""

    def __init__(self, visitor, artwork, ticket_type):
        self._visitor = visitor
        self._artwork = artwork
        self._ticket_type = ticket_type
        self._ticket_price = 0
        self._purchased_tickets = []

    def set_price_ticket(self):
        ticket_price = 0
        if self._visitor.get_age() < 18 or self._visitor.get_age() >= 60 or self._visitor.get_visitor_type() in [
            "teacher", "student"]:
            return ticket_price

        base_price = 63
        if self._ticket_type == "special event":
            base_price += 50
        if self._ticket_type == "group":
            base_price *= 0.5
        ticket_price = base_price * 1.05
        self._ticket_price = ticket_price
        return self._ticket_price

    def get_price_ticket(self):
        return self._ticket_price

    def set_purchased_ticket(self):
        price = self.set_price_ticket()
        self._purchased_tickets.append((self._artwork.get_title(), self._ticket_type, price))

    def get_purchased_tickets(self):
        return self._purchased_tickets

    def generate_receipt(self):
        print("Visitor:", self._visitor.get_first_name(), self._visitor.get_last_name())
        print("Artwork:", self._artwork.get_title())
        print("Ticket Type:", self._ticket_type)
        print("Ticket Price:", 63, "AED")
        if self._ticket_type == "special event":
            print("Special event: 50 AED")
        elif self._ticket_type == "group":
            print("Group discount: 5%")
        else:
            pass
        print("Vat: 1.05")
        if self._ticket_price == 0:
            print("Eligible for free ticket (elder, minor, teacher, or student)")
        total_bill = self._ticket_price
        print("Total Bill:", total_bill, "AED")
        print("\n")



