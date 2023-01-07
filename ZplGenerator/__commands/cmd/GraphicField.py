from typing import Any, Optional


class GraphicField:
	def __init__(self, compressionType, noOfBytes, graphicFieldCount, noOfBytesInRow, data) -> None:
		"""
		The ^GF command allows you to download graphic field data directly into the printer’s bitmap storage area. This command follows the conventions for any other field, meaning a field orientation is included. The graphic field data can be placed at any location within the bitmap space.
		"""
		self.__compressionType = compressionType
		self.__noOfBytes = noOfBytes
		self.__graphicFieldCount = graphicFieldCount
		self.__noOfBytesInRow = noOfBytesInRow
		self.__data = data

	def __str__(self) -> str:
		format = f"^GF{self.__compressionType},{self.__noOfBytes},{self.__graphicFieldCount},{self.__noOfBytesInRow},{self.__data}"
		return format
