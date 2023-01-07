from typing import Any, Optional


class Code49Barcode:
	def __init__(self, orientation, height, printInterpretationLine, startingMode) -> None:
		"""
		The ^B4 command creates a multi-row, continuous, variable-length symbology capable of encoding the full 128-character ASCII set. It is ideally suited for applications requiring large amounts of data in a small space.
		"""
		self.__orientation = orientation
		self.__height = height
		self.__printInterpretationLine = printInterpretationLine
		self.__startingMode = startingMode

	def __str__(self) -> str:
		format = f"^B4{self.__orientation},{self.__height},{self.__printInterpretationLine},{self.__startingMode}"
		return format
