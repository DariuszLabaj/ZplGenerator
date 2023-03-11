from typing import Any, Optional


class CodaBlockBarcode:
	def __init__(self, orientation, height, securityLevel, noOfCharPerRow, noOfRows, mode) -> None:
		"""
		The ^BB command produces a two-dimensional, multirow, stacked symbology. It is ideally suited for applications that require large amounts of information.
		"""
		self.__orientation = orientation
		self.__height = height
		self.__securityLevel = securityLevel
		self.__noOfCharPerRow = noOfCharPerRow
		self.__noOfRows = noOfRows
		self.__mode = mode

	def __str__(self) -> str:
		format = f"^BB{self.__orientation},{self.__height},{self.__securityLevel},{self.__noOfCharPerRow},{self.__noOfRows},{self.__mode}"
		return format
