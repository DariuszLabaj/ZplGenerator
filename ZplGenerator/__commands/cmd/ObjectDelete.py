from typing import Any, Optional


class ObjectDelete:
	def __init__(self, driveLocation, name, extension) -> None:
		"""
		The ^ID command deletes objects, graphics, fonts, and stored formats from storage areas. Objects can be deleted selectively or in groups. This command can be used within a printing format to delete objects before saving new ones, or in a stand-alone format to delete objects
		"""
		self.__driveLocation = driveLocation
		self.__name = name
		self.__extension = extension

	def __str__(self) -> str:
		format = f"^ID{self.__driveLocation}:{self.__name}.{self.__extension}"
		return format
