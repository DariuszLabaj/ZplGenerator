from typing import Any, Optional


class DownloadScalableFont:
	def __init__(self, deviceToStoreFont, name, extension, noOfBytes, data) -> None:
		"""
		The ~DS command is used to set the printer to receive a downloadable scalable font and defines the size of the font in bytes.
		"""
		self.__deviceToStoreFont = deviceToStoreFont
		self.__name = name
		self.__extension = extension
		self.__noOfBytes = noOfBytes
		self.__data = data

	def __str__(self) -> str:
		format = f"~DS{self.__deviceToStoreFont}:{self.__name}.{self.__extension},{self.__noOfBytes},{self.__data}"
		return format
