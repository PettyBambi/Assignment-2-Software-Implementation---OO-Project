# creating class for ticket
class Ticket:
    """Class to represents a ticket"""


    # constructor to initialize attributes
    def __init__(self, visitor):
        self._visitor = visitor
        self._purchased_tickets = []

    # calculates the set price comparing and checks with conditions
    def set_price_ticket(self, ticket_type):
        ticket_price = 0
        # Checking if the visitor qualifies for a free ticket
        if self._visitor.get_age() < 18 or self._visitor.get_age() >= 60 or self._visitor.get_visitor_type() in [
            "teacher", "student"]:
            if self._visitor.get_national_id_presented():
                return ticket_price

        # Base price for adults
        base_price = 63
        if ticket_type == "special event":
            base_price += 15
        elif ticket_type == "group" or ticket_type == "tour":
            base_price *= 0.5
        ticket_price = base_price * 1.05
        return ticket_price  # Return the calculated ticket price
    def get_price_ticket(self):
        return self._ticket_price

    # buys tickets to be purchased
    def set_purchased_ticket(self, item, ticket_types):
        total_price = 0
        for ticket_type in ticket_types:
            price = self.set_price_ticket(ticket_type)
            self._purchased_tickets.append((item, ticket_type, price))
            total_price += price
        return total_price

    # calculating the correct price individually
    def individual_ticket_price(self, index):
        if 0 <= index < len(self._purchased_tickets):
            return self._purchased_tickets[index][2]  # Return the price of the ticket at the specified index
        else:
            return None
    def total_bill(self):
        total_bill = sum(ticket[2] for ticket in self._purchased_tickets)
        return total_bill

    # method to display string attributes of the ticket such as price
    def generate_receipt(self):
        print("Visitor:", self._visitor.get_first_name(), self._visitor.get_last_name())
        for purchased_ticket in self._purchased_tickets:
            print("Item:", purchased_ticket[0])
            print("Ticket Type:", purchased_ticket[1])
            print("Ticket Price:", purchased_ticket[2], "AED")
            if purchased_ticket[1] == "special event":
                print("Special event: 15AED")
            elif purchased_ticket[1] == "group":
                print("Group discount: 5%")
            elif purchased_ticket[1] == "tour":
                print("Tour discount: 50%")
            else:
                pass
            print("Vat: 1.05")
            if purchased_ticket[2] == 0:
                print("Eligible for free ticket (elder, minor, teacher, or student), national ID presented")
            else:
                print("Not eligible for free ticket (elder, minor, teacher, or student), no national ID presented")
        print("Total Bill:", self.total_bill(), "AED\n")





