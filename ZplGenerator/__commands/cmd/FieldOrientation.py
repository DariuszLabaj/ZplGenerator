from typing import Any, Optional


class FieldOrientation:
	def __init__(self, rotation, justification) -> None:
		"""
		The ^FW command sets the default orientation for all command fields that have an orientation (rotation) parameter (and in x.14 sets the default justification for all commands with a justification parameter). Fields can be rotated 0, 90, 180, or 270 degrees clockwise by using this command. In x.14, justification can be left, right, or auto
		"""
		self.__rotation = rotation
		self.__justification = justification

	def __str__(self) -> str:
		format = f"^FW{self.__rotation},{self.__justification}"
		return format
