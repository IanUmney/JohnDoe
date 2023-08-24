import random

from PIL import Image, ImageDraw, ImageFont
import cv2
import random
import datetime


def create_nino_image(_nino, _name):
    """Loads blank NINO card and draws name and number to it"""

    image = Image.open("src/national_insurance/NINO_Card.png")
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

    output_image_path = "src/national_identity_card/generated_national_identity_card.jpg"

    image.save(output_image_path)





def poscal():
    # Function to capture mouse click event
    def mouse_click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button click
            print(f"Mouse clicked at (x, y): ({x}, {y})")

    # Load an image
    image_path = "src/national_identity_card/generated_national_identity_card.jpg"
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

