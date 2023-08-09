import random
import string
import datetime
# import configparser
# import requests
# import json
# import urllib.request
# import os


class JohnDoe:

    def __init__(self, **kwargs):
        self.gender = kwargs.get("gender", "male")[0].lower()
        self.name = kwargs.get("name", self.name())
        self.age = int(kwargs.get("age", self.age()))
        self.birthday = self.birthday()
        self.mobile_number = self.mobile_number()
        self.address = self.address()
        self.email = self.email()
        self.ip_address = self.ip_address()
        self.nino = self.nino()
        self.bank_card = self.bank_card()
        self.driving_license = self.driving_license()
        # self.image = self.image()

    def _age(self):
        if self.age <= 18:
            exit(f"You cannot generate minors. Odep.")
        else:
            return self.age

    # Private function to check gender is given correctly
    def _gender(self):
        if self.gender == "m":
            return "male"
        elif self.gender == "f":
            return "female"
        else:
            exit("Gender must either be 'male' or 'female'! No 'Apache Attack Helicopters'")

    def create(self):
        """Return all the JohnDoe object information"""
        self_dict = self.__dict__
        for x in self_dict:
            if type(self_dict[x]) == dict:
                print(f"{x}")
                for y in self_dict[x]:
                    print(f"\t{y} : {self_dict[x][y]}")
            else:
                print(f"{x} : {self_dict[x]}")
        return self_dict

    @staticmethod
    def mobile_number():
        """Get a random phone number in UK format using
        genuine prefixes and providers"""

        with open(f"./src/mobile_numbers.txt", "r") as file:
            # Get random line from number file
            random_line = random.choice(file.readlines())

            # Get random number prefix
            number = random_line.split(" ")[0]

            # Add suffix to genuine number prefix
            while len(number) < 11:
                number += str(random.randint(0, 9))

            # Get provider associated with number prefix
            provider = " ".join(random_line.strip().split(" ")[1:])

        return {"number": number, "provider": provider}

    @staticmethod
    def nino():
        """Create a national insurance number with format AB123456C"""

        # random ascii char
        _rac = lambda: random.choice(string.ascii_uppercase)

        return f"{_rac()}{_rac()}{random.randint(111_111, 999_999)}{_rac()}"

    @staticmethod
    def address():
        """Get random UK adrress information.
        Postcode and area are genuine.
        Street names are random choice from top 50"""

        # Get random house number
        house_number = random.randint(1, 500)

        # Get random street name
        with open(f"./src/streets.txt", "r") as street_file:
            line = street_file.readlines()
            random_line = random.choice(line)
            street = random_line.strip()

        # Get random postcode and area
        with open(f"./src/postcodes.txt") as file:
            line = file.readlines()
            random_line = random.choice(line)

            postcode = random_line.strip().split(",")[0]
            area = random_line.strip().split(",")[1]

        return {"house_number": house_number,
                "street": street,
                "area": area,
                "postcode": postcode
                }

    def name(self):
        """Get a random name from the most common forenames
        and surnames in the UK"""

        # Get random forename
        with open(f"./src/{self._gender()}.txt") as forename_file:
            line = forename_file.readlines()
            random_name = random.choice(line).strip()

        # Get random surname
        with open(f"./src/surnames.txt") as surname_file:
            rl = surname_file.readlines()
            random_surname = random.choice(rl).strip()

        return f"{random_name} {random_surname}"

    @staticmethod
    def bank_card():
        """Get genuine UK bank card information provider.
        Generate random 10 numbers to complete card."""

        # Get genuine card number and provider
        with open(f"./src/cards.txt", "r") as file:
            rl = file.readlines()
            for x in rl:
                number = x.split(" ")[0].strip()
                provider = x.split(" ")[1].strip()

        # Concatenate random 10-digit number to complete card
        number = number + str(random.randint(0o000_0000_00, 9999_9999_99))

        # Random expiry date
        expiry_date = str(random.randint(1, 12)) + "/" + str(random.randint(22, 32))

        # Random CVV
        cvv = str(random.randint(123, 987))

        return {"card_number": f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:16]}",
                "provider": provider,
                "expiry_date": expiry_date,
                "cvv": cvv
                }

    @staticmethod
    def age():
        """Random age"""
        return random.randint(18, 65)

    def birthday(self):
        """Random birthday"""

        year = datetime.datetime.now().year - self._age()
        month = random.randint(1, datetime.datetime.now().month)
        day = random.randint(1, 28)

        # Always print double-digit birthdays
        if day < 10:
            day = "0" + str(day)
        if month < 10:
            month = "0" + str(month)

        return f"{day}/{month}/{year}"

    def driving_license(self):
        """Driving license according to UK format, for John Doe's details"""

        # The first five characters of the surname
        # (padded with 9s if less than 5 characters)
        if len(self.name.split(" ")[-1].replace("'", "")) < 5:
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
        if self._gender() == "male":
            c = self.birthday.split("/")[1]
        else:
            c = int(self.birthday.split("/")[1]) + 5

        # The date within the month of birth
        d = self.birthday.split("/")[0]

        # The year digit from the year of birth
        # (e.g. for 1987 it would be 7)
        e = self.birthday.split("/")[2][3]

        # The first two initials of the first names
        # (padded with a 9 if no middle name)
        if len(self.name.split(" ")) >= 3:
            f_a = self.name.split(" ")[0][0]
            f_b = self.name.split(" ")[1][0]
            f = f_a + f_b
        else:
            f = "9"

        # Arbitrary digit – usually 9, but decremented to
        # differentiate drivers with the first 13 characters in common
        g = "9"

        # Two computer check digits
        h = f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}"

        # Appended, two digits representing the licence issue, which increases
        # by 1 for each licence issued
        i = f"{random.randint(1, 9)}0"

        return "{}{}{}{}{}{}{}{} {}".format(a.upper(), b, c, d, e, f, g, h, i)

    def email(self):
        """Random email based on name of John Doe"""

        # Email providers with UK TLD
        providers = ["yahoo.com", "gmail.com", "live.com",
                     "hotmail.com", "icloud.com", "msn.com"
                     ]

        provider = random.choice(providers)

        email = ".".join(self.name.split(" ")) + "@" + provider

        return email

    @staticmethod
    def ip_address():
        """Generate a random IP based on a list 
        of genuine UK IP address blocks."""

        # Get random line from IP csv file
        with open(f"./src/ip_address.csv") as f:
            ip_range = next(f)
            for num, aline in enumerate(f, 2):
                if random.randrange(num):
                    continue
                ip_range = aline.strip("\n")

        # Get start of IP block
        ip_start = ip_range.split(",")[0]
        so1 = int(ip_start.split(".")[0])
        so2 = int(ip_start.split(".")[1])
        so3 = int(ip_start.split(".")[2])
        so4 = int(ip_start.split(".")[3])

        # Get end of IP block
        ip_end = ip_range.split(",")[1]
        eo1 = int(ip_end.split(".")[0])
        eo2 = int(ip_end.split(".")[1])
        eo3 = int(ip_end.split(".")[2])
        eo4 = int(ip_end.split(".")[3])

        # Generate random IP in block
        ip1 = random.randint(so1, eo1)
        ip2 = random.randint(so2, eo2)
        ip3 = random.randint(so3, eo3)
        ip4 = random.randint(so4, eo4)

        return "{}.{}.{}.{}".format(ip1, ip2, ip3, ip4)

    """This function will be worked on for future releases"""
    # def image(self):
    #     """Generate an AI powered image of a person matching
    #     John Doe\'s details"""
    #
    #     # Load config file to get key
    #     full_path = os.path.dirname(os.path.abspath(__file__))
    #     config = configparser.ConfigParser()
    #     config.read(os.path.join(full_path, 'config.ini'))
    #
    #     # Get API key from confif file
    #     api_key = config["GeneratedPhotos"]["API_KEY"]
    #
    #     if api_key != "":
    #         # Set header for request
    #         header = {"Authorization": f"API-key {api_key}"}
    #
    #         # Define reqest age from John Doe's age
    #         if self._age() <= 25:
    #             age = "young-adult"
    #         elif self._age() <= 50:
    #             age = "adult"
    #         else:
    #             age = "elderly"
    #
    #         # Send request to API
    #         url = f"https://api.generated.photos/api/v1/faces?age={age}&order_by=random"
    #         r = requests.get(url, headers=header)
    #         jsonr = json.loads(r.text)
    #
    #         # Look for male result in json response
    #         try:
    #             for x in jsonr["faces"]:
    #                 if self._gender() == "male":
    #                     if x["meta"]["gender"][0] == "male":
    #                         # Get 512x512 image URL
    #                         image_url = x["urls"][-1]["512"]
    #                         break
    #                 elif self._gender() == "female":
    #                     if x["meta"]["gender"][0] == "female":
    #                         # Get 512x512 image URL
    #                         image_url = x["urls"][-1]["512"]
    #                         break
    #
    #         except Exception as e:
    #             print("Cannot get AI image at this time. Try again later", e)
    #         else:
    #             if image_url != "":
    #                 # Save the image into src/ directory
    #                 location = f"{full_path}/src/images/{self.name}_portrait.jpg"
    #                 requests.urlretrieve(image_url, location)
    #                 return location
    #             else:
    #                 print("no image url")


if __name__ == "__main__":
    JohnDoe().create()

