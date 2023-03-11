from typing import Any, Optional


class ChangeInternationalFontEncoding:
	def __init__(self, characterSet, sources, destinations) -> None:
		"""
		The ^CI command enables you to call up the international character set you want to use for printing. You can mix character sets on a label.
		"""
		self.__characterSet = characterSet
		self.__sources = sources
		self.__destinations = destinations

	def __str__(self) -> str:
		format = f"^CIa,s1,d1,s2,d2,..."
		return format
