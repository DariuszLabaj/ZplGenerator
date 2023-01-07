from typing import Any, Optional


class ScalableFontCommandByName:
	def __init__(self, fieldOrientation, height, width, driveLocation, fontName, extension) -> None:
		"""
		The ^A@ command uses the complete name of a font, rather than the character designation used in ^A. Once a value for ^A@ is defined, it represents that font until a new font name is specified by ^A@.
		"""
		self.__fieldOrientation = fieldOrientation
		self.__height = height
		self.__width = width
		self.__driveLocation = driveLocation
		self.__fontName = fontName
		self.__extension = extension

	def __str__(self) -> str:
		format = f"^A@{self.__fieldOrientation},{self.__height},{self.__width},{self.__driveLocation}:{self.__fontName}.{self.__extension}"
		return format
