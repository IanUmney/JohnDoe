import random
import string
import datetime


class JohnDoe():

    def __init__(self, **kwargs):
        self.mobile_number = str(kwargs.get("mobile_number", self.mobile_number()))
        self.ni_number = kwargs.get("ni_number", self.ni_number())
        self.address = kwargs.get("address", self.address())
        self.name = kwargs.get("name", self.name())
        self.bank_card = kwargs.get("bank_card", self.bank_card())
        self.age = kwargs.get("age", self.age())
        self.birthday = kwargs.get("birthday", self.birthday())
        self.driving_license = kwargs.get("driving_license",self.driving_license())
        self.email = kwargs.get("email", self.email())

    def create(self):
        return self.__dict__

    def mobile_number(self):
        '''Get a random phone number in UK format: 07 + 123456789'''

        mobile_number = "07"

        for _ in range(9):
            mobile_number += str(random.randint(0, 9))

        return mobile_number

    def ni_number(self):
        '''Gets string with the format of a national insurance
        number: AB123456C'''

        # random ascii char
        def rac():
            return random.choice(string.ascii_uppercase)

        return f"{rac()}{rac()}{random.randint(111_111, 999_999)}{rac()}"

    def address(self):
        '''Get random UK adrress information.
        Postcode and area are genuine.
        Street names are random choice from top 50'''

        # Get random house number
        house_number = random.randint(1, 500)

        # Get random street name
        _f = open("./src/streets.txt", "r")
        line = next(_f)
        for num, aline in enumerate(_f, 2):
            if random.randrange(num):
                continue
            street = aline.strip()
        _f.close()

        # Get random postcode and area
        with open("./src/postcodes.txt") as file:
            line = file.readlines()
            random_line = random.choice(line)

            postcode = random_line.strip().split(",")[0]
            area = random_line.strip().split(",")[1]

        address = {"house_number": house_number,
                    "street": street,
                    "area": area,
                    "postcode": postcode
                    }

        return address

    def name(self):
        '''Get a random name from the most common forenames
        and surnames in the UK'''

        # Get random forename
        with open("./src/forenames.txt") as forename_file:
            line = forename_file.readlines()
            random_name = random.choice(line).strip()

        # Get random surname
        with open("./src/surnames.txt") as surname_file:
            rl = surname_file.readlines()
            random_surname = random.choice(rl).strip()

        return f"{random_name} {random_surname}"

    def bank_card(self):
        '''Get genuine UK bank card information provider.
        Generate random 10 numbers to complete card.'''

        # Get genuine card number and provider
        with open("./src/cards.txt", "r") as file:
            rl = file.readlines()
            for x in rl:
                number = x.split(" ")[0].strip()
                provider = x.split(" ")[1].strip()

        # Concatonate random 10-digit number to complete card
        number = number + str(random.randint(0000_0000_00, 9999_9999_99))

        # Random expiry date
        expiry_date = str(random.randint(1, 12)) + \
            "/" + str(random.randint(22, 32))

        # Random CVV
        cvv = str(random.randint(123, 987))

        bank_card = {"card_number": number,
                    "provider": provider,
                    "expiry_date": expiry_date,
                    "cvv": cvv
                    }

        return bank_card

    def age(self):
        '''Random age'''

        return random.randint(18, 65)

    def birthday(self):
        '''Random birthday'''

        year = datetime.datetime.now().year - int(self.age)
        month = random.randint(1, datetime.datetime.now().month)
        day = random.randint(1, 28)

        # Always print double digit birthdays
        if day < 10:
            day = "0" + str(day)
        if month < 10:
            month = "0" + str(month)

        return f"{day}/{month}/{year}"

    def driving_license(self):
        '''Driving license according to UK format, for John Doe\'s details'''

        # The first five characters of the surname
        # (padded with 9s if less than 5 characters)
        if len(self.name.split(" ")[-1]) < 5:
            a = self.name.split(" ")[-1][:5].lower()
            while len(a) < 5:
                a += "9"
        else:
            a = self.name.split(" ")[-1][:5].lower()

        # The decade digit from the year of birth
        # (e.g. for 1987 it would be 8)
        b = self.birthday.split("/")[2][2]

        # The month of birth (7th character incremented
        # by 5 if driver is female i.e. 51–62 instead of 01–12)
        c = self.birthday.split("/")[1]

        # The date within the month of birth
        d = self.birthday.split("/")[0]

        # The year digit from the year of birth
        # (e.g. for 1987 it would be 7)
        e = self.birthday.split("/")[2][3]

        # The first two initials of the first names
        # (padded with a 9 if no middle name)
        f = "9"

        # Arbitrary digit – usually 9, but decremented to
        # differentiate drivers with the first 13 characters in common
        g = "9"

        # Two computer check digits
        h = f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}"

        # Appended, two digits representing the licence issue, which increases
        # by 1 for each licence issued
        i = f"{random.randint(1,9)}0"

        return "{}{}{}{}{}{}{}{} {}".format(a, b, c, d, e, f, g, h, i)

    def email(self):
        '''Random email based on name of John Doe'''

        # Email providers with UK TLD
        providers = ["yahoo.co.uk", "gmail.co.uk", "live.co.uk",
                    "hotmail.co.uk", "icloud.co.uk", "msn.co.uk"
                    ]

        provider = random.choice(providers)

        email = ".".join(self.name.split(" ")) + "@" + provider

        return email
