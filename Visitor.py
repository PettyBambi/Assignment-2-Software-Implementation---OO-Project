from Enum_classes import Gender_f_m,Visitortype
# import enum class to determine gender and visitor type easily

# creating a class for information for the Visitor to be stored.
class Visitor:
    """Class to represent a visitor"""

    # constructor to initialize attributes
    def __init__(self, first_name, last_name, age, nationality, gender, visitor_type,national_id_presented):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._nationality = nationality
        self._gender = Gender_f_m(gender).name
        self._visitor_type = Visitortype(visitor_type).name
        self._national_id_presented=national_id_presented

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

    def set_national_id_presented(self, national_id_presented):
        self._national_id_presented = national_id_presented
    def get_national_id_presented(self):
        return self._national_id_presented

    # method to display the attributes for the visitor when printed
    def __str__(self):
        return self._visitor_type + " Name: " + str(self._first_name) + " " + str(self._last_name) + ", Age: " + str(self._age) + ", Nationality: " + str(self._nationality) + ", Gender: " + self._gender + ", National ID Presented: " + str(self._national_id_presented)


