import random
import string
from datetime import datetime
import argparse
import json
from src import nino
from src import national_identity_card as nic
import driving_license
import bank
import re


class JohnDoe:

    def __init__(self, **kwargs):
        """Initialize a JohnDoe object with optional parameters.

        Parameters:
        - gender (str): Gender of the individual ('m' or 'f').
        - name (str): Full name of the individual.
        - dob (str): Date of birth in DD/MM/YYYY format
        - docs (bool): Whether to generate identity documents (default is False).
         """

        self.gender = self.gender(kwargs.get("gender"))  # Must be first as self.name relies on gender (m\f)
        self.name = self.name(kwargs.get("name"))

        if not kwargs.get("dob"):
            self.date_of_birth = self.date_of_birth(None)
        else:
            self.date_of_birth = self.date_of_birth(kwargs.get("dob"))

        self.car = self.car()
        self.nino = self.nino()
        self.email = self.email()
        self.address = self.address()
        self.banking = self.banking_info()
        self.ip_address = self.ip_address()
        self.mobile_number = self.mobile_number()
        self.driving_license = self.driving_license()
        if kwargs.get("docs"):
            self.document()
        if kwargs.get("print"):
            self.print()

    @staticmethod
    def car() -> dict:
        """Generates car information for JD.

        Returns:
            Dictionary: associated information for vehicle.
        """

        def number_plate():
            """Generate random number plate of UK format AB01 23C.

            Returns:
                String: Random letters and numbers.
            """
            letters = string.ascii_letters
            digits = string.digits

            two_letters = random.choices(letters.upper(), k=2)
            two_numbers = random.choices(digits, k=2)
            space = " "
            three_letters = random.choices(letters.upper(), k=3)

            random_string = "".join(two_letters + two_numbers + [space] + three_letters)
            return random_string

        return {"number_plate": number_plate()}

    @staticmethod
    def gender(gender):
        """Assigns JD's gender by either parsing input or randomly generating.

        Parameters:
            gender: Must be either 'male' or 'female', or 'None' to generate random gender.

        Returns:
            String: 0th index of 'male' or 'female'.

        Note:
            gender should be expressly be given when a name has been given otherwise the gender may not match the name.
        """

        if gender is not None and gender[0].lower() in ["m", "f"]:
            return gender[0].lower()

        elif gender is not None:
            exit("Gender must be '[m]ale' or '[f]emale'.")

        else:
            randint = random.randint(1, 999)

            if randint % 2 == 0:
                return "m"
            else:
                return "f"

    def name(self, name) -> str:
        """Assigns JD's name by parsing input or randomly generating one.

        Parameters:
            name: Can be first name only, or first and last name.

        Returns:
            String: First and last name.
        """

        def random_firstname():
            with open(f"./src/names/{self.gender}.txt") as forename_file:
                _line = forename_file.readlines()
                _random_firstname = random.choice(_line).strip()
                return _random_firstname

        def random_surname():
            with open(f"./src/names/surnames.txt") as surname_file:
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
    def date_of_birth(dob) -> str:
        """Assigns JD's date of birth by parsing input or randomly generating.

        Parameters:
            dob: Date of birth in the format DD/MM/YYYY.

        Returns:
            String: Date of birth in the format DD/MM/YYYY.
        """

        def valid_dob(input_dob):
            """Checks id the input dob is in the valid format"""

            pattern = re.compile(r'^\d{2}/\d{2}/\d{4}$')

            if pattern.match(input_dob):
                day, month, year = map(int, input_dob.split('/'))
                if 1 <= day <= 31 and 1 <= month <= 12:
                    return True
            return False

        def calculate_age(birthdate):
            """Calculates age from birthdate to determine under-age generation"""

            today = datetime.today()
            birthdate = datetime.strptime(birthdate, '%d/%m/%Y')
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            return age

        def generate_dob():
            """Generate a random date of birth"""

            random_day = random.randint(1, 27)
            random_month = random.randint(1, 11)
            random_year = random.randint(datetime.now().year - 88, datetime.now().year - 18)
            date_of_birth = f"{random_month}/{random_day}/{random_year}"
            return date_of_birth

        if dob is None:
            return generate_dob()

        elif valid_dob(dob):
            if calculate_age(dob) <= 18:
                raise ValueError(f"You cannot generate minors! Odep.")
            else:
                return dob
        else:
            exit("The date of birth should be in the format of 'DD/MM/YYY'")

    def json(self) -> json:
        """Print the JohnDoe object information"""

        return json.dumps(self.__dict__, indent=4)

    @staticmethod
    def mobile_number() -> dict:
        """Assigns JD's mobile phone information based on accurate data.

        Returns:
            Dictionary: Randomly generated phone number and random provider from list.
        """

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
    def nino() -> str:
        # todo Add temp prefixes from https://www.gov.uk/hmrc-internal-manuals/national-insurance-manual/nim39110
        """Assign JD's national insurance number with format QQ 12 34 56 C.

        Returns:
            String: Randomly generated letters and numbers in correct format.
        """

        # random ascii char
        _rac = lambda: random.choice(string.ascii_uppercase)
        _random_int = lambda: random.randint(10, 99)

        return f"{_rac()}{_rac()} {_random_int()} {_random_int()} {_random_int()} {_rac()}"

    @staticmethod
    def address() -> dict:
        """Assign JD's address.

        Returns:
            Dictionary:
                House number:   Random integer 1 - 500.
                Street:         Random choice of popular UK street names.
                Area:           Random choice of any UK area.
                Postcode:       Based on area.

        """

        # Get random house number
        house_number = random.randint(1, 500)

        # Get random street name
        with open(f"./src/addresses/streets.txt", "r") as street_file:
            line = street_file.readlines()
            random_line = random.choice(line)
            street = random_line.strip()

        # Get random postcode and area
        with open(f"./src/addresses/postcodes.txt") as file:
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
    def banking_info() -> dict:
        """Generate JD's banking information.

        Returns:
            Dictionary:
                Bank:           Based on sortcode
                Sortcode:       Random from list of UK banks
                Account Number: Randomly generated
                Card number:    Randomly generated
                Provider:       Based on card number
                Expiry date:    Randomly generated
                CVV:            Randomly Generated
        """

        def account_details() -> dict:
            """Gets the accurate information from file"""

            with open("src/bank/sortcodes.txt", "r") as f:
                lines = f.readlines()
                l = random.choice(lines)

                sort = l.split("\t")[0]
                _sort_code = f"{sort[0:2]}-{sort[2:4]}-{sort[4:6]}"

                _bank = l.split("\t")[1].strip("\n")

                _account_number = random.randint(12345678, 87654321)

                return {"sort_code": _sort_code,
                        "account_number": _account_number,
                        "bank": _bank}

        # Get genuine card number and provider
        with open(f"./src/bank/cards.txt", "r") as file:
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

        account_number = account_details()["account_number"]
        sort_code = account_details()["sort_code"]
        bank = account_details()["bank"]

        return {"bank": bank,
                "sort_code": sort_code,
                "account_number": account_number,
                "card_number": f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:16]}",
                "provider": provider,
                "expiry_date": expiry_date,
                "cvv": cvv
                }

    def driving_license(self) -> str:
        """Generates JD's driving license number in accurate format.

        Returns:
            String: Uses JD's gender, name, date of birth, and randomly generated characters.
        """

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
        b = str(self.date_of_birth).split("/")[2][2]

        # The month of birth (7th character incremented
        # by 5 if driver is female i.e. 51–62 instead of 01–12)
        if self.gender == "m":
            c = str(self.date_of_birth).split("/")[1]
        else:
            c = int(str(self.date_of_birth).split("/")[1]) + 5

        # The date within the month of birth
        d = str(self.date_of_birth).split("/")[0]

        # The year digit from the year of birth
        # (e.g. for 1987 it would be 7)
        e = str(self.date_of_birth).split("/")[2][3]

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
        g = "9"  # todo make this dynamic (as above with db)

        # Two computer check digits
        h = f"{random.choice(string.ascii_uppercase)}" \
            f"{random.choice(string.ascii_uppercase)}"

        # Appended, two digits representing the licence issue, which increases
        # by 1 for each licence issued
        i = f"{random.randint(1, 9)}"

        return "{}{}{}{}{}{}{}{} {}".format(a.upper(), b, c, d, e, f, g, h, i)

    def email(self) -> str:
        """Generates JD's email address.

        Returns:
            String: Uses JD's first and last name with a random email provider
        """

        # Email providers with UK TLD
        providers = ["yahoo.co.uk", "gmail.co.uk", "live.co.uk",
                     "hotmail.co.uk", "icloud.co.uk", "msn.co.uk"
                     ]

        provider = random.choice(providers)

        email = ".".join(self.name.split(" ")) + "@" + provider

        return email

    @staticmethod
    def ip_address() -> str:
        """Generate JD's IP address from UK IP blocks.

        A random line is chosen and the minimum and maximum IP address block is used to generate the IP.

        Returns:
            String: Randomly generated IP based on provider IP block.
        """

        # Get random line from IP csv file
        with open(f"src/addresses/ip_address.csv") as f:
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

    def document(self) -> None:
        """Generate and show Jd's identity documents by calling the generate() function of the respective classes.

        Returns:
            None: Upon success the generated cards will automatically open.
        """
        ident_card = nic.NationalIdentityCard(forename=self.name.split(" ")[0],
                                              surname=self.name.split(" ")[1],
                                              date_of_birth=self.date_of_birth,
                                              gender=self.gender,
                                              place_of_birth=self.address["area"])

        dl = driving_license.DrivingLicense(forename=self.name.split(" ")[0],
                                            surname=self.name.split(" ")[1],
                                            date_of_birth=self.date_of_birth,
                                            place_of_birth=self.address["area"],
                                            gender=self.gender,
                                            dvla_number=self.driving_license,
                                            address=f"{self.address['house_number']} {self.address['street']}\n"
                                                    f"{self.address['area']} {self.address['postcode']}")

        bank_card = bank.Bank(name=self.name, cc_number=self.banking["card_number"], expiry=self.banking["expiry_date"])

        nin = nino.Nino(self.name, self.nino)

        nin.generate_card()  # Generate national insurance card
        dl.generate_card()  # Generate driving license
        ident_card.generate_card()  # generate national identity card
        bank_card.generate()

    def print(self) -> None:
        """Prints JD's information to the console

        Returns:
            None: Prints self.__dict__ as json via self.json()
        """
        print(self.json())


def main():
    parser = argparse.ArgumentParser(description="Generate PII for testing environments")
    parser.add_argument("--name", type=str, help="Name (first last)")
    parser.add_argument("--dob", type=str, help="Date of birth (DD/MM/YY)")
    parser.add_argument("--gender", help="Gender (m/f)")
    parser.add_argument("--docs", action="store_true", help="Generate identity documents")
    parser.add_argument("--print", action="store_true", help="Print output to console")

    arguments = parser.parse_args()
    args_dict = vars(arguments)

    JohnDoe(**args_dict)


if __name__ == "__main__":
    main()
