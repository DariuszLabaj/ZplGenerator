from typing import Any, Optional


class FieldOrigin:
	def __init__(self, xPosition, yPosition, justification) -> None:
		"""
		The ^FO command sets a field origin, relative to the label home (^LH) position. ^FO sets the upper-left corner of the field area by defining points along the x-axis and y-axis independent of the rotation.
		"""
		self.__xPosition = xPosition
		self.__yPosition = yPosition
		self.__justification = justification

	def __str__(self) -> str:
		format = f": ^FO{self.__xPosition},{self.__yPosition},{self.__justification}"
		return format
