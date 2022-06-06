"""
Program Name: JohnDoe
Version: 2.0
Author: Ian Umney
License: MIT

This application was written with the aim of being used
in testing environments which require sensitive personally
identifiable information (PII) of a UK British subject.

Release version 2.0 contains the following updates:
    + todo Refactor package name to "JohnDoePII"
    + todo GUI for better UX
    + todo Dynamically change JohnDoe's information

=======================================
("Planned updates for future releases")
Release version 2.1:
    + Webapp
    + API access (token)
Release version 2.2:
    + AI/ML integration for deeper UX

"""
##################
# !/usr/bin/python3
import random
import string
import datetime
import configparser
import requests
import json
import urllib.request
import os
import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="Name to use", type=str)
parser.add_argument("--age", help="Age to use", type=int, metavar="{18..99}")
parser.add_argument("--gender", help="Gender to use", type=str, choices=["male", "female"])
parser.add_argument("-p", "--pdf", help="Print results to PDF page", action="store_true")
parser.add_argument("-v", "--verbose", help="Print results to command line", action="store_true")
args = parser.parse_args()

class JohnDoe:
    """Main object of any generated character."""
    def __init__(self, **kwargs):
        self.gender = self.gender(kwargs)
        self.name = self.name(kwargs)
        self.age = self.age(kwargs)
        self.mobile_number = self.mobile_number()
        self.social_security = self.social_security()
        self.address = self.address()
        self.bank_card = self.bank_card()
        self.birthday = self.birthday()
        self.driving_license = self.driving_license()
        self.ip_address = self.ip_address()

    def gender(self, kwargs):
        """Either accept input gender or randomly assign one"""
        if kwargs.get("gender"):
            self.gender = kwargs.get("gender")
        elif args.gender:
            self.gender = args.gender
        else:
            random_int = random.randint(1, 99)  # Get random number 1..99
            if random_int % 2 == 0:  # If number/2 is equal
                random_gender = "female"
            else:
                random_gender = "male"
            self.gender = random_gender
        return self.gender

    def name(self, kwargs):
        if kwargs.get("name"):
            self.name = kwargs.get("name")
        elif args.name:
            self.name = args.name
        else:
            """Get a random name from the most common forenames
            and surnames in the UK"""
            with open(f"./src/gb/{self.gender}.txt") as forename_file:  # Get random forename
                line = forename_file.readlines()
                random_name = random.choice(line).strip()
            with open(f"./src/gb/surnames.txt") as surname_file:  # Get random surname
                rl = surname_file.readlines()
                random_surname = random.choice(rl).strip()
            self.name = f"{random_name} {random_surname}"
        return self.name

    def age(self, kwargs):
        """Either get the ages from args or kwargs, or generate random age"""
        if kwargs.get("age"):  # If age in kwargs
            if kwargs.get("age") < 18:
                exit("You cannot generate minors. Weirdo")
            else:
                self.age = kwargs.get("age")  # Set age to kwargs
        elif args.age:  # If age in kwargs
            if args.age < 18:
                exit("You cannot generate minors. Weirdo")
            else:
                self.age = args.age   # Set age to args.age
        else:
            self.age = random.randint(18, 99)  # Set age to random number
        return self.age

    def mobile_number(self):
        """Get a random phone number in UK format using
        genuine prefixes and providers"""
        number = None
        provider = None
        with open(f"./src/gb/mobile_numbers.txt", "r") as file:
            random_line = random.choice(file.readlines()) # Get random line from number file
            provider = " ".join(random_line.strip().split(" ")[1:])  # Get provider associated with number prefix
            number = random_line.split(" ")[0] # Get random number prefix
            while len(number) < 11: # While phone number length is less than 11
                number += str(random.randint(0, 9)) # Keep appending random numbers

        # def number():
        #     return self.mobile_number["number"]
        #
        # def provider():
        #     return self.mobile_number["provider"]

        return f"{number}, {provider}"

    def social_security(self):
        """Gets string with the format of a national insurance
        number: AB123456C"""
        rac: () = lambda: random.choice(string.ascii_uppercase)  # random ascii char
        return f"{rac()}{rac()}{random.randint(111_111, 999_999)}{rac()}"

    def address(self):
        """Get random UK address information.
        Postcode and area are genuine.
        Street names are random choice from top 50"""

        # Get random house number
        house_number = random.randint(1, 500)

        # Get random street name
        with open(f"./src/gb/streets.txt", "r") as street_file:
            line = street_file.readlines()
            random_line = random.choice(line)
            street = random_line.strip()

        # Get random postcode and area
        with open(f"./src/gb/postcodes.txt") as file:
            line = file.readlines()
            random_line = random.choice(line)

            postcode = random_line.strip().split(",")[0]
            area = random_line.strip().split(",")[1]

        address = f"{house_number} {street}, {area}, {postcode}"
        return address

    def bank_card(self):
        """Get genuine UK bank card information provider.
        Generate random 10 numbers to complete card."""

        # Get genuine card number and provider
        with open(f"./src/gb/cards.txt", "r") as file:
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

        bank_card = f"{number}, {cvv}, {expiry_date}, {provider}"
        return bank_card # todo make bank card object

    def birthday(self):
        """Random birthday"""
        # ensures that age is calculated from previous date
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
        """Driving license according to UK format, for John Doe\'s details"""

        # The first five characters of the surname (padded with 9s if less than 5 characters)
        # surname_length = len(self.name["secondname"])
        # A = self.name["secondname"][:surname_length]
        A = self.name.split(" ")[1][:5]
        if len(A) < 5:  # If surname is shorter than 5 letters
            while len(A) < 5:  # While A is shorter than five letters
                A = A + "9"  # Pad surname with 9's

        B = self.birthday.split("/")[2][2] # The decade digit from the year of birth

        # The month of birth (7th character incremented by 5 if driver is female i.e. 51–62 instead of 01–12)
        if self.gender == "male":
            C = self.birthday.split("/")[1]
        else:
            C = int(self.birthday.split("/")[1])+5

        # The date within the month of birth
        D = self.birthday.split("/")[0]

        # The year digit from the year of birth
        # (e.g. for 1987 it would be 7)
        E = self.birthday.split("/")[2][3]

        # The first two initials of the first names
        # (padded with a 9 if no middle name)
        # if len(self.name) >= 3:
        #     f_a = self.name.split(" ")[0][0]
        #     f_b = self.name.split(" ")[1][0]
        #     F = f_a + f_b
        # else:
        F = "9"

        # Arbitrary digit – usually 9, but decremented to
        # differentiate drivers with the first 13 characters in common
        G = random.randint(1, 9)

        # Two random computer check digits
        H = f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}"

        # Appended, two digits representing the licence issue, which increases
        # by 1 for each licence issued
        I = f"{random.randint(1,9)}0"

        return "{}{}{}{}{}{}{}{}{}".format(A.upper(), B, C, D, E, F, G, H, I)

    def email(self):
        """Random email based on name of John Doe"""

        # Email providers with
        providers = ["yahoo.co.uk", "gmail.co.uk", "live.co.uk", "hotmail.co.uk", "icloud.co.uk", "msn.co.uk"]

        provider = random.choice(providers)

        email = ".".join(self.name.split(" ")) + "@" + provider

        return email

    def ip_address(self):
        """Generate a random IP based on a list
        of genuine UK IP address blocks."""

        # Get random line from IP csv file
        with open(f"./src/gb/ip_address.csv") as f:
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

    def image(self):
        """Generate an AI powered image of a person matching
        John Doe\'s details"""

        # Load config file to get key
        full_path = os.path.dirname(os.path.abspath(__file__))
        config = configparser.ConfigParser()
        config.read(os.path.join(full_path, 'config.ini'))

        # Get API key from config file
        api_key = config["GeneratedPhotos"]["API_KEY"]

        if api_key != "":
            # Set header for request
            HEADER = {"Authorization": f"API-key {api_key}"}

            # Define request age from John Doe's age
            if self.age() <= 25:
                age = "young-adult"
            elif self.age() <= 50:
                age = "adult"
            else:
                age = "elderly"

            # Send request to API 
            url = f"https://api.generated.photos/api/v1/faces?age={age}&order_by=random"
            r = requests.get(url, headers=HEADER)
            jsonr = json.loads(r.text)

            # Look for male result in json response
            try:
                for x in jsonr["faces"]:
                    if self.gender() == "male":
                        if x["meta"]["gender"][0] == "male":
                            # Get 512x512 image URL
                            image_url = x["urls"][-1]["512"]
                            break
                    elif self.gender() == "female":
                        if x["meta"]["gender"][0] == "female":
                            # Get 512x512 image URL
                            image_url = x["urls"][-1]["512"]
                            break

            except Exception as e:
                logging.error("Cannot connect to AI image server at this time.")
                print("Cannot get AI image at this time. Try again later", e)
            else:
                if image_url != "":
                    # Save the image into src/ directory
                    location = f"{full_path}/src/images/{self.name}_portrait.jpg"
                    urllib.request.urlretrieve(image_url, location)
                    return location
                else:
                    print("no image url")
        else:
            logging.info("No AI image API was supplied - Skipping face generation")

    def list(self):
        for x in self.__dict__:
            print(f"{x}: {self.__dict__[x]}")

    def create(self):
        name = kwargs.get("name")


def main():
    logging.basicConfig(filename="event.log", format="%(asctime)s %(levelname)s : %(message)s", level=logging.INFO)


    jd = JohnDoe()

    if args.verbose:  # If user wants verbose output
        print(jd.list())
    if args.pdf:  # If user wants PDF output
        print("===TODO PDF OUTPUT")


if __name__ == "__main__":
    main()
