from typing import Any, Optional


class GraphicSymbol:
	def __init__(self, orientation, height, width) -> None:
		"""
		The ^GS command enables you to generate the registered trademark, copyright symbol, and other symbols.
		"""
		self.__orientation = orientation
		self.__height = height
		self.__width = width

	def __str__(self) -> str:
		format = f"^GS{self.__orientation},{self.__height},{self.__width}"
		return format
