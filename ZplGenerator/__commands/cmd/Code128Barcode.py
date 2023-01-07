from typing import Any, Optional


class Code128Barcode:
	def __init__(self, orientation, height, printInterpretationLine, printInterpretationLineAboveCode, checkDigit, mode) -> None:
		"""
		The ^BC command creates the Code 128 barcode, a high-density, variable length, continuous, alphanumeric symbology. It was designed for complexly encoded product identification.
		"""
		self.__orientation = orientation
		self.__height = height
		self.__printInterpretationLine = printInterpretationLine
		self.__printInterpretationLineAboveCode = printInterpretationLineAboveCode
		self.__checkDigit = checkDigit
		self.__mode = mode

	def __str__(self) -> str:
		format = f"^BC{self.__orientation},{self.__height},{self.__printInterpretationLine},{self.__printInterpretationLineAboveCode},{self.__checkDigit},{self.__mode}"
		return format
