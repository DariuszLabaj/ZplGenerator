from typing import Any, Optional


class EraseDownloadGraphics:
	def __init__(self, driveLocation, name, extension) -> None:
		"""
		Erase Download Graphics
		"""
		self.__driveLocation = driveLocation
		self.__name = name
		self.__extension = extension

	def __str__(self) -> str:
		format = f"~EG"
		return format
