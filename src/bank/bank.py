from PIL import Image, ImageDraw, ImageFont


class Bank:
    # Open the base image
    image = Image.open("src/bank/Credit_Card_blank.jpg")

    # add and paste the chip image
    chip_image = Image.open("src/bank/chip.png")
    chip_position = (110, 225)
    image.paste(chip_image, chip_position)
    # todo image.paste(chip_image, chip_position, chip_image)  # replace above when alpha added to png

    # add and paste the hologram image
    hologram_image = Image.open("src/bank/hologram.jpg")
    hologram_position = (700, 250)
    image.paste(hologram_image, hologram_position)

    # add and paste the visa image
    visa_image = Image.open("src/bank/visa.jpg")
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
    output_image_path = "src/bank/cc_image.png"
    image.save(output_image_path)


Bank()
