# creates tour class
class Tour:
    """Class to represent a tour"""


    # constructor to initialize attributes
    def __init__(self, date, max_capacity, guide, description):
        self._date = date
        self._max_capacity = max_capacity
        self._guide = guide
        self._visitors = []
        self._description = description

    # setters and getters
    def set_date(self, date):
        self._date = date
    def get_date(self):
        return self._date

    def set_max_capacity(self, max_capacity):
        self._max_capacity = max_capacity
    def get_max_capacity(self):
        return self._max_capacity

    def set_guide(self, guide):
        self._guide = guide
    def get_guide(self):
        return self._guide

    # adds visitor to the list if there is space
    def add_visitor(self, visitor):
        if len(self._visitors) < self._max_capacity:
            self._visitors.append(visitor)
            return True
        else:
            return False
    def get_visitors(self):
        return self._visitors

    def set_description(self, description):
        self._description = description
    def get_description(self):
        return self._description

    # method to display string attributes of the new tour
    def __str__(self):
        return "Tour Date: " + str(self._date) + "\nMax Capacity: " + str(self._max_capacity) + "\nGuide: " + self._guide + "\nDescription: " + self._description + "\nNumber of Visitors: " + str(len(self._visitors))