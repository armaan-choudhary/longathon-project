from dataFunctions import *
import random
import datetime

firstNames = [
    "Dhruv",
    "Joe",
    "Linda",
    "Kushagra",
    "Mannan",
    "John",
    "Rudra",
    "Kanav",
    "Ishika",
    "Tanisha",
    "Armaan",
    "Arjun",
    "Trisha",
    "Anjali",
    "Basmati",
    "Somwati",
    "Raj",
    "Rohan",
    "Mohan",
    "Soham",
    "Rohika",
    "Zehi",
    "Bangu",
    "Kamles",
    "Rajesh",
    "Shloka",
    "Robert",
    "Mary",
    "David",
    "Linda",
    "James",
    "Elizabeth",
    "Michael",
    "Emily",
    "William",
    "Sarah",
    "Richard",
    "Jessica",
    "Joseph",
    "Jennifer",
    "Charles",
    "Amanda",
    "Thomas",
    "Melissa",
]
lastNames = [
    "Saini",
    "Doe",
    "Smith",
    "Choudhary",
    "Kumar",
    "Patel",
    "Singh",
    "Lal",
    "Chhabra",
    "Chattopadhyay",
    "Hemsworth",
    "Donald",
    "Whimsley",
    "Joota",
    "Jokung",
    "Funcha",
    "Lancho",
    "Makimoc",
    "Surlipreet",
    "Saxena",
    "Kant",
    "Aquagaurd",
    "Pure",
    "Lendi",
    "Williams",
    "Brown",
    "Jones",
    "Miller",
    "Davis",
    "Garcia",
    "Rodriguez",
    "Martinez",
    "Hernandez",
    "Lopez",
    "Gonzalez",
    "Wilson",
    "Anderson",
    "Thomas",
    "Taylor",
    "Moore",
    "Jackson",
    "Martin",
]
genders = ["Male", "Female"]
streets = [
    "Kamla",
    "Vimal",
    "Rajnigandha",
    "Market",
    "Munch",
    "Perk",
    "Pearson",
    "Limca",
    "Coca",
    "Lenovo",
    "Aarushi",
    "Mahatama",
    "Wall",
    "Tower",
    "Chezck",
    "Xerope",
    "Systum",
    "Makie",
    "Chunni",
    "Main",
    "Central",
    "Park",
    "Hill",
    "River",
    "Forest",
    "Lake",
    "Ocean",
    "Sky",
    "Star",
    "Moon",
    "Sun",
    "Earth",
    "Mars",
    "Venus",
    "Jupiter",
    "Saturn"
]
streetTypes = [
    "Road",
    "Street",
    "Gali",
    "Avenue",
    "Colony",
    "Lane",
    "Alley",
    "Boulevard",
    "Drive",
    "Circle",
    "Court",
    "Crescent",
    "Esplanade",
    "Expressway",
    "Freeway",
    "Highway",
    "Mall",
    "Parkway",
    "Place",
    "Plaza",
    "Ridge",
    "Row",
    "Square",
    "Terrace",
    "Trail",
    "Turnpike",
    "Viaduct",
    "Way"
]


def randomDate(start, end):
    time_between_dates = end - start
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d")


start_date = datetime.date(2000, 1, 1)
end_date = datetime.date(2024, 12, 31)


def randomAddress():
    return (
        str(random.randint(100, 999))
        + " "
        + random.choice(streets)
        + " "
        + random.choice(streetTypes)
    )


n = int(input("Enter Number of Entries : "))

for i in range(n):
    AddParent(
        random.choice(firstNames),
        random.choice(lastNames),
        # randomDate(start_date, end_date),
        # random.choice(genders),
        randomAddress(),
        str(random.randint(1000000000, 9999999999)),
    )

conn.commit()
conn.close()
