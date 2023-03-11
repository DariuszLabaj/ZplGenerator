from typing import Any, Optional


class DownloadFormat:
	def __init__(self, deviceToStoreFormat, name, extension) -> None:
		"""
		The ^DF command saves ZPL II format commands as text strings to be later merged using ^XF with variable data. The format to be stored might contain field number (^FN) commands to be referenced when recalled.
		"""
		self.__deviceToStoreFormat = deviceToStoreFormat
		self.__name = name
		self.__extension = extension

	def __str__(self) -> str:
		format = f"^DF{self.__deviceToStoreFormat}:{self.__name}.{self.__extension}"
		return format
