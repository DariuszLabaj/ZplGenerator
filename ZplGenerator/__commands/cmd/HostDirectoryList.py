from typing import Any, Optional


class HostDirectoryList:
	def __init__(self, driveLocation, name, extension) -> None:
		"""
		^HW is used to transmit a directory listing of objects in a specific memory area (storage device) back to the host device. This command returns a formatted ASCII string of object names to the host.
		"""
		self.__driveLocation = driveLocation
		self.__name = name
		self.__extension = extension

	def __str__(self) -> str:
		format = f"^HW{self.__driveLocation}:{self.__name}.{self.__extension}"
		return format
