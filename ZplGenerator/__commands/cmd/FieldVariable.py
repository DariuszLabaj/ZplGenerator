from typing import Any, Optional


class FieldVariable:
	def __init__(self, data) -> None:
		"""
		^FV replaces the ^FD (field data) command in a label format when the field is variable.
		"""
		self.__data = data

	def __str__(self) -> str:
		format = f"^FV{self.__data}"
		return format
