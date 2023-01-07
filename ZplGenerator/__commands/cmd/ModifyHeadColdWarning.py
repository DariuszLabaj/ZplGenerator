from typing import Any, Optional


class ModifyHeadColdWarning:
	def __init__(self, enableHeadColdWarning) -> None:
		"""
		The ^MW command allows you to set the head cold warning indicator based on the operating environment.
		"""
		self.__enableHeadColdWarning = enableHeadColdWarning

	def __str__(self) -> str:
		format = f"^MW{self.__enableHeadColdWarning}"
		return format
