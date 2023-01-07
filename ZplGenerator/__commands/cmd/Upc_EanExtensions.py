from typing import Any, Optional


class Upc_EanExtensions:
	def __init__(self, orientation, height, printInterpretationLine, printInterpretationLineAboveCode) -> None:
		"""
		The ^BS command is the two-digit and five-digit add-on used primarily by publishers to create bar codes for ISBNs (International Standard Book Numbers). These extensions are handled as separate bar codes.
		"""
		self.__orientation = orientation
		self.__height = height
		self.__printInterpretationLine = printInterpretationLine
		self.__printInterpretationLineAboveCode = printInterpretationLineAboveCode

	def __str__(self) -> str:
		format = f"^BS{self.__orientation},{self.__height},{self.__printInterpretationLine},{self.__printInterpretationLineAboveCode}"
		return format
