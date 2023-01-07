from typing import Any, Optional


class PrintDirectoryLabel:
	def __init__(self, sourceDevice: Optional[Any], name: Optional[Any], extension: Optional[Any]) -> None:
		"""
		The ^WD command is used to print a label listing bar codes, objects stored in DRAM, or fonts.
		"""
		self.__sourceDevice = sourceDevice if sourceDevice else ''
		self.__name = name if name else ''
		self.__extension = extension if extension else ''

	def __str__(self) -> str:
		format = f"^WD{self.__sourceDevice}:{self.__name}.{self.__extension}"
		return format
