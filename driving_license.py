import random
import datetime
from PIL import Image, ImageDraw, ImageFont


class DrivingLicense:

    def __init__(self, forename, surname, gender, date_of_birth, place_of_birth, dvla_number, address):
        self.forename = forename
        self.surname = surname
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth
        self.month_of_issue = str(random.randint(1, 12))
        if int(self.month_of_issue) <= 9:
            self.month_of_issue = f"0{self.month_of_issue}"
        self.nationality = "British Citizen"
        self.dvla_number = dvla_number

        current_year = datetime.datetime.now().year
        self.year_of_issue = random.randint(current_year - 10, current_year)
        self.expiry = f"{self.month_of_issue}/{self.year_of_issue + 10}"
        self.issue = f"{self.month_of_issue}/{self.year_of_issue}"
        self.issue_number = str(random.randint(123456, 987654))
        self.address = address

    def generate_card(self):

        image = Image.open("src/driving license/blank_driving_license.png")
        draw = ImageDraw.Draw(image)

        # todo signature

        font = ImageFont.truetype("src/fonts/Roboto-black.ttf", size=8)
        font2 = ImageFont.truetype("src/fonts/Roboto-black.ttf", size=13)

        draw.text((105, 27), self.surname, font=font, fill=(0, 0, 0))
        draw.text((105, 37), self.forename, font=font, fill=(0, 0, 0))
        # draw.text((177, 150), self.gender, font=font, fill=(0, 0, 0))
        # draw.text((235, 150), self.nationality, font=font, fill=(0, 0, 0))
        draw.text((105, 58), self.date_of_birth, font=font, fill=(0, 0, 0))
        # draw.text((319, 184), self.place_of_birth, font=font2, fill=(0, 0, 0))
        draw.text((105, 78), self.expiry, font=font, fill=(0, 0, 0))
        draw.text((105, 68), self.issue, font=font, fill=(0, 0, 0))
        draw.text((130, 88), self.dvla_number, font=font, fill=(0, 0, 0))
        draw.text((103, 126), self.address, font=font, fill=(0, 0, 0))
        # draw.rectangle([x1, y1, x2, y2], fill="white")


        output_image_path = "src/national_identity_card/generated_national_identity_card.jpg"
        image.save(output_image_path)
        image.show(f"{self.surname}, {self.forename}")

