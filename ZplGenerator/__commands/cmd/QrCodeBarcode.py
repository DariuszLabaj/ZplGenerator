from typing import Any, Optional


class QrCodeBarcode:
	def __init__(self, orientation, model, magnificationFactor, errorCorrection, maskValue) -> None:
		"""
		The ^BQ command produces a matrix symbology consisting of an array of nominally square modules arranged in an overall square pattern. A unique pattern at three of the symbol’s four corners assists in determining bar code size, position, and inclination.
		"""
		self.__orientation = orientation
		self.__model = model
		self.__magnificationFactor = magnificationFactor
		self.__errorCorrection = errorCorrection
		self.__maskValue = maskValue

	def __str__(self) -> str:
		format = f"^BQ{self.__orientation},{self.__model},{self.__magnificationFactor},{self.__errorCorrection},{self.__maskValue}"
		return format
