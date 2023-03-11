from typing import Any, Optional


class FontIdentifier:
	def __init__(self, font, deviceToStoreFont: Optional[Any], name, extension) -> None:
		"""
		All built-in fonts are referenced using a one-character identifier. The ^CW command assigns a single alphanumeric character to a font stored in DRAM, memory card, EPROM, or Flash
		"""
		self.__font = font
		self.__deviceToStoreFont = deviceToStoreFont if deviceToStoreFont else ''
		self.__name = name
		self.__extension = extension

	def __str__(self) -> str:
		format = f"^CW{self.__font},{self.__deviceToStoreFont}:{self.__name}.{self.__extension}"
		return format
