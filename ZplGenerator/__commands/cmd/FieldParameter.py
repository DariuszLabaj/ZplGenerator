from typing import Any, Optional


class FieldParameter:
	def __init__(self, direction, charGap) -> None:
		"""
		The ^FP command allows vertical and reverse formatting of the font field, commonly used for printing Asian fonts.
		"""
		self.__direction = direction
		self.__charGap = charGap

	def __str__(self) -> str:
		format = f"^FP{self.__direction},{self.__charGap}"
		return format
