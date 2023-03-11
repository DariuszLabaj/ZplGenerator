from typing import Any, Optional


class FieldHexadecimalIndicator:
	def __init__(self, hexadecimalIndicator) -> None:
		"""
		The ^FH command allows you to enter the hexadecimal value for any character directly into the ^FD statement. The ^FH command must precede each ^FD command that uses hexadecimals in its field.
		"""
		self.__hexadecimalIndicator = hexadecimalIndicator

	def __str__(self) -> str:
		format = f"^FH{self.__hexadecimalIndicator}"
		return format
