import random
import string
import datetime


class JohnDoe():

    def __init__(self, **kwargs):
        self.mobile_number = kwargs.get("mobile_number", self.mobile_number())
        self.ni_number = kwargs.get("ni_number", self.ni_number())
        self.address = kwargs.get("address", self.address())
        self.name = kwargs.get("name", self.name())
        self.bank_card = kwargs.get("bank_card", self.bank_card())
        self.age = kwargs.get("age", self.age())
        self.birthday = kwargs.get("birthday", self.birthday())

    def create(self):
        return {
                "name": self.name,
                "address": self.address,
                "phone_number": self.mobile_number,
                "ni_number": self.ni_number,
                "bank_card": self.bank_card,
                "age": self.age,
                "birthday": self.birthday
                }

    def mobile_number(self):
        '''Get a random phone number in UK format: 07 + 123456789'''
        mobile_number = "07"

        for _ in range(9):
            mobile_number += str(random.randint(0, 9))
        return mobile_number

    def ni_number(self):
        '''Gets string with the format of a national insurance
        number: AB123456C'''
        def rac():  # random ascii char
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

        # Get random postcode and area
        with open("./src/postcodes.txt") as file:
            line = file.readlines()
            random_line = random.choice(line)

            postcode = random_line.strip().split(",")[0]
            area = random_line.strip().split(",")[1]

        return(f"{house_number} {street}, {area}, {postcode}")

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

        return f"{number} - {provider} Expiry:{expiry_date} CVV:{cvv}"

    def age(self):
        '''Random age'''
        return str(random.randint(18, 65))

    def birthday(self):
        '''random birthday'''
        year = datetime.datetime.now().year - int(self.age)
        month = random.randint(1, datetime.datetime.now().month)
        day = random.randint(1, 28)

        return f"{day}/{month}/{year}"
