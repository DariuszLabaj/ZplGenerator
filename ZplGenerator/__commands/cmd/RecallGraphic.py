from typing import Any, Optional


class RecallGraphic:
	def __init__(self, sourceDevice, name, extension, scaleX, scaleY) -> None:
		"""
		The ^XG command is used to recall one or more graphic images for printing. This command is used in a label format to merge graphics, such as company logos and piece parts, with text data to form a complete label.
		"""
		self.__sourceDevice = sourceDevice
		self.__name = name
		self.__extension = extension
		self.__scaleX = scaleX
		self.__scaleY = scaleY

	def __str__(self) -> str:
		format = f"^XG{self.__sourceDevice}:{self.__name}.{self.__extension},{self.__scaleX},{self.__scaleY}"
		return format
