from typing import Any, Optional


class HostFormat:
	def __init__(self, driveLocation, name, extension) -> None:
		"""
		The ^HF command sends stored formats to the host.
		"""
		self.__driveLocation = driveLocation
		self.__name = name
		self.__extension = extension

	def __str__(self) -> str:
		format = f"^HF{self.__driveLocation},{self.__name}.{self.__extension}"
		return format
