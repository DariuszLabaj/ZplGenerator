from typing import Any, Optional


class DownloadUnboundedTrueTypeFont:
	def __init__(self, deviceToStoreFont, name, extension, noOfBytes, data) -> None:
		"""
		Some international fonts, such as Asian fonts, have more than 256 printable characters. These fonts are supported as large TrueType fonts and are downloaded to the printer with the ~DU command.
		"""
		self.__deviceToStoreFont = deviceToStoreFont
		self.__name = name
		self.__extension = extension
		self.__noOfBytes = noOfBytes
		self.__data = data

	def __str__(self) -> str:
		format = f"~DU{self.__deviceToStoreFont}:{self.__name}.{self.__extension},{self.__noOfBytes},{self.__data}"
		return format
