from typing import Any, Optional


class InitializeFlashMemory:
	def __init__(self, deviceToInitialize) -> None:
		"""
		The ^JB command is used to initialize various types of Flash memory available in the Zebra printers.
		"""
		self.__deviceToInitialize = deviceToInitialize

	def __str__(self) -> str:
		format = f"^JB{self.__deviceToInitialize}"
		return format
