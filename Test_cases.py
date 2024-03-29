from Museum_details import Museum_details
from Artifact import Artifact
from Artwork import Artwork
from Visitor import Visitor
from Tour import Tour
from Ticket import Ticket
from Exhibition import Exhibition
from Special_Event import Special_Event
# importing classes from different files

# creating visitors
visitor1 = Visitor("Maryam", "Ahmed", 23, "Emirati", 2, 2, True)
visitor2 = Visitor("Ahmed", "Saeed", 19, "Emirati", 1, 1, False)
visitor3 = Visitor("Brim", "Stone", 67, "American", 1, 3, True)

# creating artworks
artwork1 = Artwork("Starry Night", "Vincent van Gogh", "1889", 2, 3, "Oil on canvas depicting a night sky")
artwork2 = Artwork("The Persistence of Memory", "Salvador Dali", "1931", 3, 2, "Surrealist painting of melting clocks")
artwork3 = Artwork("The Creation of Adam", "Michelangelo", "1508-1512", 2, 1, "Fresco on the ceiling of the Sistine Chapel")
artwork4 = Artwork("Mona Lisa", "Leonardo da Vinci", "1503", 3, 3, "A portrait painting.")

# creating artifacts
artifact1 = Artifact("Statue of Zeus at Olympia", "Ancient Greece", "435 BC", 3, 1, "A giant seated figure of the Greek god Zeus, made by the sculptor Phidias.")
artifact2 = Artifact("Terracotta Army", "China", "210–209 BC", 1, 2, "A collection of terracotta sculptures depicting the armies of Qin Shi Huang, the first Emperor of China.")
artifact3 = Artifact("King Tutankhamun's Mask", "Ancient Egypt", "1323 BC", 3, 1, "A gold death mask of the 18th-dynasty Egyptian Pharaoh Tutankhamun.")

# creating exhibitions
exhibition1 = Exhibition("Ancient Egypt Exhibition", 2, "Ancient Egypt", "3 months", [artwork1, artwork3], [artifact1, artifact3])
exhibition2 = Exhibition("Surrealism Showcase", 3, "Modern Art", "2 months", [artwork2], [])
exhibition3 = Exhibition("Renaissance Revival", 1, "European Art", "4 months", [artwork3], [])

# creating special events
special_event1 = Special_Event("Emirati Cultural Festival", "2024-04-15", 1, "4 hours", "Celebrating Emirati heritage and traditions")
special_event2 = Special_Event("Musical Concert", "2024-04-01", 1, "2 hours", "A live performance by renowned artists")
special_event3 = Special_Event("Traditional Dance Performance", "2024-05-20", 1, "2 hours", "Showcasing Emirati dance forms")

# creating tours
tour1 = Tour("2024-04-05", 20, "Ahmed Ali", "Exploring the cultural heritage of the UAE.")
tour2 = Tour("2024-04-10", 15, "Emma Thompson", "Discovering ancient ruins and civilizations.")

# creating tickets
ticket1 = Ticket(visitor2)
ticket2 = Ticket(visitor2)
ticket3 = Ticket(visitor3)

# purchasing tickets for the exhibition, special event, and tour
ticket1.set_purchased_ticket(exhibition1, ["exhibition"])
ticket1.set_purchased_ticket(special_event2, ["special_event"])
ticket2.set_purchased_ticket(special_event3, ["special event"])
ticket3.set_purchased_ticket(tour1, ["tour"])
# Generate and print the receipt
# ticket1.generate_receipt()

# create and input museum details
museum_details = Museum_details("Louvre Museum", "Abu Dhabi, UAE", "10:00 AM - 5:00 PM")
museum_details.set_artworks([artwork1, artwork2, artwork3, artwork4])
museum_details.set_artifacts([artifact1, artifact2, artifact3])
museum_details.set_exhibitions([exhibition1, exhibition2, exhibition3])
museum_details.set_special_events([special_event1, special_event2, special_event3])
museum_details.set_tours([tour1, tour2])

# print(museum_details)
