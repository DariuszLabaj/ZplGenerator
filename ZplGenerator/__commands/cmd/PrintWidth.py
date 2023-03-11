from typing import Any, Optional


class PrintWidth:
	def __init__(self, width) -> None:
		"""
		The ^PW command allows you to set the print width.
		"""
		self.__width = width

	def __str__(self) -> str:
		format = f"^PW{self.__width}"
		return format
