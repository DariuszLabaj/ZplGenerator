from typing import Any, Optional


class ImageSave:
	def __init__(self, driveLocation, name, extension, printImageAfterStoring) -> None:
		"""
		The ^IS command is used within a label format to save that format as a graphic image, rather than as a ZPL II script. It is typically used toward the end of a script. The saved image can later be recalled with virtually no formatting time and overlaid with variable data to form a complete label
		"""
		self.__driveLocation = driveLocation
		self.__name = name
		self.__extension = extension
		self.__printImageAfterStoring = printImageAfterStoring

	def __str__(self) -> str:
		format = f"^IS{self.__driveLocation}:{self.__name}.{self.__extension},{self.__printImageAfterStoring}"
		return format
