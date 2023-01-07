from typing import Any, Optional


class DownloadBoundedTrueTypeFont:
	def __init__(self, deviceToStoreFont, name, extension, noOfBytes, data) -> None:
		"""
		Use ZTools to convert a TrueType font to a Zebra-downloadable format. that has less than 256 characters in it. To convert a font that has more than 256 characters, see ~DU 
		"""
		self.__deviceToStoreFont = deviceToStoreFont
		self.__name = name
		self.__extension = extension
		self.__noOfBytes = noOfBytes
		self.__data = data

	def __str__(self) -> str:
		format = f"~DT{self.__deviceToStoreFont}:{self.__name}.{self.__extension},{self.__noOfBytes},{self.__data}"
		return format
