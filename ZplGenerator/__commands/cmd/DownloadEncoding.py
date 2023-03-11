from typing import Any, Optional


class DownloadEncoding:
	def __init__(self, deviceToStoreTable, name, extension, tableSize, data) -> None:
		"""
		The standard encoding for TrueType Windows® fonts is always Unicode. The ZPL II field data must be converted from some other encoding to Unicode that the Zebra printer understands. The required translation tables are provided with font packs. Some tables can be downloaded from zebra.com.
		"""
		self.__deviceToStoreTable = deviceToStoreTable
		self.__name = name
		self.__extension = extension
		self.__tableSize = tableSize
		self.__data = data

	def __str__(self) -> str:
		format = f"~DE{self.__deviceToStoreTable}:{self.__name}.{self.__extension},{self.__tableSize},{self.__data}"
		return format
