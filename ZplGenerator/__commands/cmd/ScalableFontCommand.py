from typing import Any, Optional


class ScalableFontCommand:
	def __init__(self, fontName, fieldOrientation, height, width) -> None:
		"""
		The ^A command specifies the font to use in a text field. ^A designates the font for the current ^FD statement or field. The font specified by ^A is used only once for that ^FD entry. If a value for ^A is not specified again, the default ^CF font is used for the next ^FD entry.
		"""
		self.__fontName = fontName
		self.__fieldOrientation = fieldOrientation
		self.__height = height
		self.__width = width

	def __str__(self) -> str:
		format = f"^A{self.__fontName}{self.__fieldOrientation},{self.__height},{self.__width}"
		return format
