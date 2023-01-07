from typing import Any, Optional


class ChangeControlCommandCharacter:
	def __init__(self, controlCommandCharacter) -> None:
		"""
		The ^CT and ~CT commands are used to change the control command prefix. The default prefix is the tilde (~).
		"""
		self.__controlCommandCharacter = controlCommandCharacter

	def __str__(self) -> str:
		format = f"~CT{self.__controlCommandCharacter}"
		return format
