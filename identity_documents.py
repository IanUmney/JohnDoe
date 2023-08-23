import random

from PIL import Image, ImageDraw, ImageFont
import cv2
import random
import datetime


def create_bank_card():
    # Open the base image
    image = Image.open("src/identity documents/Credit_Card_blank.jpg")

    # add and paste the chip image
    chip_image = Image.open("src/identity documents/chip.png")
    chip_position = (110, 225)
    image.paste(chip_image, chip_position)
    # todo image.paste(chip_image, chip_position, chip_image)  # replace above when alpha added to png

    # add and paste the hologram image
    hologram_image = Image.open("src/identity documents/hologram.jpg")
    hologram_position = (700, 250)
    image.paste(hologram_image, hologram_position)

    # add and paste the visa image
    visa_image = Image.open("src/identity documents/visa.jpg")
    visa_position = (700, 50)
    image.paste(visa_image, visa_position)

    # Draw the credit card number
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("src/fonts/CREDC___.ttf", size=55)
    text_position = (100, 400)
    number = "1234 5678 9101 1121"
    draw.text(text_position, number, font=font, fill=(0, 0, 0))

    # Draw the name
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("src/fonts/CREDC___.ttf", size=40)
    name_position = (125, 560)
    name = "IAN UMNEY"
    draw.text(name_position, name, font=font, fill=(0, 0, 0))

    # Draw the expiry
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("src/fonts/Roboto-Light.ttf", size=45)
    text_position = (300, 500)
    expires = "01/27"
    draw.text(text_position, expires, font=font, fill=(0, 0, 0))

    # Save and show the image
    output_image_path = "src/identity documents/cc_image.png"
    image.save(output_image_path)


def create_nino_image(_nino, _name):
    """Loads blank NINO card and draws name and number to it"""

    image = Image.open("src/NINO_Card.png")
    draw = ImageDraw.Draw(image)

    def draw_nino(nino, draw):
        """Draw the NINO to the card"""

        font = ImageFont.truetype("src/fonts/Roboto-Black.ttf", size=75)

        text_position = (200, 515)

        draw.text(text_position, nino, font=font, fill=(0, 0, 0))

    def draw_name(name, draw):
        """Draw the name to the card"""

        font = ImageFont.truetype("src/fonts/Roboto-Light.ttf", size=60)

        text_position = (225, 615)

        draw.text(text_position, name, font=font, fill=(0, 0, 0))

    draw_nino(_nino, draw)
    draw_name(_name, draw)

    output_image_path = "src/output.jpg"

    image.save(output_image_path)


def create_identify_card(forename, surname, gender, date_of_birth, place_of_birth):

    image = Image.open("src/uk-identity-card.jpeg")
    draw = ImageDraw.Draw(image)

    nationality = "British Citizen"

    month_of_issue = str(random.randint(1, 12))
    if int(month_of_issue) <= 9:
        month_of_issue = f"0{month_of_issue}"
    current_year = datetime.datetime.now().year
    year_of_issue = random.randint(current_year - 10, current_year)
    expiry = f"{month_of_issue}/{year_of_issue + 10}"
    issue = f"{month_of_issue}/{year_of_issue}"

    issue_number = str(random.randint(123456, 987654))

    # todo issue date, expiry date, top-right ident no, signature

    font = ImageFont.truetype("src/fonts/Roboto-black.ttf", size=15)
    draw.text((84, 62), surname, font=font, fill=(0, 0, 0))
    draw.text((84, 82), forename, font=font, fill=(0, 0, 0))
    draw.text((177, 150), gender, font=font, fill=(0, 0, 0))
    draw.text((235, 150), nationality, font=font, fill=(0, 0, 0))
    draw.text((187, 185), date_of_birth, font=font, fill=(0, 0, 0))
    draw.text((319, 184), place_of_birth, font=font, fill=(0, 0, 0))
    draw.text((203, 249), expiry, font=font, fill=(0, 0, 0))
    draw.text((203, 216), issue, font=font, fill=(0, 0, 0))
    draw.text((386, 15), issue_number, font=font, fill=(0, 0, 0))

    output_image_path = "src/FAKE_NATIONAL_IDENT.jpg"
    image.save(output_image_path)


def poscal():
    # Function to capture mouse click event
    def mouse_click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button click
            print(f"Mouse clicked at (x, y): ({x}, {y})")

    # Load an image
    image_path = "src/output.jpg"
    image = cv2.imread(image_path)

    # Display the image
    cv2.imshow("Image", image)

    # Set the mouse click callback function
    cv2.setMouseCallback("Image", mouse_click)

    # Wait for a key event
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()

# create_identify_card()
# poscal()
# create_nino_image("JX 81 44 39 D", "Ian Umney")
# create_bank_card()

