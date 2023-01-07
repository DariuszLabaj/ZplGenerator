from typing import Any, Optional


class DownloadGraphics:
	def __init__(self, deviceToStoreImage, name, extension, noOfBytes, noOfBytesInRow, data) -> None:
		"""
		The ~DG command downloads an ASCII Hex representation of a graphic image. If .GRF is not the specified file extension, .GRF is automatically appended.
		"""
		self.__deviceToStoreImage = deviceToStoreImage
		self.__name = name
		self.__extension = extension
		self.__noOfBytes = noOfBytes
		self.__noOfBytesInRow = noOfBytesInRow
		self.__data = data

	def __str__(self) -> str:
		format = f"~DG{self.__deviceToStoreImage}:{self.__name}.{self.__extension},{self.__noOfBytes},{self.__noOfBytesInRow},{self.__data}"
		return format
