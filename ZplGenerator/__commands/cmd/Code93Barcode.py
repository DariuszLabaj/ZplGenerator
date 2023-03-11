from typing import Any, Optional


class Code93Barcode:
	def __init__(self, orientation, height, printInterpretationLine, printInterpretationLineAboveCode, printCheckDigit) -> None:
		"""
		The ^BA command creates a variable length, continuous symbology. The Code 93 bar code is used in many of the same applications as Code 39. It uses the full 128-character ASCII set. ZPL II, however, does not support ASCII control codes or escape sequences. It uses the substitute characters shown below.
		"""
		self.__orientation = orientation
		self.__height = height
		self.__printInterpretationLine = printInterpretationLine
		self.__printInterpretationLineAboveCode = printInterpretationLineAboveCode
		self.__printCheckDigit = printCheckDigit

	def __str__(self) -> str:
		format = f"^BA{self.__orientation},{self.__height},{self.__printInterpretationLine},{self.__printInterpretationLineAboveCode},{self.__printCheckDigit}"
		return format
