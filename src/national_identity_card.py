from PIL import Image, ImageDraw, ImageFont
import random
import datetime


class NationalIdentityCard:

    def __init__(self, forename, surname, gender, date_of_birth, place_of_birth):
        self.forename = forename
        self.surname = surname
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth
        self.month_of_issue = str(random.randint(1, 12))
        if int(self.month_of_issue) <= 9:
            self.month_of_issue = f"0{self.month_of_issue}"
        self.nationality = "British Citizen"

        current_year = datetime.datetime.now().year
        self.year_of_issue = random.randint(current_year - 10, current_year)
        self.expiry = f"{self.month_of_issue}/{self.year_of_issue + 10}"
        self.issue = f"{self.month_of_issue}/{self.year_of_issue}"
        self.issue_number = str(random.randint(123456, 987654))

    def generate_card(self):
        image = Image.open("src/national_identity_card/national_identity_card.jpeg")
        draw = ImageDraw.Draw(image)

        # todo signature

        font = ImageFont.truetype("src/fonts/Roboto-black.ttf", size=15)
        font2 = ImageFont.truetype("src/fonts/Roboto-black.ttf", size=13)
        signature = ImageFont.truetype("src/fonts/Daniels Signature DEMO.ttf", size=18)

        draw.text((84, 62), self.surname, font=font, fill=(0, 0, 0))
        draw.text((84, 82), self.forename, font=font, fill=(0, 0, 0))
        draw.text((177, 150), self.gender, font=font, fill=(0, 0, 0))
        draw.text((235, 150), self.nationality, font=font, fill=(0, 0, 0))
        draw.text((187, 185), self.date_of_birth, font=font, fill=(0, 0, 0))
        draw.text((319, 184), self.place_of_birth, font=font2, fill=(0, 0, 0))
        draw.text((203, 249), self.expiry, font=font, fill=(0, 0, 0))
        draw.text((203, 216), self.issue, font=font, fill=(0, 0, 0))
        draw.text((386, 15), self.issue_number, font=font, fill=(0, 0, 0))
        draw.text((310, 230), f"{self.forename[0]} {self.surname}", font=signature, fill=(0, 0, 0))
        # draw.rectangle([x1, y1, x2, y2], fill="white")

        output_image_path = "src/national_identity_card/generated_national_identity_card.jpg"
        image.save(output_image_path)
        image.show(f"{self.surname}, {self.forename}")
