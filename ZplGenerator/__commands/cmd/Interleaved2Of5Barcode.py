from typing import Any, Optional


class Interleaved2Of5Barcode:
	def __init__(self, orientation, height, printInterpretationLine, printInterpretationLineAboveCode, calculateAndPrintMod10CheckDigit) -> None:
		"""
		The ^B2 command produces the Interleaved 2 of 5 bar code, a high-density, self-checking, continuous, numeric symbology
		"""
		self.__orientation = orientation
		self.__height = height
		self.__printInterpretationLine = printInterpretationLine
		self.__printInterpretationLineAboveCode = printInterpretationLineAboveCode
		self.__calculateAndPrintMod10CheckDigit = calculateAndPrintMod10CheckDigit

	def __str__(self) -> str:
		format = f"^B2{self.__orientation},{self.__height},{self.__printInterpretationLine},{self.__printInterpretationLineAboveCode},{self.__calculateAndPrintMod10CheckDigit}"
		return format
