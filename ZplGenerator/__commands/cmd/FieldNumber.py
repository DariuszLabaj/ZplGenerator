from typing import Any, Optional


class FieldNumber:
	def __init__(self, number, data: Optional[Any]) -> None:
		"""
		The ^FN command numbers the data fields. This command is used in both ^DF (Store Format) and ^XF (Recall Format) commands
		"""
		self.__number = number
		self.__data = data if data else ''

	def __str__(self) -> str:
		format = f"^FN{self.__number}"{self.__data}""
		return format
