from typing import Any, Optional


class ChangeCaret:
	def __init__(self, caretCharacter) -> None:
		"""
		The ^CC command is used to change the format command prefix. The default prefix is the caret (^).
		"""
		self.__caretCharacter = caretCharacter

	def __str__(self) -> str:
		format = f"~CC{self.__caretCharacter}"
		return format
