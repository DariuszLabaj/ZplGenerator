from typing import Any, Optional


class Industrial2Of5Barcode:
	def __init__(self, orientation, height, printInterpretationLine, printInterpretationLineAboveCode) -> None:
		"""
		The ^BI command is a discrete, self-checking, continuous numeric symbology. The Industrial 2 of 5 bar code has been in use the longest of the 2 of 5 family of bar codes. Of that family, the Standard 2 of 5 (^BJ) and Interleaved 2 of 5 (^B2) bar codes are also available in ZPL II.
		"""
		self.__orientation = orientation
		self.__height = height
		self.__printInterpretationLine = printInterpretationLine
		self.__printInterpretationLineAboveCode = printInterpretationLineAboveCode

	def __str__(self) -> str:
		format = f"^BI{self.__orientation},{self.__height},{self.__printInterpretationLine},{self.__printInterpretationLineAboveCode}"
		return format
