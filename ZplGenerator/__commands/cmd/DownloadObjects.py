from typing import Any, Optional


class DownloadObjects:
	def __init__(self, deviceToStore, name, format, extension, noOfBytes, noOfBytesInRow, data) -> None:
		"""
		The ~DY command downloads to the printer graphic objects or fonts in any supported format. This command can be used in place of ~DG for more saving and loading options. ~DY is the preferred command to download TrueType fonts on printers with firmware later than X.13. It is faster than ~DU. The ~DY command also supports downloading wireless certificate files.
		"""
		self.__deviceToStore = deviceToStore
		self.__name = name
		self.__format = format
		self.__extension = extension
		self.__noOfBytes = noOfBytes
		self.__noOfBytesInRow = noOfBytesInRow
		self.__data = data

	def __str__(self) -> str:
		format = f"~DY{self.__deviceToStore}:{self.__name},{self.__format},{self.__extension},{self.__noOfBytes},{self.__noOfBytesInRow},{self.__data}"
		return format
