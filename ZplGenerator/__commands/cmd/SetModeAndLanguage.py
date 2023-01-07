from typing import Any, Optional


class SetModeAndLanguage:
	def __init__(self, mode, language) -> None:
		"""
		The ^SL command is used to specify the Real-Time Clock’s mode of operation and language for printing information.
		"""
		self.__mode = mode
		self.__language = language

	def __str__(self) -> str:
		format = f"^SL{self.__mode},{self.__language}"
		return format
