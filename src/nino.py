from PIL import Image, ImageDraw, ImageFont


class Nino:

    def __init__(self, name, nino):

        self.generate_nino_card(name, nino)

    @staticmethod
    def generate_nino_card(_name, _nino):
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

        output_image_path = "src/national_insurance/nino_card.jpg"

        image.save(output_image_path)
        image.show(f"{_name}, {_nino}")
