from typing import Any, Optional


class MsiBarcode:
	def __init__(self, orientation, checkDigit, height, printInterpretationLine, printInterpretationLineAboveCode, insertCheckDigitIntoInterpretationLine) -> None:
		"""
		The ^BM command is a pulse-width modulated, continuous, non-self- checking symbology. It is a variant of the Plessey bar code (^BP).
		"""
		self.__orientation = orientation
		self.__checkDigit = checkDigit
		self.__height = height
		self.__printInterpretationLine = printInterpretationLine
		self.__printInterpretationLineAboveCode = printInterpretationLineAboveCode
		self.__insertCheckDigitIntoInterpretationLine = insertCheckDigitIntoInterpretationLine

	def __str__(self) -> str:
		format = f"^BM{self.__orientation},{self.__checkDigit},{self.__height},{self.__printInterpretationLine},{self.__printInterpretationLineAboveCode},{self.__insertCheckDigitIntoInterpretationLine}"
		return format
