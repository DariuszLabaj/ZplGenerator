from typing import Any, Optional


class HaltZebraNetAlert:
	def __init__(self, conditionType, destination, haltMessages) -> None:
		"""
		The ^SQ command is used to stop the ZebraNet Alert option
		"""
		self.__conditionType = conditionType
		self.__destination = destination
		self.__haltMessages = haltMessages

	def __str__(self) -> str:
		format = f"^SQ{self.__conditionType},{self.__destination},{self.__haltMessages}"
		return format
