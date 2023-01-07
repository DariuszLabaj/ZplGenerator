from typing import Any, Optional


class HostGraphic:
	def __init__(self, deviceToStoreGraphic, name, extension) -> None:
		"""
		The ^HG command is used to upload graphics to the host. The graphic image can be stored for future use, or it can be downloaded to any Zebra printer.
		"""
		self.__deviceToStoreGraphic = deviceToStoreGraphic
		self.__name = name
		self.__extension = extension

	def __str__(self) -> str:
		format = f"^HG{self.__deviceToStoreGraphic}:{self.__name}.{self.__extension}"
		return format
