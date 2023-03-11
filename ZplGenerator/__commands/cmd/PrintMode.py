from typing import Any, Optional


class PrintMode:
	def __init__(self, desiredMode, prePeelSelect) -> None:
		"""
		The ^MM command determines the action the printer takes after a label or group of labels has printed.
		"""
		self.__desiredMode = desiredMode
		self.__prePeelSelect = prePeelSelect

	def __str__(self) -> str:
		format = f"^MM{self.__desiredMode},{self.__prePeelSelect}"
		return format
