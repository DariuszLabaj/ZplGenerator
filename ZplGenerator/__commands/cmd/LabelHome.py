from typing import Any, Optional


class LabelHome:
	def __init__(self, xPosition, yPosition) -> None:
		"""
		The ^LH command sets the label home position.
		"""
		self.__xPosition = xPosition
		self.__yPosition = yPosition

	def __str__(self) -> str:
		format = f"^LH{self.__xPosition},{self.__yPosition}"
		return format
