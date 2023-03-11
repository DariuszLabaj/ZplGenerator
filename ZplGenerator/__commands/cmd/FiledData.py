from typing import Any, Optional


class FiledData:
	def __init__(self, data) -> None:
		"""
		The ^FD command defines the data string for a field. The field data can be any printable character except those used as command prefixes (^ and ~).
		"""
		self.__data = data

	def __str__(self) -> str:
		format = f"^FD{self.__data}"
		return format
