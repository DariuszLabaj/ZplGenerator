from typing import Any, Optional


class PlanetCodeBarcode:
	def __init__(self, orientation, height, printInterpretationLine, printInterpretationLineAboveCode) -> None:
		"""
		The ^B5 command is supported in all printers as a resident bar code. Accepted bar code characters are 0-9.
		"""
		self.__orientation = orientation
		self.__height = height
		self.__printInterpretationLine = printInterpretationLine
		self.__printInterpretationLineAboveCode = printInterpretationLineAboveCode

	def __str__(self) -> str:
		format = f"^B5{self.__orientation},{self.__height},{self.__printInterpretationLine},{self.__printInterpretationLineAboveCode}"
		return format
