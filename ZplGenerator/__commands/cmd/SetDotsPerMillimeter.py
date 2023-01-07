from typing import Any, Optional


class SetDotsPerMillimeter:
	def __init__(self, value) -> None:
		"""
		The ^JM command lowers the density of the print—24 dots/mm becomes 12, 12 dots/mm becomes 6, 8 dots/mm becomes 4, and 6 dots/mm becomes 3. ^JM also affects the field origin (^FO) placement on the label (see example below).
		"""
		self.__value = value

	def __str__(self) -> str:
		format = f"^JM{self.__value}"
		return format
