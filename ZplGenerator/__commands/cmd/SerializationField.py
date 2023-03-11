from typing import Any, Optional


class SerializationField:
	def __init__(self, maskString, incrementString) -> None:
		"""
		The ^SF command allows you to serialize a standard ^FD string. The maximum size of the mask and increment string is 3K combined.
		"""
		self.__maskString = maskString
		self.__incrementString = incrementString

	def __str__(self) -> str:
		format = f"^SF{self.__maskString},{self.__incrementString}"
		return format
