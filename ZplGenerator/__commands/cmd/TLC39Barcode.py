from typing import Any, Optional


class TLC39Barcode:
	def __init__(self, orientation, widthOf39Barcode, aspectRatioOf39Barcode, heightOf39Barcode, heightOfMicroPDF417, widthOfMicroPDF417) -> None:
		"""
		The ^BT bar code is the standard for the TCIF can tag telecommunications equipment.
		"""
		self.__orientation = orientation
		self.__widthOf39Barcode = widthOf39Barcode
		self.__aspectRatioOf39Barcode = aspectRatioOf39Barcode
		self.__heightOf39Barcode = heightOf39Barcode
		self.__heightOfMicroPDF417 = heightOfMicroPDF417
		self.__widthOfMicroPDF417 = widthOfMicroPDF417

	def __str__(self) -> str:
		format = f"^BT{self.__orientation},{self.__widthOf39Barcode},{self.__aspectRatioOf39Barcode},{self.__heightOf39Barcode},{self.__heightOfMicroPDF417},{self.__widthOfMicroPDF417}"
		return format
