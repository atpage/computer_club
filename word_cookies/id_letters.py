#!/usr/bin/env python

"""Convert a screenshot of a Word Cookies puzzle into the letters."""

################################### Imports: ###################################

import argparse
from PIL import Image
import pytesseract

################################## Functions: ##################################

def load_image(filename):
    return Image.open(filename)

def crop_to_bottom_half(image):
    """Return only the bottom half of image."""
    image = image.crop((0, image.size[1] / 2, image.size[0], image.size[1]))
    return image

################################### main(): ####################################

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Identify the letters at the bottom of a Word Cookies screenshot.')
    parser.add_argument('filename',
                        help='filename of screenshot')
    args = parser.parse_args()

    # WIP:
    image = load_image(args.filename)
    image = crop_to_bottom_half(image)
    image.save('cropped_by_python.png')

    # print(
    #     pytesseract.image_to_string(
    #         Image.open('screenshots/cropped_example.png'),
    #         # config='-psm 9'
    #     )
    # )

#################################### TODO: #####################################

# - subtract background from cropped image
# - prep remaining part (the letters) for OCR

################################################################################
