from typing import Any, Optional


class FieldTypeset:
	def __init__(self, xPosition, yPosition, justification) -> None:
		"""
		The ^FT command sets the field position, relative to the home position of the label designated by the ^LH command. The typesetting origin of the field is fixed with respect to the contents of the field and does not change with rotation.
		"""
		self.__xPosition = xPosition
		self.__yPosition = yPosition
		self.__justification = justification

	def __str__(self) -> str:
		format = f"^FT{self.__xPosition},{self.__yPosition},{self.__justification}"
		return format
