from typing import Any, Optional


class SetPrintheadResistance:
	def __init__(self, value) -> None:
		"""
		The ^SR command allows you to set the printhead resistance.
		"""
		self.__value = value

	def __str__(self) -> str:
		format = f"^SR{self.__value}"
		return format
