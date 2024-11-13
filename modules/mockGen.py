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
]
streetTypes = [
    "Road",
    "Street",
    "Gali",
    "Avenue",
    "Colony",
    "Land",
    "Mark",
    "Elon",
    "Track",
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
    AddStudent(
        random.choice(firstNames),
        random.choice(lastNames),
        randomDate(start_date, end_date),
        random.choice(genders),
        randomAddress(),
        str(random.randint(1000000000, 9999999999)),
    )

conn.commit()
conn.close()
