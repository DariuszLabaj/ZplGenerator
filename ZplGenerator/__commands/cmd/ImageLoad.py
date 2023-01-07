from typing import Any, Optional


class ImageLoad:
	def __init__(self, driveLocation, name, extension) -> None:
		"""
		The ^IL command is used at the beginning of a label format to load a stored image of a format and merge it with additional data. The image is always positioned at ^FO0,0.
		"""
		self.__driveLocation = driveLocation
		self.__name = name
		self.__extension = extension

	def __str__(self) -> str:
		format = f"^IL{self.__driveLocation}:{self.__name}.{self.__extension}"
		return format
