from typing import Any, Optional


class ChangeAlphanumericDefaultFont:
	def __init__(self, font, height, width) -> None:
		"""
		The ^CF command sets the default font used in your printer. You can use the ^CF command to simplify your programs.
		"""
		self.__font = font
		self.__height = height
		self.__width = width

	def __str__(self) -> str:
		format = f"^CF{self.__font},{self.__height},{self.__width}"
		return format
