import random
import string
import datetime
import images
import argparse
import json


class JohnDoe:

    def __init__(self, **kwargs):
        """Initialize a JohnDoe object with optional parameters.

        Parameters:
        - gender (str): Gender of the individual ('m' or 'f').
        - name (str): Full name of the individual.
        - age (str): Age of the individual (default is random between 18 and 65).
        - documents (bool): Whether to generate identity documents (default is False).
         """

        self.gender = self.gender(kwargs.get("gender"))  # Must be first as self.name relies on gender
        self.name = self.name(kwargs.get("name"))
        self.age = self.age(kwargs.get("age"))

        if kwargs.get("documents"):
            self.documents = True
        else:
            self.documents = False

        self.nino = self.nino()
        self.email = self.email()
        # self.image = self.image()
        self.address = self.address()
        self.birthday = self.birthday()
        self.bank_card = self.bank_card()
        self.ip_address = self.ip_address()
        self.mobile_number = self.mobile_number()
        self.driving_license = self.driving_license()

    @staticmethod
    def gender(gender):
        """Check is the gender has been given, is correct, or assign a random gender."""

        if gender is not None and gender[0].lower() in ["m", "f"]:
            return gender[0].lower()

        elif gender is not None:
            exit("Gender must be 'male' or 'female'. No 'Apache attack helicopters'")

        else:
            randint = random.randint(1, 999)

            if randint % 2 == 0:
                return "m"
            else:
                return "f"

    def name(self, name):
        """Handle naming the person from input or generation"""

        def random_firstname():
            with open(f"./src/{self.gender}.txt") as forename_file:
                _line = forename_file.readlines()
                _random_firstname = random.choice(_line).strip()
                return _random_firstname

        def random_surname():
            with open(f"./src/surnames.txt") as surname_file:
                _line = surname_file.readlines()
                _random_surname = random.choice(_line).strip()
                return _random_surname

        if name is not None:

            if len(name.split()) == 1:
                generated_surname = random_surname()
                return f"{name.capitalize()} {generated_surname}"

            elif len(name.split()) == 2:
                first = name.split()[0].capitalize()
                second = name.split()[1].capitalize()
                name = f"{first} {second}"
                return name

            elif len(name.split()) >= 3:
                exit("The name can only contain first and last name.")

        else:
            generated_name = f"{random_firstname()} {random_surname()}"
            return generated_name

    @staticmethod
    def age(age) -> int:

        if age is not None and age < 18:
            raise ValueError(f"You cannot generate minors! Nonce.")

        elif age is not None and age >= 18:
            return age

        else:
            return random.randint(18, 80)

    def create(self):
        """Print the JohnDoe object information"""

        # Create identity documents bool
        if self.documents:
            images.create_nino_image(self.nino, self.name)

        print(json.dumps(self.__dict__, indent=4))

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
        # todo Add temp prefixes from https://www.gov.uk/hmrc-internal-manuals/national-insurance-manual/nim39110
        """Create a national insurance number with format QQ 12 34 56 C"""

        # random ascii char
        _rac = lambda: random.choice(string.ascii_uppercase)
        _random_int = lambda: random.randint(10, 99)

        return f"{_rac()}{_rac()} {_random_int()} {_random_int()} {_random_int()} {_rac()}"

    @staticmethod
    def address():
        """Get random UK address information.
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

    def birthday(self):
        """Random birthday"""

        year = datetime.datetime.now().year - self.age
        month = random.randint(1, datetime.datetime.now().month)
        day = random.randint(1, 28)

        # Always print double-digit birthdays
        if day < 10:
            day = "0" + str(day)
        if month < 10:
            month = "0" + str(month)

        return f"{day}/{month}/{year}"

    def driving_license(self):
        """Driving license according to UK format"""

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
        if self.gender == "male":
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
        """Generate a random IP based on a list of genuine UK IP address blocks."""

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


def main():
    parser = argparse.ArgumentParser(description="Generate PII for testing environments")
    parser.add_argument("--name", type=str, help="Name (first last)")
    parser.add_argument("--age", type=int, help="Age (>18)")
    parser.add_argument("--gender", help="Gender (m/f)")
    parser.add_argument("-D", "-d", action="store_true", help="Generate identity documents")
    arguments = parser.parse_args()
    args_dict = vars(arguments)

    jd = JohnDoe(**args_dict)

    jd.create()


if __name__ == "__main__":
    main()
