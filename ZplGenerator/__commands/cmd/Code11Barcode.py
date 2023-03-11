from typing import Any, Optional


class Code11Barcode:
	def __init__(self, orientation, checkDigit, height, printInterpretationLine, printInterpretationLineAboveCode) -> None:
		"""
		The ^B1 command produces the Code 11 bar code, also known as USD-8 code. In a Code 11 barcode, each character is composed of three bars and two spaces, and the character set includes 10 digits and the hyphen (-)
		"""
		self.__orientation = orientation
		self.__checkDigit = checkDigit
		self.__height = height
		self.__printInterpretationLine = printInterpretationLine
		self.__printInterpretationLineAboveCode = printInterpretationLineAboveCode

	def __str__(self) -> str:
		format = f"^B1{self.__orientation},{self.__checkDigit},{self.__height},{self.__printInterpretationLine},{self.__printInterpretationLineAboveCode}"
		return format
