from typing import Any, Optional


class EAN8Barcode:
	def __init__(self, orientation, height, printInterpretationLine, printInterpretationLineAboveCode) -> None:
		"""
		The ^B8 command is the shortened version of the EAN-13 bar code. EAN is an acronym for European Article Numbering. Each character in the EAN-8 bar code is composed of four elements: two bars and two spaces.
		"""
		self.__orientation = orientation
		self.__height = height
		self.__printInterpretationLine = printInterpretationLine
		self.__printInterpretationLineAboveCode = printInterpretationLineAboveCode

	def __str__(self) -> str:
		format = f"^B8{self.__orientation},{self.__height},{self.__printInterpretationLine},{self.__printInterpretationLineAboveCode}"
		return format
