#!/usr/bin/env python

from PIL import Image
from pytesser import *
 
class Image2Text():

	def __init__(self,image_file):

		self.image_file = image_file

	def getText(self):

		image = Image.open(self.image_file)

		## Converting to tip format

		text = image_to_string(image)
		#text = image_file_to_string(image_file)
		return text


def main():

	image_file = "fonts_test.png"

	image2text = Image2Text(image_file)

	output_text = image2text.getText()

	print "*********Output text*********"
	print output_text


if __name__ == "__main__":
	main()