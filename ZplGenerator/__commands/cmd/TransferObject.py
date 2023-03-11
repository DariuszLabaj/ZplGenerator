from typing import Any, Optional


class TransferObject:
	def __init__(self, sourceDevice, sourceName, sourceExtension, destinationDevice, destinationName, destinationExtension) -> None:
		"""
		The ^TO command is used to copy an object or group of objects from one storage device to another. It is similar to the copy function used in PCs.
		"""
		self.__sourceDevice = sourceDevice
		self.__sourceName = sourceName
		self.__sourceExtension = sourceExtension
		self.__destinationDevice = destinationDevice
		self.__destinationName = destinationName
		self.__destinationExtension = destinationExtension

	def __str__(self) -> str:
		format = f"^TO{self.__sourceDevice}:{self.__sourceName}.{self.__sourceExtension},{self.__destinationDevice}:{self.__destinationName}.{self.__destinationExtension}"
		return format
