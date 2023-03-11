from typing import Any, Optional


class SelectEncodingTable:
	def __init__(self, locationOfEncodingTable, nameOfEncodingTable, extension) -> None:
		"""
		The ^SE command is used to select the desired ZPL or ZPL II encoding table
		"""
		self.__locationOfEncodingTable = locationOfEncodingTable
		self.__nameOfEncodingTable = nameOfEncodingTable
		self.__extension = extension

	def __str__(self) -> str:
		format = f"^SE{self.__locationOfEncodingTable}:{self.__nameOfEncodingTable}.{self.__extension}"
		return format
