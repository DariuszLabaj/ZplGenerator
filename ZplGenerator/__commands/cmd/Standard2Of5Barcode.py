from typing import Any, Optional


class Standard2Of5Barcode:
	def __init__(self, orientation, height, printInterpretationLine, printInterpretationLineAboveCode) -> None:
		"""
		The ^BJ command is a discrete, self-checking, continuous numeric symbology.
		"""
		self.__orientation = orientation
		self.__height = height
		self.__printInterpretationLine = printInterpretationLine
		self.__printInterpretationLineAboveCode = printInterpretationLineAboveCode

	def __str__(self) -> str:
		format = f"^BJ{self.__orientation},{self.__height},{self.__printInterpretationLine},{self.__printInterpretationLineAboveCode}"
		return format
