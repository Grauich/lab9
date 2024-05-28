from PIL import Image, ImageFilter
import os
from pathlib import Path


def filter_image(picture):
    img = Image.open(picture)
    filt_img = img.filter(ImageFilter.EMBOSS)
    return filt_img


def process_images(papka, papkanew):
    os.makedirs(papkanew, exist_ok=True)

    for filename in os.listdir(papka):
        if filename.lower().endswith((".jpg", ".png")):
            inputimg = os.path.join(papka, filename)
            extension = Path(filename).suffix
            outputimg = os.path.join(
                papkanew, f"{Path(filename).stem}_new{extension}"
            )
            filt_img = filter_image(inputimg)
            filt_img.save(outputimg)


def main():
    papka = "9lab1picture"
    papkanew = "9lab1pictureNEW"
    process_images(papka, papkanew)


main()
