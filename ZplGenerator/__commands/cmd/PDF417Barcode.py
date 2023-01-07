from typing import Any, Optional


class PDF417Barcode:
	def __init__(self, orientation, height, securityLevel, noOfColumns, noOfRows, truncateRightRowIndicators) -> None:
		"""
		The ^B7 command produces the PDF417 bar code, a two-dimensional, multirow, continuous, stacked symbology. PDF417 is capable of encoding over 1,000 characters per bar code. It is ideally suited for applications requiring large amounts of information at the time the bar code is read.
		"""
		self.__orientation = orientation
		self.__height = height
		self.__securityLevel = securityLevel
		self.__noOfColumns = noOfColumns
		self.__noOfRows = noOfRows
		self.__truncateRightRowIndicators = truncateRightRowIndicators

	def __str__(self) -> str:
		format = f"^B7{self.__orientation},{self.__height},{self.__securityLevel},{self.__noOfColumns},{self.__noOfRows},{self.__truncateRightRowIndicators}"
		return format
