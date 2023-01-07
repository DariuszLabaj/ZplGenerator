from typing import Any, Optional


class DownloadBitmapFont:
	def __init__(self, deviceToStoreFont, name, extension, orientation, height, width, base, space, noOfCharacters, copyright, data) -> None:
		"""
		The ~DB command sets the printer to receive a downloaded bitmap font and defines native cell size, baseline, space size, and copyright.
		"""
		self.__deviceToStoreFont = deviceToStoreFont
		self.__name = name
		self.__extension = extension
		self.__orientation = orientation
		self.__height = height
		self.__width = width
		self.__base = base
		self.__space = space
		self.__noOfCharacters = noOfCharacters
		self.__copyright = copyright
		self.__data = data

	def __str__(self) -> str:
		format = f"~DB{self.__deviceToStoreFont}:{self.__name}.{self.__extension},{self.__orientation},{self.__height},{self.__width},{self.__base},{self.__space},{self.__noOfCharacters},{self.__copyright},{self.__data}"
		return format
