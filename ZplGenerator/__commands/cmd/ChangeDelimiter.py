from typing import Any, Optional


class ChangeDelimiter:
	def __init__(self, delimiterCharacter) -> None:
		"""
		The ^CD and ~CD commands are used to change the delimiter character. This character is used to separate parameter values associated with several ZPL II commands. The default delimiter is a comma (,).
		"""
		self.__delimiterCharacter = delimiterCharacter

	def __str__(self) -> str:
		format = f"~CD{self.__delimiterCharacter}"
		return format
