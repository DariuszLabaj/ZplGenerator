from typing import Any, Optional


class LogMarsBarcode:
	def __init__(self, orientation, height, printInterpretationLine) -> None:
		"""
		The ^BL command is a special application of Code 39 used by the Department of Defense. LOGMARS is an acronym for Logistics Applications of Automated Marking and Reading Symbols.
		"""
		self.__orientation = orientation
		self.__height = height
		self.__printInterpretationLine = printInterpretationLine

	def __str__(self) -> str:
		format = f"^BL{self.__orientation},{self.__height},{self.__printInterpretationLine}"
		return format
