from PIL import Image, ImageDraw, ImageFont


class Bank:

    def __init__(self, name, cc_number, expiry):
        (self.visa_image, self.visa_position) = (Image.open("src/bank/visa.jpg"), (700, 50))
        (self.hologram_image, self.hologram_position) = (Image.open("src/bank/hologram.jpg"), (700, 250))
        (self.chip_image, self.chip_position) = (Image.open("src/bank/chip.png"), (110, 225))

        self.name = name.upper()
        self.cc_number = cc_number
        self.expiry = expiry

    def generate(self):

        image = Image.open("src/bank/Credit_Card_blank.jpg")

        image.paste(self.hologram_image, self.hologram_position)

        image.paste(self.chip_image, self.chip_position)

        # add and paste the visa image
        image.paste(self.visa_image, self.visa_position)

        # Draw the credit card number
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("src/fonts/CREDC___.ttf", size=55)
        text_position = (100, 400)
        draw.text(text_position, self.cc_number, font=font, fill=(0, 0, 0))

        # Draw the name
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("src/fonts/CREDC___.ttf", size=40)
        name_position = (125, 560)
        draw.text(name_position, self.name, font=font, fill=(0, 0, 0))

        # Draw the expiry
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("src/fonts/Roboto-Light.ttf", size=45)
        text_position = (300, 500)
        draw.text(text_position, self.expiry, font=font, fill=(0, 0, 0))

        # Save and show the image
        output_image_path = "src/bank/cc_image.png"
        image.save(output_image_path)
        image.show()

