from typing import Any, Optional


class PlesseyBarcode:
	def __init__(self, orientation, checkDigit, height, printInterpretationLine, printInterpretationLineAboveCode) -> None:
		"""
		The ^BP command is a pulse-width modulated, continuous, non-self- checking symbology.
		"""
		self.__orientation = orientation
		self.__checkDigit = checkDigit
		self.__height = height
		self.__printInterpretationLine = printInterpretationLine
		self.__printInterpretationLineAboveCode = printInterpretationLineAboveCode

	def __str__(self) -> str:
		format = f"^BP{self.__orientation},{self.__checkDigit},{self.__height},{self.__printInterpretationLine},{self.__printInterpretationLineAboveCode}"
		return format
