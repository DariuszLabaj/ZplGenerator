from typing import Any, Optional


class ImageMove:
	def __init__(self, driveLocation, name, extension) -> None:
		"""
		The ^IM command performs a direct move of an image from storage area into the bitmap. The command is identical to the ^XG command (Recall Graphic), except there are no sizing parameters.
		"""
		self.__driveLocation = driveLocation
		self.__name = name
		self.__extension = extension

	def __str__(self) -> str:
		format = f"^IM{self.__driveLocation}:{self.__name}.{self.__extension}"
		return format
