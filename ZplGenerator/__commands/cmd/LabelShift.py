from typing import Any, Optional


class LabelShift:
	def __init__(self, shiftLeftValue) -> None:
		"""
		The ^LS command allows for compatibility with Z-130 printer formats that are set for less than full label width. It is used to shift all field positions to the left so the same commands used on a Z-130 or Z-220 Printer can be used on other Zebra printers
		"""
		self.__shiftLeftValue = shiftLeftValue

	def __str__(self) -> str:
		format = f"^LS{self.__shiftLeftValue}"
		return format
