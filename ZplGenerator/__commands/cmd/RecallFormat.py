from typing import Any, Optional


class RecallFormat:
	def __init__(self, sourceDevice, name, extension) -> None:
		"""
		The ^XF command recalls a stored format to be merged with variable data. There can be multiple ^XF commands in one format, and they can be located anywhere within the code.
		"""
		self.__sourceDevice = sourceDevice
		self.__name = name
		self.__extension = extension

	def __str__(self) -> str:
		format = f"^XF{self.__sourceDevice}:{self.__name}.{self.__extension}"
		return format
