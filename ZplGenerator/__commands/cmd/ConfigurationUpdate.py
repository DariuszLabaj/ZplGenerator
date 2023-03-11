from typing import Any, Optional


class ConfigurationUpdate:
	def __init__(self, activeConfiguration) -> None:
		"""
		The ^JU command sets the active configuration for the printer.
		"""
		self.__activeConfiguration = activeConfiguration

	def __str__(self) -> str:
		format = f"^JU{self.__activeConfiguration}"
		return format
