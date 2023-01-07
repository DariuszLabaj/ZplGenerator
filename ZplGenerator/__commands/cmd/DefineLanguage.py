from typing import Any, Optional


class DefineLanguage:
	def __init__(self, language) -> None:
		"""
		The ^KL command selects the language displayed on the control panel.
		"""
		self.__language = language

	def __str__(self) -> str:
		format = f"^KL{self.__language}"
		return format
